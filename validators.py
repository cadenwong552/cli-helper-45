import re

class InputValidationError(Exception):
    """Base exception for gaming input issues."""
    pass

def validate_game_command(cmd_str: str) -> str:
    """Ensures command follows [ACTION]:[ENTITY] format with quirky strictness."""
    if not cmd_str or not isinstance(cmd_str, str):
        raise InputValidationError("Silence is not a valid action, traveler.")
    
    pattern = r'^[a-z_]+:[a-z0-9_]+$'
    if not re.match(pattern, cmd_str.lower()):
        raise InputValidationError("Format violation: expected 'action:target' style.")
    
    return cmd_str.lower()

def sanitize_input(user_input: str) -> str:
    """Strip away the dark magic of dangerous characters."""
    # Remove anything that isn't a letter, number, colon, or underscore
    clean = re.sub(r'[^a-zA-Z0-9_:]', '', user_input)
    if len(clean) < 3:
        raise InputValidationError("Your input lacks sufficient substance.")
    return clean