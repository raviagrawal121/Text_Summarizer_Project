from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.data_validation import DataValidation
from textsummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            data_validation.validate_all_files()
        except Exception as e:
            logger.error(e)