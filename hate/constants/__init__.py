import os
from datetime import datetime

# common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR: str = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME: str = "hate-speech-classify"
ZIP_FILE_NAME: str = "dataset.zip"
LABEL:str = "label"
TWEET:str = "tweet"

# Data Ingestion constants
DATA_INGESTION_ARTIFACTS_DIR: str = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR: str = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR: str = "raw_data.csv"





