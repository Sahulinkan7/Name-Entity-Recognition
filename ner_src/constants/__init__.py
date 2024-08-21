import os 
from datetime import datetime

# project constants

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR :str = os.path.join("artifacts",TIMESTAMP)

LOGS_DIR="logs"
LOGS_FILE_NAME="ner.log"
MODELS_DIR="models"
BEST_MODEL_DIR="best_model"

BUCKET_NAME=""
GCP_DATA_FILE_NAME=""
CSV_DATA_FILE_NAME=""
GCP_MODEL_NAME=""

DATA_INGESTION_ARTIFACTS_DIR="DataIngestionArtifacts"