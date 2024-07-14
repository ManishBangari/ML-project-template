import sys
from src.dsproject.logger import logging
from src.dsproject.exception import CustomException
from src.dsproject.components.data_ingestion  import DataIngestion

if __name__=="__main__":
    logging.info("Execution has started.")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
