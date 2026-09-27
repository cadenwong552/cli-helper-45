import re
from typing import Union, Pattern

def validate_player_tag(tag: str) -> bool:
    """Verify player tag adheres to game standards (e.g., #XXXXXX)."""
    pattern: Pattern[str] = re.compile(r'^#[A-Z0-9]{6}$')
    return bool(pattern.match(tag))

def sanitize_input(user_input: str) -> str:
    """Strip non-alphanumeric characters to prevent injection gaming exploits."""
    return re.sub(r'[^a-zA-Z0-9]', '', user_input)

def check_latency(ping: Union[int, float]) -> bool:
    """Flag potential lag spikes if ping exceeds 250ms threshold."""
    return 0 <= ping < 250

def validate_elo(rating: int) -> bool:
    """Check if ELO rating falls within valid competitive brackets."""
    return 0 <= rating <= 5000

def validate_session_token(token: str) -> bool:
    """Validate hex-encoded session tokens for auth routines."""
    if len(token) != 32:
        return False
    try:
        int(token, 16)
        return True
    except ValueError:
        return False