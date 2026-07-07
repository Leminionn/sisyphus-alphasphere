import sys
import logging
from src.core.config import load_config
from src.core.pipeline import SyncPipeline
from src.utils.logger import setup_logger

logger = setup_logger()

def main():
    try:
        # Load and validate configuration
        config = load_config()
        pipeline = SyncPipeline(config)
        pipeline.run()
    except ValueError as e:
        logger.error(f"Configuration validation failed: {e}")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"Unhandled exception in pipeline execution: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
