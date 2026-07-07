import os
from datetime import datetime, timezone
from typing import Dict
from src.core.config import AppConfig
from src.core.models import Article, ArticleState, PipelineState
from src.extract.zendesk import ZendeskExtractor
from src.transform.markdown import MarkdownTransformer
from src.delta.detector import DeltaDetector
from src.load.gemini import GeminiLoader
from src.utils.hash import calculate_sha256
from src.utils.logger import setup_logger

logger = setup_logger("pipeline")

class SyncPipeline:
    def __init__(self, config: AppConfig):
        self.config = config
        self.extractor = ZendeskExtractor(config.zendesk)
        self.transformer = MarkdownTransformer()
        self.detector = DeltaDetector(config.pipeline.state_file)
        self.loader = GeminiLoader(config.gemini)
        
        os.makedirs(self.config.pipeline.data_dir, exist_ok=True)
        os.makedirs(self.config.pipeline.articles_dir, exist_ok=True)

    def run(self) -> None:
        logger.info("Starting OptiBot Data Synchronization Pipeline run...")
        start_time = datetime.now(timezone.utc)
        
        prev_state = self.detector.load_state()
        
        try:
            fetched_articles = self.extractor.fetch_articles()
        except Exception as e:
            logger.critical(f"Failed to fetch articles: {e}. Aborting pipeline.")
            return

        logger.info("Transforming HTML bodies to Markdown and computing hashes...")
        for article in fetched_articles:
            markdown_content = self.transformer.transform(article)
            article.hash_val = calculate_sha256(markdown_content)
            
            locale_dir = os.path.join(self.config.pipeline.articles_dir, article.locale)
            os.makedirs(locale_dir, exist_ok=True)
            # Use slug for filename scheme as requested
            article.file_path = os.path.abspath(os.path.join(locale_dir, f"{article.slug}.md"))

        added, updated, deleted = self.detector.detect_deltas(fetched_articles, prev_state)
        
        logger.info(f"Deltas detected: {len(added)} added, {len(updated)} updated, {len(deleted)} deleted.")

        new_articles_state: Dict[str, ArticleState] = {}
        for k, v in prev_state.articles.items():
            new_articles_state[k] = v

        def write_article_file(art: Article) -> bool:
            try:
                with open(art.file_path, "w", encoding="utf-8") as f:
                    f.write(art.body_markdown)
                return True
            except Exception as e:
                logger.error(f"Failed to write article file for {art.id} to {art.file_path}: {e}")
                return False

        # Track successfully processed deltas to build logging statistics
        added_count = 0
        updated_count = 0
        deleted_count = 0

        for article in added:
            logger.info(f"Processing new article {article.id} ({article.title})")
            if write_article_file(article):
                if self.loader.upload_article(article):
                    new_articles_state[str(article.id)] = ArticleState(
                        id=article.id,
                        slug=article.slug,
                        hash_val=article.hash_val,
                        updated_at=article.updated_at.isoformat() if article.updated_at else datetime.now(timezone.utc).isoformat(),
                        gemini_file_name=article.gemini_file_name,
                        gemini_uri=article.gemini_uri
                    )
                    added_count += 1

        for article in updated:
            logger.info(f"Processing updated article {article.id} ({article.title})")
            if write_article_file(article):
                if self.loader.upload_article(article):
                    new_articles_state[str(article.id)] = ArticleState(
                        id=article.id,
                        slug=article.slug,
                        hash_val=article.hash_val,
                        updated_at=article.updated_at.isoformat() if article.updated_at else datetime.now(timezone.utc).isoformat(),
                        gemini_file_name=article.gemini_file_name,
                        gemini_uri=article.gemini_uri
                    )
                    updated_count += 1

        for state in deleted:
            logger.info(f"Processing deleted article {state.id}")
            if state.gemini_file_name:
                self.loader.delete_gemini_document(state.gemini_file_name)
            
            found_local_file = False
            for root, _, files in os.walk(self.config.pipeline.articles_dir):
                filename = f"{state.slug}.md"
                if filename in files:
                    file_to_delete = os.path.join(root, filename)
                    try:
                        os.remove(file_to_delete)
                        logger.info(f"Removed local file: {file_to_delete}")
                        found_local_file = True
                    except Exception as e:
                        logger.error(f"Failed to remove local file {file_to_delete}: {e}")
            if not found_local_file:
                logger.info(f"Local file for deleted article {state.id} ({state.slug}.md) was not found on disk.")
                
            new_articles_state.pop(str(state.id), None)
            deleted_count += 1

        new_state = PipelineState(
            last_sync=start_time.isoformat(),
            articles=new_articles_state
        )
        self.detector.save_state(new_state)
        
        # Calculate skipped (articles that were already up to date)
        skipped_count = len(fetched_articles) - len(added) - len(updated)
        
        # Log job counts as explicitly required
        logger.info("=========================================")
        logger.info("Sync Job Execution Counts:")
        logger.info(f" - Added: {added_count} (Remote & Local)")
        logger.info(f" - Updated: {updated_count} (Remote & Local)")
        logger.info(f" - Deleted: {deleted_count} (Remote & Local)")
        logger.info(f" - Skipped: {skipped_count} (Already up-to-date)")
        logger.info("=========================================")
        logger.info("Pipeline sync run completed successfully.")
