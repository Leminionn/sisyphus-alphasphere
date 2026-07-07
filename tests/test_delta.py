from pathlib import Path
from src.core.models import Article, ArticleState, PipelineState
from src.delta.detector import DeltaDetector

def test_detect_deltas_added():
    detector = DeltaDetector(state_file_path=Path("dummy_state.json")) # We don't read from disk here
    
    previous_state = PipelineState(
        last_sync="2026-07-07T00:00:00",
        articles={
            "1": ArticleState(id=1, slug="art-1", hash_val="hash1", updated_at="2026-07-07T00:00:00", gemini_file_name="gemini1", gemini_uri="uri1")
        }
    )
    
    current_articles = [
        Article(id=1, title="Art 1", body_html="", hash_val="hash1"),
        Article(id=2, title="Art 2", body_html="", hash_val="hash2")
    ]
    
    added, updated, deleted = detector.detect_deltas(current_articles, previous_state)
    
    assert len(added) == 1
    assert added[0].id == 2
    assert len(updated) == 0
    assert len(deleted) == 0

def test_detect_deltas_updated():
    detector = DeltaDetector(state_file_path=Path("dummy_state.json"))
    
    previous_state = PipelineState(
        last_sync="2026-07-07T00:00:00",
        articles={
            "1": ArticleState(id=1, slug="art-1", hash_val="hash1", updated_at="2026-07-07T00:00:00", gemini_file_name="gemini1", gemini_uri="uri1")
        }
    )
    
    current_articles = [
        Article(id=1, title="Art 1", body_html="", hash_val="hash1_new")
    ]
    
    added, updated, deleted = detector.detect_deltas(current_articles, previous_state)
    
    assert len(added) == 0
    assert len(updated) == 1
    assert updated[0].id == 1
    assert updated[0].gemini_file_name == "gemini1"
    assert len(deleted) == 0

def test_detect_deltas_deleted():
    detector = DeltaDetector(state_file_path=Path("dummy_state.json"))
    
    previous_state = PipelineState(
        last_sync="2026-07-07T00:00:00",
        articles={
            "1": ArticleState(id=1, slug="art-1", hash_val="hash1", updated_at="2026-07-07T00:00:00", gemini_file_name="gemini1", gemini_uri="uri1"),
            "2": ArticleState(id=2, slug="art-2", hash_val="hash2", updated_at="2026-07-07T00:00:00", gemini_file_name="gemini2", gemini_uri="uri2")
        }
    )
    
    current_articles = [
        Article(id=1, title="Art 1", body_html="", hash_val="hash1")
    ]
    
    added, updated, deleted = detector.detect_deltas(current_articles, previous_state)
    
    assert len(added) == 0
    assert len(updated) == 0
    assert len(deleted) == 1
    assert deleted[0].id == 2
