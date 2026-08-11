import logging
import time
import random

def setup_logger(name):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger('cli_helper')

class NetworkOperationError(Exception):
    pass

def retry_logic(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except NetworkOperationError as e:
                    attempts += 1
                    logger.warning(f'Attempt {attempts} failed: {e}')
                    time.sleep(delay + random.uniform(0, 1))
            logger.error('All attempts failed')
            raise NetworkOperationError('Max retries exceeded')
        return wrapper
    return decorator

@retry_logic(max_retries=5, delay=1)
def fetch_data():
    if random.choice([True, False]):  # Simulate a network request failure
        raise NetworkOperationError('Network issue occurred')
    return 'Data fetched successfully!'

if __name__ == '__main__':
    try:
        data = fetch_data()
        logger.info(data)
    except NetworkOperationError:
        logger.critical('Failed to fetch data after retries')