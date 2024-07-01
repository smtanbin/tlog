import logging
import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

class ISOFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.utcfromtimestamp(record.created)
        return dt.isoformat() + 'Z'

def setup_logger(log_path):
    """
    Set up a logger with ISO 8601 timestamp format.

    Args:
        log_path (str): Path to the log file.
    """
    # Ensure the log directory exists
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create a logger
    logger = logging.getLogger('iso_logger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler that logs messages
    file_handler = TimedRotatingFileHandler(log_path, when="midnight", interval=1, backupCount=7)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter that uses the ISO 8601 format
    formatter = ISOFormatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger
