import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml :Path)->ConfigBox:
    """read yaml file and return ConfigBox

    Args:
        path_to_yaml (Path): path like input

    Raises:
        BoxValueError: if yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: configuration box
    """
    try:
        with open(path_to_yaml) as f:
            config = yaml.safe_load(f)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(config)
    except BoxValueError:
        logger.error(f"yaml file:{path_to_yaml} is not a valid yaml file")
        raise BoxValueError
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories : list,verbose= True):
    """create directories

    Args:
        path_to_directories (list): list of directories to create
        verbose (bool, optional): ignore if multiple directories to be build . Defaults to True.
    """
    for directory in path_to_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            if verbose:
                logger.info(f"directory:{directory} created successfully")
        else:
            if verbose:
                logger.info(f"directory:{directory} already exists")

@ensure_annotations
def get_size(path:Path)-> str:
    """get size of of files

    Args:
        path (Path): path like input

    Returns:
        str: size of files
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

