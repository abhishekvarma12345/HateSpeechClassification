import os
import sys
import pandas as pd
from hate.logger import logging
from hate.exception import CustomException

from hate.entity.config_entity import DataValidationConfig
from hate.entity.artifact_entity import (
    DataIngestionArtifacts,
    DataValidationArtifacts
)

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifacts, data_validation_config: DataValidationConfig):
        self.data_validation_config = data_validation_config
        self.imbalance_data_file_path = data_ingestion_artifact.imbalance_data_file_path
        self.raw_data_file_path = data_ingestion_artifact.raw_data_file_path
    
    def perform_schema_validation(self, file_path: str, name: str) -> bool:
        logging.info("Entered the perform_schema_validation method of DataValidation class.")
        try:
            imbalanced_df = pd.read_csv(file_path)
            imb_columns = imbalanced_df.columns
            
            is_valid = True
            if len(imb_columns) == self.data_validation_config.IMBALANCE_DATA_COLUMNS:
                logging.info(f"{name} data no of columns check passed.")
                if tuple(imb_columns) == tuple(self.data_validation_config.IMBALANCE_DATA_COLUMN_NAMES):
                    logging.info(f"{name} data column names check passed.")
                    is_valid = True
                else:
                    logging.info(f"{name} data column names check failed.")
                    is_valid = False
            else:
                logging.info(f"{name} data no of columns check failed.")
                is_valid = False
                
            return is_valid
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def initiate_data_validation(self) -> DataValidationArtifacts:
        logging.info("Entered the initiate_data_validation method of DataValidation class")
        try:
            is_valid_imb_data = self.perform_schema_validation(self.imbalance_data_file_path, "imbalanced")
            id_valid_raw_data = self.perform_schema_validation(self.imbalance_data_file_path, "raw")
            
            data_validation_artifacts = DataValidationArtifacts(
                is_valid_data=(is_valid_imb_data and id_valid_raw_data)
            )
            
            logging.info("Exited the initiate_data_validation method of DataValidation class")

            logging.info(f"Data Validation artifact: {data_validation_artifacts}")

            return data_validation_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e