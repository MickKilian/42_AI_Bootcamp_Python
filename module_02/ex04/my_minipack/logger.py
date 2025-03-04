# my_minipack/logger.py

import logging

def setup_logger():
    logger = logging.getLogger('my_minipack')
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger()

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)
