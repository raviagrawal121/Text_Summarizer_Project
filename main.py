from textsummarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from textsummarizer.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from textsummarizer.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
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


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} Completed <<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} Completed <<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e