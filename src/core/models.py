from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional

@dataclass
class Article:
    id: int
    title: str
    body_html: str
    body_markdown: str = ""
    locale: str = "en-us"
    updated_at: Optional[datetime] = None
    hash_val: str = ""
    file_path: str = ""
    gemini_file_name: str = ""
    gemini_uri: str = ""

@dataclass
class ArticleState:
    id: int
    hash_val: str
    updated_at: str  # ISO format string
    gemini_file_name: str
    gemini_uri: str

@dataclass
class PipelineState:
    last_sync: str  # ISO format string
    articles: Dict[str, ArticleState] = field(default_factory=dict)
