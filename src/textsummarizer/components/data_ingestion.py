import os
import urllib.request as request
import zipfile
from textsummarizer.logging import logger
from textsummarizer.utils.common import get_size
from textsummarizer.entity import DataIngetionconfig
from pathlib import Path



class DataIngestion:
    def __init__(self,config:DataIngetionconfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(url = self.config.source_url,filename = self.config.local_data_file)
            logger.info(f"{filename} downloaded! with following headers: {headers}")
        else:
            logger.info(f"file already exists of size {get_size(Path(self.config.local_data_file))}")


    
    def unzip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"unzip successfully")