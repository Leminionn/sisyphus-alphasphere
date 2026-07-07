import json
import logging
from pathlib import Path
from typing import Dict, List, Tuple
from src.core.models import Article, ArticleState, PipelineState

logger = logging.getLogger("delta_detector")

class DeltaDetector:
    def __init__(self, state_file_path: Path):
        self.state_file_path = Path(state_file_path)

    def load_state(self) -> PipelineState:
        """
        Loads the pipeline sync state from the state file.
        If the file does not exist, starts fresh.
        If corrupted, backs it up and starts fresh to prevent blocking subsequent runs.
        """
        if not self.state_file_path.exists():
            logger.info("No previous state file found. Starting fresh.")
            return PipelineState(last_sync="", articles={})
        
        try:
            content = self.state_file_path.read_text(encoding="utf-8")
            if not content.strip():
                return PipelineState(last_sync="", articles={})
                
            data = json.loads(content)
            
            articles_data = data.get("articles", {})
            articles_state = {}
            for k, v in articles_data.items():
                articles_state[k] = ArticleState(
                    id=v["id"],
                    slug=v.get("slug", ""),
                    hash_val=v["hash_val"],
                    updated_at=v["updated_at"],
                    gemini_file_name=v.get("gemini_file_name", ""),
                    gemini_uri=v.get("gemini_uri", ""),
                    locale=v.get("locale", "en-us")  # Backward compatibility
                )
            
            return PipelineState(
                last_sync=data.get("last_sync", ""),
                articles=articles_state
            )
        except (json.JSONDecodeError, KeyError) as e:
            backup_path = self.state_file_path.with_suffix(".json.bak")
            logger.error(f"State file is corrupted: {e}. Backing up to {backup_path} and starting fresh.")
            try:
                if self.state_file_path.exists():
                    self.state_file_path.replace(backup_path)
            except OSError as ex:
                logger.error(f"Failed to backup corrupted state file: {ex}")
            return PipelineState(last_sync="", articles={})

    def save_state(self, state: PipelineState) -> None:
        """Saves the pipeline sync state to the state file."""
        self.state_file_path.parent.mkdir(parents=True, exist_ok=True)
            
        data = {
            "last_sync": state.last_sync,
            "articles": {
                k: {
                    "id": v.id,
                    "slug": v.slug,
                    "hash_val": v.hash_val,
                    "updated_at": v.updated_at,
                    "gemini_file_name": v.gemini_file_name,
                    "gemini_uri": v.gemini_uri,
                    "locale": v.locale
                } for k, v in state.articles.items()
            }
        }
        
        try:
            # Write atomically or simply write text
            temp_file = self.state_file_path.with_suffix(".tmp")
            temp_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
            temp_file.replace(self.state_file_path)
            logger.info(f"Sync state saved to {self.state_file_path}.")
        except OSError as e:
            logger.error(f"Failed to save sync state to {self.state_file_path}: {e}")

    def detect_deltas(self, current_articles: List[Article], previous_state: PipelineState) -> Tuple[List[Article], List[Article], List[ArticleState]]:
        """
        Compares current Zendesk articles against previous sync state.
        Returns:
            added_articles: Articles to be added
            updated_articles: Articles that have changed and need updating
            deleted_states: ArticleState records for articles that were deleted from Zendesk
        """
        prev_articles = previous_state.articles
        
        added = []
        updated = []
        deleted = []
        
        current_ids = {str(a.id) for a in current_articles}
        
        for article in current_articles:
            art_id_str = str(article.id)
            if art_id_str not in prev_articles:
                added.append(article)
            else:
                prev_art_state = prev_articles[art_id_str]
                if prev_art_state.hash_val != article.hash_val:
                    # Carry forward Gemini metadata to replace or update
                    article.gemini_file_name = prev_art_state.gemini_file_name
                    article.gemini_uri = prev_art_state.gemini_uri
                    updated.append(article)
                else:
                    # Article is unchanged, keep existing Gemini resource info
                    article.gemini_file_name = prev_art_state.gemini_file_name
                    article.gemini_uri = prev_art_state.gemini_uri
        
        for prev_id_str, prev_art_state in prev_articles.items():
            if prev_id_str not in current_ids:
                deleted.append(prev_art_state)
                
        return added, updated, deleted
