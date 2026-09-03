import re

class GameInputValidator:
    def __init__(self):
        self._patterns = {
            'cmd': re.compile(r'^[a-z_]{3,12}$'),
            'level': re.compile(r'^lvl_[0-9]{1,3}$'),
            'coords': re.compile(r'^x\d+y\d+$')
        }

    def validate(self, input_str: str, key: str) -> bool:
        if key not in self._patterns:
            return False
        return bool(self._patterns[key].match(input_str.strip().lower()))

def main_loop():
    validator = GameInputValidator()
    print('--- cli-helper-45 session ---')
    while True:
        user_in = input('>>> ').split()
        if not user_in:
            continue
        
        cmd = user_in[0]
        args = user_in[1:] if len(user_in) > 1 else []
        
        if cmd == 'exit':
            break

        if validator.validate(cmd, 'cmd'):
            print(f'executing {cmd}...')
            for arg in args:
                if validator.validate(arg, 'level') or validator.validate(arg, 'coords'):
                    print(f'processed argument: {arg}')
                else:
                    print(f'invalid argument format: {arg}')
        else:
            print('unknown command pattern')

if __name__ == '__main__':
    main_loop()