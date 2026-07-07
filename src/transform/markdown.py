import markdownify
from src.core.models import Article
from src.utils.logger import setup_logger

logger = setup_logger("markdown_transformer")

class MarkdownTransformer:
    def __init__(self):
        pass

    def transform(self, article: Article) -> str:
        """
        Converts the HTML body of an article to clean markdown and prepends metadata headers.
        """
        if not article.body_html:
            markdown_content = ""
        else:
            markdown_content = markdownify.markdownify(
                article.body_html,
                heading_style="ATX",
                strip=['script', 'style']
            ).strip()
            
        while "\n\n\n" in markdown_content:
            markdown_content = markdown_content.replace("\n\n\n", "\n\n")
            
        metadata_header = (
            f"# {article.title}\n\n"
            f"**Article ID:** {article.id}\n"
            f"**Locale:** {article.locale}\n"
            f"**Last Updated:** {article.updated_at.isoformat() if article.updated_at else 'Unknown'}\n"
            f"---\n\n"
        )
        
        full_markdown = metadata_header + markdown_content
        article.body_markdown = full_markdown
        return full_markdown
