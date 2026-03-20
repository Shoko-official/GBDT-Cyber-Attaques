import sys
import os
from src.utils.logger import logger

# Add src to path
sys.path.append(os.path.join(os.getcwd()))

from src.data.preprocessing import main as run_preprocessing
from src.features.build_features import main as run_features

def main():
    """
    Main entry point to run the entire data pipeline.
    """
    logger.info("=== Starting NSL-KDD Data Pipeline ===")
    
    try:
        # Step 1: Preprocessing
        logger.info("Step 1/2: Running Preprocessing...")
        run_preprocessing()
        
        # Step 2: Feature Engineering
        logger.info("Step 2/2: Running Feature Engineering...")
        run_features()
        
        logger.info("=== Pipeline Completed Successfully ===")
        
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
