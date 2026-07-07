import re
import logging
import markdownify
from src.core.models import Article

logger = logging.getLogger("markdown_transformer")

class MarkdownTransformer:
    def __init__(self):
        # Match common TOC headers in markdown (case-insensitive)
        self.toc_header_regex = re.compile(
            r'^(?:#+\s+)?(?:table\s+of\s+contents|in\s+this\s+article|on\s+this\s+page|toc)\b.*$', 
            re.IGNORECASE
        )
        # Match list items containing internal anchors: e.g., * [Title](#anchor)
        self.toc_item_regex = re.compile(r'^\s*(?:[\*\-\+]|\d+\.)\s+\[.*?\]\(#.*?\)\s*$')

    def _remove_html_toc_containers(self, html: str) -> str:
        """Strips HTML container elements commonly used for Table of Contents."""
        if not html:
            return html
        # Remove elements with class or ID containing "toc" or "table-of-contents"
        cleaned = re.sub(
            r'<(div|nav|ul|ol)[^>]*?(?:class|id)=["\'][^"\']*(?:toc|table-of-contents)[^"\']*["\'][^>]*?>.*?</\1>',
            '',
            html,
            flags=re.IGNORECASE | re.DOTALL
        )
        return cleaned

    def _remove_markdown_toc(self, markdown_text: str) -> str:
        """
        Parses the markdown lines to detect and strip TOC lists.
        Strips the TOC header and the subsequent list of anchor links.
        """
        lines = markdown_text.splitlines()
        cleaned_lines = []
        skip_mode = False
        
        for line in lines:
            stripped = line.strip()
            
            # If in skip mode, continue skipping until we hit a non-empty, non-TOC-item line
            if skip_mode:
                if not stripped:
                    continue
                if self.toc_item_regex.match(line):
                    continue
                skip_mode = False
            
            # Check if this line is a TOC section header
            if self.toc_header_regex.match(stripped):
                skip_mode = True
                continue
                
            cleaned_lines.append(line)
            
        return "\n".join(cleaned_lines).strip()

    def transform(self, article: Article) -> str:
        """
        Converts the HTML body of an article to clean markdown and prepends metadata headers.
        Removes images, Table of Contents (TOC) lists, and redundant image links.
        """
        try:
            # 1. HTML pre-processing: Remove TOC tags
            html_body = self._remove_html_toc_containers(article.body_html)
            
            # 2. Markdownification (excluding images, scripts, styles)
            if not html_body:
                markdown_content = ""
            else:
                markdown_content = markdownify.markdownify(
                    html_body,
                    heading_style="ATX",
                    strip=['script', 'style', 'img']
                ).strip()
            
            # 3. Post-processing: Remove residual markdown images
            markdown_content = re.sub(r'!\[.*?\]\(.*?\)', '', markdown_content)
            
            # 4. Post-processing: Strip links pointing to image files (e.g. [Logo](url.png))
            markdown_content = re.sub(
                r'\[.*?\]\([^\)]*?\.(?:png|jpg|jpeg|gif|svg|webp)(?:\?[^\)]*?)?\)',
                '',
                markdown_content,
                flags=re.IGNORECASE
            )
            
            # 5. Post-processing: Strip empty link tags (e.g. [](url) or [  ](url))
            markdown_content = re.sub(r'\[\s*?\]\([^\)]*?\)', '', markdown_content)
            
            # 6. Post-processing: Strip Markdown TOC block
            markdown_content = self._remove_markdown_toc(markdown_content)
            
            # 7. Clean up multiple blank lines
            markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
            
            # 8. Prepend metadata header including original article URL
            metadata_header = (
                f"# {article.title}\n\n"
                f"**Article ID:** {article.id}\n"
                f"**Locale:** {article.locale}\n"
                f"**Article URL:** {article.html_url}\n"
                f"**Last Updated:** {article.updated_at.isoformat() if article.updated_at else 'Unknown'}\n"
                f"---\n\n"
            )
            
            full_markdown = metadata_header + markdown_content
            article.body_markdown = full_markdown
            return full_markdown
            
        except Exception as e:
            logger.error(f"Failed to transform article {article.id}: {e}")
            raise RuntimeError(f"HTML to Markdown conversion failed: {e}") from e
