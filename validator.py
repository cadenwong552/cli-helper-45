import re

class InputGuardian:
    def __init__(self, patterns):
        self.patterns = {k: re.compile(v) for k, v in patterns.items()}

    def validate(self, key, value):
        if key not in self.patterns:
            return False
        return bool(self.patterns[key].match(str(value)))

def sanitize_gaming_input(raw_input):
    # Cleanse input for game commands, allowing alphanumeric and underscores only
    return re.sub(r'[^a-zA-Z0-9_]', '', raw_input).lower()

def process_loop(guardian):
    print("--- cli-helper-45 session active ---")
    while True:
        user_raw = input(">>> ")
        if user_raw.lower() in ['exit', 'quit']:
            break
            
        cmd, *args = user_raw.split()
        if guardian.validate('command', cmd):
            print(f"Executing: {cmd}")
        else:
            print(f"Invalid command sequence: {cmd}")

if __name__ == '__main__':
    g = InputGuardian({'command': r'^[a-z]{3,12}$'})
    process_loop(g)