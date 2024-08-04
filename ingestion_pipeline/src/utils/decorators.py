import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_operation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Finished {func.__name__}")
        return result
    return wrapper