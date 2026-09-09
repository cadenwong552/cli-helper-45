import re

class GameInputValidator:
    def __init__(self):
        self.patterns = {
            'cmd': r'^(quit|jump|shoot|loot|map:w+)',
            'coord': r'^d{1,3},d{1,3}$'
        }

    def validate(self, raw_input):
        cmd_match = re.match(self.patterns['cmd'], raw_input)
        if cmd_match:
            return True, cmd_match.group(0)
        return False, None

def process_game_loop():
    validator = GameInputValidator()
    print("cli-helper-45 session active. Awaiting command...")
    
    while True:
        try:
            user_input = input(">> ").strip().lower()
            if user_input == 'exit':
                break
            
            is_valid, command = validator.validate(user_input)
            
            if is_valid:
                handle_action(command)
            else:
                print(f"invalid input '{user_input}' detected - aborting command sequence")
                
        except EOFError:
            break

def handle_action(command):
    mapping = {
        'jump': lambda: print("character performs leap"),
        'shoot': lambda: print("weapon fired"),
        'loot': lambda: print("inventory updated")
    }
    action = mapping.get(command, lambda: print(f"executing dynamic command: {command}"))
    action()

if __name__ == "__main__":
    process_game_loop()