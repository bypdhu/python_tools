import logging
from logging import handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGER_PATH = os.path.join(BASE_DIR, 'logs', 'logs')  # like: /var/XXX/logs/logs   /var/XXX/logs/logs.2017-11.12


def init_logger(path):
    log_formatter = "%(asctime)s | %(levelname)s - %(message)s"
    date_formatter = "%Y-%m-%d %H:%M:%S"
    if isinstance(path, str) and os.path.exists(os.path.dirname(path)):
        log = logging.getLogger('logger_name')
        logHandler = handlers.TimedRotatingFileHandler(path, when='midnight')
        logFormatter = logging.Formatter(fmt=log_formatter, datefmt=date_formatter)
        logHandler.setFormatter(logFormatter)
        log.addHandler(logHandler)
        log.setLevel(logging.DEBUG)
        log.propagate = False  # disable console output
    else:
        logging.basicConfig(level=logging.DEBUG,
                            format=log_formatter, datefmt=date_formatter)
        log = logging.getLogger('logger_name')
    return log


LOGGER = init_logger(LOGGER_PATH)
