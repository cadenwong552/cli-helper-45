import re
from typing import Any, Optional

class InputValidator:
    """Gaming CLI input validation logic using patterns."""
    
    COMMAND_MAP = {
        'move': r'^(up|down|left|right)$',
        'attack': r'^(slash|stab|magic|spell_\d+)$',
        'inventory': r'^(show|drop|use|equip)\s[a-z0-9_]+$'
    }

    def __init__(self, debug_mode: bool = False):
        self.debug = debug_mode

    def validate(self, cmd: str, args: str) -> bool:
        if cmd not in self.COMMAND_MAP:
            return False
        
        pattern = self.COMMAND_MAP[cmd]
        input_str = f"{cmd} {args}".strip() if args else cmd
        
        match = re.match(pattern, input_str)
        if self.debug and not match:
            print(f"[Validator] Rejected: {input_str}")
        
        return bool(match)

    def sanitize_input(self, raw_input: str) -> tuple[str, str]:
        parts = raw_input.lower().strip().split(' ', 1)
        command = parts[0]
        arguments = parts[1] if len(parts) > 1 else ""
        return command, arguments

def run_loop(validator: InputValidator):
    while True:
        user_input = input("cli-helper-45 > ")
        if user_input.lower() == 'exit':
            break
            
        cmd, args = validator.sanitize_input(user_input)
        if validator.validate(cmd, args):
            print(f"Executing {cmd} with {args or 'default'}")
        else:
            print("Invalid command syntax for current game state")