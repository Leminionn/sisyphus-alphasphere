import os
from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv

# Load env variables from .env if it exists
load_dotenv()

@dataclass
class ZendeskConfig:
    base_url: str
    locales: List[str]

@dataclass
class GeminiConfig:
    api_key: str
    model: str

@dataclass
class PipelineConfig:
    data_dir: str
    articles_dir: str
    state_file: str

@dataclass
class AppConfig:
    zendesk: ZendeskConfig
    gemini: GeminiConfig
    pipeline: PipelineConfig

def load_config() -> AppConfig:
    # Zendesk Config (Public scraping)
    base_url = os.environ.get("SUPPORT_BASE_URL", "https://support.optisigns.com").rstrip("/")
    locales_raw = os.environ.get("SUPPORT_LOCALES", "en-us")
    locales = [lang.strip() for lang in locales_raw.split(",") if lang.strip()]

    # Gemini Config
    api_key = os.environ.get("API_KEY") or os.environ.get("GEMINI_API_KEY", "")
    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

    # Pipeline Config
    data_dir = os.environ.get("SYNC_DATA_DIR", "data")
    articles_dir = os.environ.get("SYNC_ARTICLES_DIR", "data/articles")
    state_file = os.environ.get("SYNC_STATE_FILE", "data/state.json")

    return AppConfig(
        zendesk=ZendeskConfig(base_url=base_url, locales=locales),
        gemini=GeminiConfig(api_key=api_key, model=model),
        pipeline=PipelineConfig(data_dir=data_dir, articles_dir=articles_dir, state_file=state_file)
    )
