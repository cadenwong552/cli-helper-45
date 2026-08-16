import logging
import time

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)


def retry_with_logging(func, retries=3, delay=2):
    logger = CustomLogger('NetworkOperation')
    for attempt in range(retries):
        try:
            result = func()
            return result
        except Exception as e:
            logger.log_error(f'Attempt {attempt + 1} failed: {e}')
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                logger.log_error('All attempts failed')
                raise
