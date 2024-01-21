from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_transformation import DataTransformation
from textsummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            logger.error(e)