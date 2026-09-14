import re

class GameInputSanitizer:
    def __init__(self, allowed_commands=None):
        self.commands = allowed_commands or {'play', 'quit', 'save', 'load', 'stats'}

    def validate(self, user_input):
        raw = str(user_input).strip().lower()
        if not raw:
            return None
        
        token = re.split(r'\s+', raw)[0]
        if token in self.commands:
            return token
        return None

def input_loop(sanitizer):
    while True:
        try:
            user_text = input('>> ')
            cmd = sanitizer.validate(user_text)
            if cmd:
                yield cmd
            else:
                print(f'Unknown sequence: {user_text[:10]}')
        except (EOFError, KeyboardInterrupt):
            break

if __name__ == '__main__':
    # usage example within cli-helper-45 game loop
    validator = GameInputSanitizer()
    for command in input_loop(validator):
        print(f'Executing action: {command}')