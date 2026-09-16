import sys
import time
from typing import Dict

class RetroGameLogger:
    LEVELS: Dict[str, str] = {
        "INFO": "[ QUEST ]",
        "WARNING": "[HAZARD ]",
        "ERROR": "[CRITICAL]",
        "DEBUG": "[EXPLOIT ]"
    }

    COLORS: Dict[str, str] = {
        "INFO": "\033[92m",
        "WARNING": "\033[93m",
        "ERROR": "\033[91m",
        "DEBUG": "\033[94m",
        "RESET": "\033[0m"
    }

    def __init__(self, player_name: str = "Player1"):
        self.player_name = player_name
        self.xp = 0
        self.start_time = time.time()

    def _get_uptime(self) -> str:
        elapsed = time.time() - self.start_time
        return f"{elapsed:.2f}s"

    def _render_health_bar(self, level: str) -> str:
        bar_chars = {
            "INFO": "██████████",
            "WARNING": "█████░░░░░",
            "ERROR": "█░░░░░░░░░",
            "DEBUG": "███████░░░"
        }
        return bar_chars.get(level, "░░░░░░░░░░")

    def log(self, level: str, message: str) -> None:
        level_upper = level.upper()
        if level_upper not in self.LEVELS:
            level_upper = "INFO"

        self.xp += 10 if level_upper == "INFO" else (50 if level_upper == "ERROR" else 5)
        prefix = self.LEVELS[level_upper]
        color = self.COLORS[level_upper]
        reset = self.COLORS["RESET"]
        uptime = self._get_uptime()
        bar = self._render_health_bar(level_upper)

        sys.stdout.write(
            f"{color}{prefix}{reset} "
            f"[{self.player_name} | XP: {self.xp:04d} | {uptime}] "
            f"{color}{bar}{reset} "
            f"- {message}\n"
        )
        sys.stdout.flush()

    def quest(self, msg: str) -> None:
        self.log("INFO", msg)

    def hazard(self, msg: str) -> None:
        self.log("WARNING", msg)

    def critical(self, msg: str) -> None:
        self.log("ERROR", msg)

    def exploit(self, msg: str) -> None:
        self.log("DEBUG", msg)