import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder

# Attack mapping for multi-class classification
ATTACK_MAPPING = {
    'apache2': 'dos', 'back': 'dos', 'land': 'dos', 'neptune': 'dos', 'mailbomb': 'dos',
    'pod': 'dos', 'processtable': 'dos', 'smurf': 'dos', 'teardrop': 'dos', 'udpstorm': 'dos', 'worm': 'dos',
    'ipsweep': 'probe', 'mscan': 'probe', 'nmap': 'probe', 'portsweep': 'probe', 'saint': 'probe', 'satan': 'probe',
    'ftp_write': 'r2l', 'guess_passwd': 'r2l', 'httptunnel': 'r2l', 'imap': 'r2l', 'multihop': 'r2l', 'named': 'r2l',
    'phf': 'r2l', 'sendmail': 'r2l', 'snmpgetattack': 'r2l', 'snmpguess': 'r2l', 'spy': 'r2l', 'warezclient': 'r2l',
    'warezmaster': 'r2l', 'xlock': 'r2l', 'xsnoop': 'r2l',
    'buffer_overflow': 'u2r', 'loadmodule': 'u2r', 'perl': 'u2r', 'ps': 'u2r', 'rootkit': 'u2r', 'sqlattack': 'u2r', 'xterm': 'u2r',
    'normal': 'normal'
}

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
