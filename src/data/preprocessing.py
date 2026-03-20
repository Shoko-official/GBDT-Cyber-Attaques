import pandas as pd
import os
import sys

# Add src to path if needed for local execution
sys.path.append(os.path.join(os.getcwd()))

from src.config import COLUMNS
from src.utils.logger import logger

def load_data(file_path):
    """
    Load NSL-KDD data from a text file and assign column names.
    
    Args:
        file_path (str): Path to the .txt file.
        
    Returns:
        pd.DataFrame: Loaded dataframe.
    """
    logger.info(f"Loading data from {file_path}...")
    df = pd.read_csv(file_path, names=COLUMNS, header=None)
    return df

def preprocess_basic(df):
    """
    Perform basic string cleaning and check for missing values.
    
    Args:
        df (pd.DataFrame): Dataframe to clean.
        
    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include=['object']).columns
    for col in str_cols:
        df[col] = df[col].str.strip()
    
    # Check for missing values
    missing = df.isnull().sum().sum()
    if missing > 0:
        logger.warning(f"Found {missing} missing values.")
    else:
        logger.info("No missing values found.")
    
    return df

def main():
    raw_dir = "data/archive"  # Updated to point where the user put the data
    processed_dir = "data/processed"
    os.makedirs(processed_dir, exist_ok=True)
    
    train_path = os.path.join(raw_dir, "KDDTrain+.txt")
    test_path = os.path.join(raw_dir, "KDDTest+.txt")
    
    if not os.path.exists(train_path):
        # Fallback to subdirectory if needed
        train_path = os.path.join(raw_dir, "nsl-kdd", "KDDTrain+.txt")
        test_path = os.path.join(raw_dir, "nsl-kdd", "KDDTest+.txt")
    
    train_df = load_data(train_path)
    test_df = load_data(test_path)
    
    train_df = preprocess_basic(train_df)
    test_df = preprocess_basic(test_df)
    
    # Save as CSV for easier inspection
    train_df.to_csv(os.path.join(processed_dir, "train_basic.csv"), index=False)
    test_df.to_csv(os.path.join(processed_dir, "test_basic.csv"), index=False)
    print("Basic preprocessing finished. Files saved to data/processed/")

if __name__ == "__main__":
    main()
