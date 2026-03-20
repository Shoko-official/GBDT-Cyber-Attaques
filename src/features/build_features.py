import pandas as pd
import numpy as np
import os
import sys
from sklearn.preprocessing import LabelEncoder

# Add src to path
sys.path.append(os.path.join(os.getcwd()))

from src.config import ATTACK_MAPPING

def encode_data(df):
    # 1. Target Encoding (Binary)
    df['target_binary'] = df['attack'].apply(lambda x: 0 if x == 'normal' else 1)
    
    # 2. Target Encoding (Multi-class)
    df['target_multi'] = df['attack'].map(lambda x: ATTACK_MAPPING.get(x, 'other'))
    
    # 3. Categorical Encoding (One-Hot)
    cat_cols = ['protocol_type', 'service', 'flag']
    df_encoded = pd.get_dummies(df, columns=cat_cols)
    
    return df_encoded

def main():
    processed_dir = "data/processed"
    
    train_df = pd.read_csv(os.path.join(processed_dir, "train_basic.csv"))
    test_df = pd.read_csv(os.path.join(processed_dir, "test_basic.csv"))
    
    print("Encoding features...")
    train_encoded = encode_data(train_df)
    test_encoded = encode_data(test_df)
    
    # Ensure train and test have the same columns after One-Hot encoding
    missing_cols = set(train_encoded.columns) - set(test_encoded.columns)
    for c in missing_cols:
        test_encoded[c] = 0
    
    missing_cols = set(test_encoded.columns) - set(train_encoded.columns)
    for c in missing_cols:
        train_encoded[c] = 0
        
    # Reorder columns to match
    test_encoded = test_encoded[train_encoded.columns]
    
    train_encoded.to_csv(os.path.join(processed_dir, "train_processed.csv"), index=False)
    test_encoded.to_csv(os.path.join(processed_dir, "test_processed.csv"), index=False)
    print("Feature encoding finished. Saved to train_processed.csv and test_processed.csv")

if __name__ == "__main__":
    main()
