from google import genai
from google.genai import types
from google.genai.errors import APIError
from src.core.config import GeminiConfig
from src.core.models import Article
from src.utils.logger import setup_logger

logger = setup_logger("gemini_loader")

class GeminiLoader:
    def __init__(self, config: GeminiConfig):
        self.config = config
        api_key = config.api_key if config.api_key else None
        self.client = genai.Client(api_key=api_key)

    def upload_article(self, article: Article) -> bool:
        """
        Uploads the article's markdown file to the Gemini File API.
        If the article has a previous gemini_file_name, it attempts to delete it first.
        """
        if not article.file_path:
            logger.error(f"Article {article.id} has no associated local file path. Cannot upload.")
            return False

        if article.gemini_file_name:
            self.delete_gemini_file(article.gemini_file_name)

        logger.info(f"Uploading file for article {article.id} ({article.file_path}) to Gemini File API...")
        try:
            display_name = f"optibot_article_{article.id}_{article.locale}"
            
            gemini_file = self.client.files.upload(
                file=article.file_path,
                config=types.UploadFileConfig(display_name=display_name)
            )
            
            article.gemini_file_name = gemini_file.name
            article.gemini_uri = gemini_file.uri
            logger.info(f"Successfully uploaded article {article.id}. Gemini Name: {gemini_file.name}, URI: {gemini_file.uri}")
            return True
        except APIError as e:
            logger.error(f"Gemini API Error uploading article {article.id}: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error uploading article {article.id}: {e}")
            return False

    def delete_gemini_file(self, file_name: str) -> bool:
        """
        Attempts to delete a file from Gemini File API.
        Returns True if successful (or if the file was already deleted/expired), False otherwise.
        """
        if not file_name:
            return True
            
        logger.info(f"Deleting file {file_name} from Gemini File API...")
        try:
            self.client.files.delete(name=file_name)
            logger.info(f"Successfully deleted {file_name} from Gemini.")
            return True
        except APIError as e:
            if "404" in str(e) or "not found" in str(e).lower():
                logger.warning(f"File {file_name} not found on Gemini (likely expired after 48 hours or already deleted).")
                return True
            logger.error(f"Gemini API Error deleting file {file_name}: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error deleting file {file_name}: {e}")
            return False
