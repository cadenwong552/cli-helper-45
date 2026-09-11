import re

class GameInputValidator:
    """
    A quirky validator that uses regex black magic
    to filter gaming console commands.
    """
    def __init__(self, allowed_commands):
        self.allowed_commands = allowed_commands

    def validate(self, user_input: str) -> bool:
        if not user_input or len(user_input) > 64:
            return False

        # Strip gaming-specific junk symbols
        clean = re.sub(r'[^a-zA-Z0-9_\s]', '', user_input).strip()
        
        # Check if the command is in the gaming dictionary
        parts = clean.split()
        if not parts or parts[0].lower() not in self.allowed_commands:
            return False
            
        return True

    @staticmethod
    def sanitize_stats(value: str) -> int:
        """Extracts digits from potential XP/Level strings"""
        try:
            return int(re.search(r'\d+', value).group())
        except (AttributeError, ValueError):
            return 0

# Main loop integration mock
def process_input(raw_data):
    validator = GameInputValidator(['spawn', 'teleport', 'give', 'status'])
    if validator.validate(raw_data):
        return f"Executing: {raw_data}"
    return "Error: Illegal move detected by system"