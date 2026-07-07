import json
import os
from typing import Dict, List, Tuple
from src.core.models import Article, ArticleState, PipelineState
from src.utils.logger import setup_logger

logger = setup_logger("delta_detector")

class DeltaDetector:
    def __init__(self, state_file_path: str):
        self.state_file_path = state_file_path

    def load_state(self) -> PipelineState:
        if not os.path.exists(self.state_file_path):
            logger.info("No previous state file found. Starting fresh.")
            return PipelineState(last_sync="", articles={})
        
        try:
            with open(self.state_file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            articles_data = data.get("articles", {})
            articles_state = {}
            for k, v in articles_data.items():
                articles_state[k] = ArticleState(
                    id=v["id"],
                    hash_val=v["hash_val"],
                    updated_at=v["updated_at"],
                    gemini_file_name=v.get("gemini_file_name", ""),
                    gemini_uri=v.get("gemini_uri", "")
                )
            
            return PipelineState(
                last_sync=data.get("last_sync", ""),
                articles=articles_state
            )
        except Exception as e:
            logger.error(f"Error loading state file: {e}. Starting fresh.")
            return PipelineState(last_sync="", articles={})

    def save_state(self, state: PipelineState) -> None:
        dir_name = os.path.dirname(self.state_file_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
            
        data = {
            "last_sync": state.last_sync,
            "articles": {
                k: {
                    "id": v.id,
                    "hash_val": v.hash_val,
                    "updated_at": v.updated_at,
                    "gemini_file_name": v.gemini_file_name,
                    "gemini_uri": v.gemini_uri
                } for k, v in state.articles.items()
            }
        }
        
        try:
            with open(self.state_file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Sync state saved to {self.state_file_path}.")
        except Exception as e:
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
                prev_state = prev_articles[art_id_str]
                if prev_state.hash_val != article.hash_val:
                    article.gemini_file_name = prev_state.gemini_file_name
                    article.gemini_uri = prev_state.gemini_uri
                    updated.append(article)
                else:
                    article.gemini_file_name = prev_state.gemini_file_name
                    article.gemini_uri = prev_state.gemini_uri
        
        for prev_id_str, prev_state in prev_articles.items():
            if prev_id_str not in current_ids:
                deleted.append(prev_state)
                
        return added, updated, deleted
