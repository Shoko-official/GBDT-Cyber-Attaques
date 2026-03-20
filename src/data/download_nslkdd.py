import os
import requests

def download_file(url, target_path):
    print(f"Downloading {url} to {target_path}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(target_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Done.")

def main():
    raw_dir = "data/raw"
    os.makedirs(raw_dir, exist_ok=True)
    
    # URL for NSL-KDD on GitHub (reliable mirror)
    base_url = "https://raw.githubusercontent.com/defcom17/NSL-KDD/master/"
    files = ["KDDTrain+.txt", "KDDTest+.txt"]
    
    for filename in files:
        target = os.path.join(raw_dir, filename)
        if not os.path.exists(target):
            url = base_url + filename
            download_file(url, target)
        else:
            print(f"{filename} already exists.")

if __name__ == "__main__":
    main()
