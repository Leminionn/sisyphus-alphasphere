import os
import yaml
from dataclasses import dataclass
from typing import List

@dataclass
class ZendeskConfig:
    subdomain: str
    email: str
    token: str
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

def load_config(config_path: str = "config.yaml") -> AppConfig:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
        
    with open(config_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    # Extract sections with safe defaults
    zd_data = data.get("zendesk", {})
    gemini_data = data.get("gemini", {})
    pipe_data = data.get("pipeline", {})

    # Apply environment variable overrides for sensitive values
    subdomain = os.environ.get("ZENDESK_SUBDOMAIN", zd_data.get("subdomain", ""))
    email = os.environ.get("ZENDESK_EMAIL", zd_data.get("email", ""))
    token = os.environ.get("ZENDESK_TOKEN", zd_data.get("token", ""))
    locales = zd_data.get("locales", ["en-us"])

    api_key = os.environ.get("GEMINI_API_KEY", gemini_data.get("api_key", ""))
    model = os.environ.get("GEMINI_MODEL", gemini_data.get("model", "gemini-2.5-flash"))

    data_dir = pipe_data.get("data_dir", "data")
    articles_dir = pipe_data.get("articles_dir", "data/articles")
    state_file = pipe_data.get("state_file", "data/state.json")

    return AppConfig(
        zendesk=ZendeskConfig(subdomain=subdomain, email=email, token=token, locales=locales),
        gemini=GeminiConfig(api_key=api_key, model=model),
        pipeline=PipelineConfig(data_dir=data_dir, articles_dir=articles_dir, state_file=state_file)
    )
