import logging
import re
from datetime import datetime, timezone
from typing import Dict

from src.core.config import AppConfig
from src.core.models import Article, ArticleState, PipelineState
from src.extract.zendesk import ZendeskExtractor
from src.transform.markdown import MarkdownTransformer
from src.delta.detector import DeltaDetector
from src.load.gemini import GeminiLoader
from src.utils.hash import calculate_sha256

logger = logging.getLogger("pipeline")

class SyncPipeline:
    def __init__(self, config: AppConfig):
        self.config = config
        self.extractor = ZendeskExtractor(config.zendesk)
        self.transformer = MarkdownTransformer()
        self.detector = DeltaDetector(config.pipeline.state_file)
        self.loader = GeminiLoader(config.gemini)
        
        # Ensure directories exist
        self.config.pipeline.data_dir.mkdir(parents=True, exist_ok=True)
        self.config.pipeline.articles_dir.mkdir(parents=True, exist_ok=True)

    def run(self) -> None:
        """Runs the ETL synchronization pipeline."""
        logger.info("Starting OptiBot Data Synchronization Pipeline run...")
        start_time = datetime.now(timezone.utc)
        
        try:
            prev_state = self.detector.load_state()
        except Exception as e:
            logger.error(f"Failed to load previous pipeline state: {e}. Proceeding with fresh state.")
            prev_state = PipelineState(last_sync="", articles={})
        
        try:
            fetched_articles = self.extractor.fetch_articles()
        except Exception as e:
            logger.critical(f"Extraction failed: {e}. Aborting pipeline run.", exc_info=True)
            return

        logger.info("Transforming HTML bodies to Markdown and computing hashes...")
        for article in fetched_articles:
            try:
                markdown_content = self.transformer.transform(article)
                article.hash_val = calculate_sha256(markdown_content)
                # Assign file path (using clean slug)
                locale_dir = self.config.pipeline.articles_dir / article.locale.lower()
                safe_slug = re.sub(r'[^a-zA-Z0-9_\-]', '', article.slug)
                article.file_path = locale_dir / f"{safe_slug}.md"
            except Exception as e:
                logger.error(f"Failed to transform article {article.id}: {e}")
                continue

        added, updated, deleted = self.detector.detect_deltas(fetched_articles, prev_state)
        logger.info(f"Deltas detected: {len(added)} added, {len(updated)} updated, {len(deleted)} deleted.")

        new_articles_state: Dict[str, ArticleState] = {
            k: v for k, v in prev_state.articles.items()
        }

        # Track successfully processed deltas for stats
        added_count = 0
        updated_count = 0
        deleted_count = 0

        # Helper to process a single article (Write file & Upload to Gemini)
        def process_article(art: Article) -> bool:
            try:
                # 1. Write file to local disk
                art.file_path.parent.mkdir(parents=True, exist_ok=True)
                art.file_path.write_text(art.body_markdown, encoding="utf-8")
                
                # 2. Upload and index in Gemini
                if self.loader.upload_article(art):
                    new_articles_state[str(art.id)] = ArticleState(
                        id=art.id,
                        slug=art.slug,
                        hash_val=art.hash_val,
                        updated_at=art.updated_at.isoformat() if art.updated_at else datetime.now(timezone.utc).isoformat(),
                        gemini_file_name=art.gemini_file_name,
                        gemini_uri=art.gemini_uri,
                        locale=art.locale
                    )
                    # Save state incrementally
                    self.detector.save_state(PipelineState(
                        last_sync=start_time.isoformat(),
                        articles=new_articles_state
                    ))
                    return True
                else:
                    logger.error(f"Failed to upload article {art.id} to Gemini.")
                    return False
            except Exception as e:
                logger.error(f"Error processing article {art.id}: {e}")
                return False

        # Process additions
        for article in added:
            logger.info(f"Processing new article {article.id} ({article.title})")
            if process_article(article):
                added_count += 1

        # Process updates
        for article in updated:
            logger.info(f"Processing updated article {article.id} ({article.title})")
            if process_article(article):
                updated_count += 1

        # Process deletions
        for state in deleted:
            logger.info(f"Processing deleted article {state.id}")
            
            # 1. Delete from Gemini
            if state.gemini_file_name:
                self.loader.delete_gemini_document(state.gemini_file_name)
            
            # 2. Delete local file
            filename = f"{state.slug}.md"
            file_path = self.config.pipeline.articles_dir / state.locale.lower() / filename
            deleted_locally = False
            
            try:
                if file_path.exists():
                    file_path.unlink()
                    deleted_locally = True
                else:
                    # Fallback to search if locale folder mismatched
                    for p in self.config.pipeline.articles_dir.rglob(filename):
                        if p.is_file():
                            p.unlink()
                            deleted_locally = True
            except OSError as e:
                logger.error(f"Failed to delete local file for article {state.id}: {e}")

            if not deleted_locally:
                logger.warning(f"Local file for deleted article {state.id} ({filename}) was not found on disk.")
                
            new_articles_state.pop(str(state.id), None)
            self.detector.save_state(PipelineState(
                last_sync=start_time.isoformat(),
                articles=new_articles_state
            ))
            deleted_count += 1

        # Save new pipeline state
        new_state = PipelineState(
            last_sync=start_time.isoformat(),
            articles=new_articles_state
        )
        self.detector.save_state(new_state)
        
        # Calculate skipped
        skipped_count = len(fetched_articles) - len(added) - len(updated)
        
        logger.info("=========================================")
        logger.info("Sync Job Execution Counts:")
        logger.info(f" - Added: {added_count} (Remote & Local)")
        logger.info(f" - Updated: {updated_count} (Remote & Local)")
        logger.info(f" - Deleted: {deleted_count} (Remote & Local)")
        logger.info(f" - Skipped: {skipped_count} (Already up-to-date)")
        logger.info("=========================================")
        logger.info("Pipeline sync run completed successfully.")
