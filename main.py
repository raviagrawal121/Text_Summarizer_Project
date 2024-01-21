from textsummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} Completed <<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

