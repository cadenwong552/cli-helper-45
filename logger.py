import sys
from datetime import datetime
from typing import Any

class GamingLogger:
    def __init__(self, debug_mode: bool = False):
        self.debug_mode = debug_mode
        self.colors = {'info': '\033[94m', 'warn': '\033[93m', 'crit': '\033[91m', 'end': '\033[0m'}

    def log(self, level: str, message: str, metadata: dict[str, Any] | None = None) -> None:
        timestamp = datetime.now().strftime('%H:%M:%S')
        color = self.colors.get(level.lower(), '')
        prefix = f"{color}[{level.upper()}][{timestamp}]{self.colors['end']}"
        
        output = f"{prefix} {message}"
        if metadata:
            output += f" | context: {metadata}"
            
        sys.stdout.write(output + '\n')

    def capture_event(self, event_name: str, score: int, player_id: str = 'guest') -> None:
        """Specialized hook for high-frequency gaming telemetry."""
        severity = 'info'
        if score < 0:
            severity = 'crit'
        
        self.log(severity, f"event: {event_name}", {"score": score, "uid": player_id})

logger = GamingLogger()