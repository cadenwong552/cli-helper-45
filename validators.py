import re

class InputGuardian:
    """
    A quirky gatekeeper for gaming CLI commands.
    Expects clean, arcade-ready strings.
    """
    def __init__(self, allowed_commands):
        self.commands = allowed_commands
        self.pattern = re.compile(r'^[a-zA-Z0-9_]{3,15}$')

    def validate(self, raw_input: str) -> bool:
        clean = raw_input.strip()
        if not self.pattern.match(clean):
            return False
        return clean in self.commands

    @staticmethod
    def sanitize_stats(val):
        try:
            num = int(val)
            return max(0, min(num, 9999))
        except (ValueError, TypeError):
            return 0

def run_loop(guardian):
    while True:
        user_in = input(">> ")
        if user_in.lower() in ['exit', 'quit']:
            break
        
        if guardian.validate(user_in):
            print(f"Executing {user_in}...")
        else:
            print("Input rejected by guardian logic.")

if __name__ == '__main__':
    g = InputGuardian(['start', 'stop', 'respawn', 'loot'])
    run_loop(g)