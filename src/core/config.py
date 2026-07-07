import os
from dataclasses import dataclass
from pathlib import Path
from typing import List
from dotenv import load_dotenv

# Load env variables from .env if it exists
load_dotenv()

@dataclass
class ZendeskConfig:
    base_url: str
    locales: List[str]
    timeout: int = 10
    max_retries: int = 3

@dataclass
class GeminiConfig:
    api_key: str
    store_name: str = "optibot-knowledge-base"

@dataclass
class PipelineConfig:
    data_dir: Path
    articles_dir: Path
    state_file: Path

@dataclass
class AppConfig:
    zendesk: ZendeskConfig
    gemini: GeminiConfig
    pipeline: PipelineConfig

def load_config() -> AppConfig:
    """Loads configuration from environment variables and validates key requirements."""
    # Zendesk Config (Public scraping)
    base_url = os.environ.get("SUPPORT_BASE_URL", "https://support.optisigns.com").rstrip("/")
    locales_raw = os.environ.get("SUPPORT_LOCALES", "en-us")
    locales = [lang.strip() for lang in locales_raw.split(",") if lang.strip()]
    
    try:
        timeout = int(os.environ.get("SUPPORT_TIMEOUT", "10"))
        max_retries = int(os.environ.get("SUPPORT_MAX_RETRIES", "3"))
    except ValueError as e:
        raise ValueError(f"Invalid integer for scraper timeout/retries: {e}")

    # Gemini Config
    api_key = os.environ.get("API_KEY") or os.environ.get("GEMINI_API_KEY", "")
    # Check for empty API key or placeholder
    if not api_key or api_key.strip() == "your_gemini_api_key_here":
        raise ValueError(
            "GEMINI_API_KEY is not configured or is set to the default placeholder. "
            "Please configure a valid API key in your .env file."
        )
    # Pipeline Config (Using Path objects)
    data_dir = Path(os.environ.get("SYNC_DATA_DIR", "data"))
    articles_dir = Path(os.environ.get("SYNC_ARTICLES_DIR", "data/articles"))
    state_file = Path(os.environ.get("SYNC_STATE_FILE", "data/state.json"))

    store_name = os.environ.get("GEMINI_STORE_NAME", "optibot-knowledge-base")

    return AppConfig(
        zendesk=ZendeskConfig(
            base_url=base_url,
            locales=locales,
            timeout=timeout,
            max_retries=max_retries
        ),
        gemini=GeminiConfig(
            api_key=api_key,
            store_name=store_name
        ),
        pipeline=PipelineConfig(
            data_dir=data_dir,
            articles_dir=articles_dir,
            state_file=state_file
        )
    )
