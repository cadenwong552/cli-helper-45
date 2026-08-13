import logging

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        handler = logging.FileHandler(f'{name}.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

if __name__ == '__main__':
    logger = GameLogger('game_events')
    try:
        user_input = input('Enter command: ')
        if not user_input:
            raise ValueError('Input cannot be empty')
        elif len(user_input) > 100:
            raise ValueError('Input too long')
        logger.log_info(f'User entered: {user_input}')
    except ValueError as e:
        logger.log_error(f'Input validation error: {e}')
        print('Error:', e)