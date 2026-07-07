from datetime import datetime
from src.core.models import Article
from src.transform.markdown import MarkdownTransformer

def test_transform_basic():
    transformer = MarkdownTransformer()
    article = Article(
        id=123,
        title="My Article Title",
        body_html="<h1>Heading 1</h1><p>This is a paragraph.</p>",
        locale="en-us",
        html_url="https://support.optisigns.com/hc/en-us/articles/123",
        updated_at=datetime(2026, 7, 7, 12, 0, 0)
    )
    
    markdown = transformer.transform(article)
    
    assert "# My Article Title" in markdown
    assert "**Article ID:** 123" in markdown
    assert "**Locale:** en-us" in markdown
    assert "**Article URL:** https://support.optisigns.com/hc/en-us/articles/123" in markdown
    assert "**Last Updated:** 2026-07-07T12:00:00" in markdown
    assert "# Heading 1" in markdown
    assert "This is a paragraph." in markdown

def test_transform_image_removal():
    transformer = MarkdownTransformer()
    article = Article(
        id=123,
        title="Article with Images",
        body_html="""
        <p>Here is an image: <img src='logo.png' alt='Logo'> and text.</p>
        <p>Wrapped image: <a href="logo.png"><img src="logo.png"></a></p>
        <p>Normal link: <a href="https://google.com">Google</a></p>
        <p>Direct image link: <a href="logo.png">Image Link</a></p>
        """,
        locale="en-us",
        updated_at=None
    )
    
    markdown = transformer.transform(article)
    
    # Image file references should be fully stripped
    assert "logo.png" not in markdown
    assert "Logo" not in markdown
    assert "Image Link" not in markdown
    
    # Normal text and normal links must be preserved
    assert "Here is an image:" in markdown
    assert "and text." in markdown
    assert "[Google](https://google.com)" in markdown

def test_transform_html_toc_removal():
    transformer = MarkdownTransformer()
    article = Article(
        id=123,
        title="Article with HTML TOC",
        body_html="""
        <div class="toc">
            <h3>Table of Contents</h3>
            <ul>
                <li><a href="#sec1">Section 1</a></li>
                <li><a href="#sec2">Section 2</a></li>
            </ul>
        </div>
        <h2>Real Header</h2>
        <p>This is the real content.</p>
        """,
        locale="en-us"
    )
    
    markdown = transformer.transform(article)
    
    assert "Table of Contents" not in markdown
    assert "Section 1" not in markdown
    assert "Real Header" in markdown
    assert "This is the real content." in markdown

def test_transform_markdown_toc_removal():
    transformer = MarkdownTransformer()
    article = Article(
        id=123,
        title="Article with Markdown TOC",
        body_html="""
        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#sec1">Section 1</a></li>
            <li><a href="#sec2">Section 2</a></li>
        </ul>
        <h2>Actual Content</h2>
        <p>Hello world.</p>
        """,
        locale="en-us"
    )
    
    markdown = transformer.transform(article)
    
    assert "Table of Contents" not in markdown
    assert "Section 1" not in markdown
    assert "Actual Content" in markdown
    assert "Hello world." in markdown
