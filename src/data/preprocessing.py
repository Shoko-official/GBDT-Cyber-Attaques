import pandas as pd
import os

COLUMNS = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land",
    "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
    "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
    "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
    "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
    "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
    "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
    "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "attack", "level"
]

def load_data(file_path):
    print(f"Loading {file_path}...")
    df = pd.read_csv(file_path, names=COLUMNS, header=None)
    return df

def preprocess_basic(df):
    # Strip whitespace from string columns
    str_cols = df.select_dtypes(include=['object']).columns
    for col in str_cols:
        df[col] = df[col].str.strip()
    
    # Check for missing values
    missing = df.isnull().sum().sum()
    print(f"Found {missing} missing values.")
    
    # In NSL-KDD, the 'level' column is often ignored for basic classification
    # but we'll keep it for EDA.
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
