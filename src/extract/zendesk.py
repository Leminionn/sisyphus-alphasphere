from datetime import datetime
from typing import List
import requests
from src.core.config import ZendeskConfig
from src.core.models import Article
from src.utils.logger import setup_logger

logger = setup_logger("zendesk_extractor")

class ZendeskExtractor:
    def __init__(self, config: ZendeskConfig):
        self.config = config
        self.session = requests.Session()
        self.session.auth = (f"{config.email}/token", config.token)

    def fetch_articles(self) -> List[Article]:
        """
        Fetches all published articles from Zendesk for the configured locales.
        If no locales are configured, fetches all articles.
        """
        articles: List[Article] = []
        locales = self.config.locales if self.config.locales else [None]
        
        for locale in locales:
            if locale:
                url = f"https://{self.config.subdomain}.zendesk.com/api/v2/help_center/{locale.lower()}/articles.json"
                logger.info(f"Fetching Zendesk articles for locale '{locale}'...")
            else:
                url = f"https://{self.config.subdomain}.zendesk.com/api/v2/help_center/articles.json"
                logger.info("Fetching all Zendesk articles...")
                
            params = {"per_page": 100}
            
            while url:
                try:
                    response = self.session.get(url, params=params if "?" not in url else None)
                    response.raise_for_status()
                    data = response.json()
                    
                    batch = data.get("articles", [])
                    logger.info(f"Retrieved {len(batch)} articles in this page.")
                    
                    for item in batch:
                        if item.get("draft") is True:
                            continue
                            
                        updated_at_str = item.get("updated_at")
                        updated_at_dt = None
                        if updated_at_str:
                            try:
                                clean_dt_str = updated_at_str.replace("Z", "+00:00")
                                updated_at_dt = datetime.fromisoformat(clean_dt_str)
                            except ValueError:
                                logger.warning(f"Could not parse updated_at string: {updated_at_str}")
                        
                        articles.append(
                            Article(
                                id=item["id"],
                                title=item["title"],
                                body_html=item.get("body") or "",
                                locale=item.get("locale", "en-us"),
                                updated_at=updated_at_dt
                            )
                        )
                        
                    url = data.get("next_page")
                    params = {}
                    
                except requests.exceptions.RequestException as e:
                    logger.error(f"Error fetching articles from Zendesk API: {e}")
                    raise e
                    
        unique_articles = {}
        for a in articles:
            unique_articles[a.id] = a
            
        logger.info(f"Total published articles fetched: {len(unique_articles)}")
        return list(unique_articles.values())
