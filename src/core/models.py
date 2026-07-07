from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

@dataclass
class Article:
    id: int
    title: str
    body_html: str
    body_markdown: str = ""
    locale: str = "en-us"
    html_url: str = ""
    slug: str = ""
    updated_at: Optional[datetime] = None
    hash_val: str = ""
    file_path: Optional[Path] = None
    gemini_file_name: str = ""  # resource name in Gemini File Search Store
    gemini_uri: str = ""

@dataclass
class ArticleState:
    id: int
    slug: str
    hash_val: str
    updated_at: str  # ISO format string
    gemini_file_name: str
    gemini_uri: str
    locale: str = "en-us"

@dataclass
class PipelineState:
    last_sync: str  # ISO format string
    articles: Dict[str, ArticleState] = field(default_factory=dict)
