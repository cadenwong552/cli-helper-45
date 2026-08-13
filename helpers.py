import re
import sys

class InputValidation:
    @staticmethod
    def is_valid_integer(value):
        if re.match(r'^\d+$', value):
            return True
        return False

    @staticmethod
    def is_valid_choice(value, choices):
        return value in choices


def main_loop():
    valid_choices = ['start', 'stop', 'exit']
    while True:
        user_input = input('Enter command (start/stop/exit): ').strip().lower()

        if user_input == 'exit':
            print('Exiting...')
            sys.exit(0)

        if not InputValidation.is_valid_choice(user_input, valid_choices):
            print(f'Invalid choice: {user_input}. Please select from {valid_choices}.')
            continue

        # Simulating further processing based on choice
        if user_input == 'start':
            print('Game started!')
        elif user_input == 'stop':
            print('Game stopped!')


if __name__ == '__main__':
    main_loop()