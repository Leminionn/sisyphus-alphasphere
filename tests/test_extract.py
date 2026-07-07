from unittest.mock import MagicMock
import pytest
import requests
from src.core.config import ZendeskConfig
from src.extract.zendesk import ZendeskExtractor

def test_fetch_articles_success(monkeypatch):
    # Mock config
    config = ZendeskConfig(
        base_url="https://test.zendesk.com",
        locales=["en-us"],
        timeout=5,
        max_retries=2
    )
    
    # Mock requests response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "articles": [
            {
                "id": 1,
                "title": "Test Article 1",
                "body": "<p>Content 1</p>",
                "draft": False,
                "updated_at": "2026-07-07T12:00:00Z",
                "html_url": "https://test.zendesk.com/hc/en-us/articles/1-test-article-1",
                "locale": "en-us"
            }
        ],
        "next_page": None
    }
    
    # Mock Session.get
    mock_get = MagicMock(return_value=mock_response)
    monkeypatch.setattr(requests.Session, "get", mock_get)
    
    extractor = ZendeskExtractor(config)
    articles = extractor.fetch_articles()
    
    assert len(articles) == 1
    assert articles[0].id == 1
    assert articles[0].title == "Test Article 1"
    assert articles[0].slug == "1-test-article-1"
    assert articles[0].body_html == "<p>Content 1</p>"
    
    # Verify timeout parameter was passed to session.get
    mock_get.assert_called_once_with(
        "https://test.zendesk.com/api/v2/help_center/en-us/articles.json",
        params={"per_page": 100},
        timeout=5
    )

def test_fetch_articles_raises_extraction_error(monkeypatch):
    config = ZendeskConfig(
        base_url="https://test.zendesk.com",
        locales=["en-us"],
        timeout=5,
        max_retries=1
    )
    
    # Mock Session.get to raise RequestException
    mock_get = MagicMock(side_effect=requests.exceptions.RequestException("Network down"))
    monkeypatch.setattr(requests.Session, "get", mock_get)
    
    extractor = ZendeskExtractor(config)
    
    with pytest.raises(RuntimeError) as exc_info:
        extractor.fetch_articles()
        
    assert "Zendesk API request failed" in str(exc_info.value)
