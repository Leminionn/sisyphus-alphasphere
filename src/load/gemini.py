from google import genai
from google.genai import types
from google.genai.errors import APIError
import time
from src.core.config import GeminiConfig
from src.core.models import Article
from src.utils.logger import setup_logger

logger = setup_logger("gemini_loader")

class GeminiLoader:
    def __init__(self, config: GeminiConfig):
        self.config = config
        api_key = config.api_key if config.api_key else None
        self.client = genai.Client(api_key=api_key)
        self.store_name = None
        self._init_store()

    def _init_store(self) -> None:
        """
        Initializes the File Search Store. Checks if 'optibot-knowledge-base' 
        already exists, and creates it if not.
        """
        if not self.config.api_key or self.config.api_key == "your_gemini_api_key_here":
            logger.warning("GEMINI_API_KEY is not set or using placeholder. Skipping store initialization.")
            return

        try:
            logger.info("Initializing Gemini File Search Store...")
            stores = self.client.file_search_stores.list()
            target_store = None
            
            for store in stores:
                if store.display_name == "optibot-knowledge-base":
                    target_store = store
                    break

            if target_store:
                self.store_name = target_store.name
                logger.info(f"Reusing existing File Search Store: {self.store_name} ({target_store.display_name})")
            else:
                logger.info("No existing 'optibot-knowledge-base' store found. Creating one...")
                new_store = self.client.file_search_stores.create(
                    config=types.CreateFileSearchStoreConfig(
                        display_name="optibot-knowledge-base",
                        embedding_model="models/gemini-embedding-2"
                    )
                )
                self.store_name = new_store.name
                logger.info(f"Created new File Search Store: {self.store_name}")

        except APIError as e:
            logger.error(f"Gemini API Error during store initialization: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during store initialization: {e}")

    def upload_article(self, article: Article) -> bool:
        """
        Uploads the article's markdown file to the Gemini File Search Store.
        If the article has a previous gemini_file_name, it attempts to delete it first.
        """
        if not self.store_name:
            self._init_store()
            if not self.store_name:
                logger.error("File Search Store is not initialized. Cannot upload article.")
                return False

        if not article.file_path:
            logger.error(f"Article {article.id} has no associated local file path. Cannot upload.")
            return False

        if article.gemini_file_name:
            self.delete_gemini_document(article.gemini_file_name)

        logger.info(f"Uploading file for article {article.id} ({article.file_path}) to Gemini File Search Store...")
        try:
            word_count = len(article.body_markdown.split())
            estimated_chunks = max(1, -(-word_count // 375))  # Ceiling division (500 tokens ~ 375 words)
            
            config = types.UploadToFileSearchStoreConfig(
                display_name=article.slug,
                chunking_config=types.ChunkingConfig(
                    white_space_config=types.WhiteSpaceConfig(
                        max_tokens_per_chunk=500,
                        max_overlap_tokens=100
                    )
                )
            )

            operation = self.client.file_search_stores.upload_to_file_search_store(
                file_search_store_name=self.store_name,
                file=article.file_path,
                config=config
            )
            
            logger.info(f"Upload initiated. Waiting for document indexing to complete...")
            while not operation.done:
                time.sleep(2)
                operation = self.client.operations.get(name=operation.name)
                
            if operation.error:
                logger.error(f"Error during indexing of article {article.id}: {operation.error}")
                return False

            doc_name = operation.response.document_name
            article.gemini_file_name = doc_name
            article.gemini_uri = f"gemini://{doc_name}"
            
            logger.info(f"Successfully uploaded and indexed article {article.id}!")
            logger.info(f"Document Name: {doc_name}")
            logger.info(f"Stats: 1 file uploaded, approx {estimated_chunks} chunks embedded.")
            return True
        except APIError as e:
            logger.error(f"Gemini API Error uploading article {article.id}: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error uploading article {article.id}: {e}")
            return False

    def delete_gemini_document(self, doc_name: str) -> bool:
        """
        Attempts to delete a document from the File Search Store.
        """
        if not doc_name:
            return True
            
        logger.info(f"Deleting document {doc_name} from File Search Store...")
        try:
            self.client.file_search_stores.documents.delete(name=doc_name)
            logger.info(f"Successfully deleted document {doc_name} from Gemini.")
            return True
        except APIError as e:
            if "404" in str(e) or "not found" in str(e).lower():
                logger.warning(f"Document {doc_name} not found in Gemini (likely already deleted).")
                return True
            logger.error(f"Gemini API Error deleting document {doc_name}: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error deleting document {doc_name}: {e}")
            return False
