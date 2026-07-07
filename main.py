import argparse
import sys
from src.core.config import load_config
from src.core.pipeline import SyncPipeline
from src.utils.logger import setup_logger

logger = setup_logger("main")

def main():
    parser = argparse.ArgumentParser(description="OptiBot ETL Help Center Data Sync Pipeline")
    parser.add_argument(
        "--config", 
        type=str, 
        default="config.yaml", 
        help="Path to configuration file (default: config.yaml)"
    )
    args = parser.parse_args()
    
    try:
        config = load_config(args.config)
        pipeline = SyncPipeline(config)
        pipeline.run()
    except Exception as e:
        logger.critical(f"Unhandled exception in pipeline execution: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
