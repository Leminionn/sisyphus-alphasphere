import re
from datetime import datetime
from typing import List
import requests
from urllib.parse import urlparse, urlunparse
from src.core.config import ZendeskConfig
from src.core.models import Article
from src.utils.logger import setup_logger

logger = setup_logger("zendesk_extractor")

class ZendeskExtractor:
    def __init__(self, config: ZendeskConfig):
        self.config = config
        self.session = requests.Session()
        # No authentication is required for public Help Center articles

    def _rewrite_url_domain(self, url: str) -> str:
        """
        Rewrites the domain of the next page URL to match the configured base_url.
        This handles cases where Zendesk API pagination returns links pointing to
        their default subdomain (which might be redirected or block unauthenticated requests).
        """
        if not url:
            return url
        parsed_url = urlparse(url)
        parsed_base = urlparse(self.config.base_url)
        rewritten = parsed_url._replace(scheme=parsed_base.scheme, netloc=parsed_base.netloc)
        return urlunparse(rewritten)

    def fetch_articles(self) -> List[Article]:
        """
        Fetches all published articles from the public Zendesk Help Center.
        """
        articles: List[Article] = []
        locales = self.config.locales if self.config.locales else [None]
        
        for locale in locales:
            if locale:
                url = f"{self.config.base_url}/api/v2/help_center/{locale.lower()}/articles.json"
                logger.info(f"Fetching Zendesk articles for locale '{locale}' from {url}...")
            else:
                url = f"{self.config.base_url}/api/v2/help_center/articles.json"
                logger.info(f"Fetching all Zendesk articles from {url}...")
                
            params = {"per_page": 100}
            
            while url:
                try:
                    logger.info(f"Requesting: {url}")
                    response = self.session.get(url, params=params if "?" not in url else None)
                    response.raise_for_status()
                    data = response.json()
                    
                    batch = data.get("articles", [])
                    logger.info(f"Retrieved {len(batch)} articles in this page.")
                    
                    for item in batch:
                        # Exclude draft articles
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
                        
                        html_url = item.get("html_url") or ""
                        slug = ""
                        if html_url:
                            parts = html_url.rstrip("/").split("/articles/")
                            if len(parts) > 1:
                                slug = parts[1]
                        if not slug:
                            slug = re.sub(r'[^a-z0-9\s-]', '', item["title"].lower())
                            slug = re.sub(r'[\s-]+', '-', slug).strip('-')

                        articles.append(
                            Article(
                                id=item["id"],
                                title=item["title"],
                                body_html=item.get("body") or "",
                                locale=item.get("locale", "en-us"),
                                html_url=html_url,
                                slug=slug,
                                updated_at=updated_at_dt
                            )
                        )
                        
                    next_page = data.get("next_page")
                    if next_page:
                        url = self._rewrite_url_domain(next_page)
                    else:
                        url = None
                    params = {}
                    
                except requests.exceptions.RequestException as e:
                    logger.error(f"Error fetching articles from Zendesk API: {e}")
                    raise e
                    
        unique_articles = {}
        for a in articles:
            unique_articles[a.id] = a
            
        logger.info(f"Total published articles fetched: {len(unique_articles)}")
        return list(unique_articles.values())
