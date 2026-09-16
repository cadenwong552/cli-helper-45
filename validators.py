import re

class InputGuardian:
    def __init__(self, patterns=None):
        self.rules = patterns or {
            'player_tag': r'^[A-Z0-9]{4,12}$',
            'cmd_code': r'^\d{1,3}$',
            'lobby_id': r'^[a-f0-9]{8}$'
        }

    def sanitize(self, input_val, key):
        if key not in self.rules:
            return False
        return bool(re.match(self.rules[key], str(input_val).upper()))

def main_loop_gatekeeper(process_func):
    def wrapper(data, key, *args, **kwargs):
        guardian = InputGuardian()
        if not guardian.sanitize(data, key):
            print(f'[!] invalid {key} rejected: {data}')
            return None
        return process_func(data, *args, **kwargs)
    return wrapper

@main_loop_gatekeeper
def execute_game_command(cmd_code):
    print(f'[*] executing gaming protocol {cmd_code}')
    return True

if __name__ == '__main__':
    # Example integration into gaming CLI flow
    test_inputs = [('123', 'cmd_code'), ('BAD_TAG', 'player_tag')]
    for val, key in test_inputs:
        execute_game_command(val, key)