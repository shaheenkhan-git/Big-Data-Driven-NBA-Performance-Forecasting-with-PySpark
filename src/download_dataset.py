import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset():
    api = KaggleApi()
    api.authenticate()
    
    dataset = 'blitzapurv/nba-players-data-1950-to-2021'
    download_path = os.path.join('datasets/raw') 
    
    os.makedirs(download_path, exist_ok=True)
    
    print(f"Downloading dataset: {dataset}...")
    api.dataset_download_files(dataset, path=download_path, unzip=True)
    
    print("Download completed successfully!")
    
    downloaded_files = os.listdir(download_path)
    print(f"Downloaded files: {downloaded_files}")

if __name__ == '__main__':
    download_kaggle_dataset()