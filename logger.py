import datetime
import sys
from enum import Enum

class Level(Enum):
    DEBUG = "[DEBUG]"
    QUEST = "[QUEST]"
    LOOT = "[LOOT]"
    CRIT = "[CRIT]"

def get_timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")

def log_event(level: Level, message: str, color: bool = True):
    c = {
        Level.DEBUG: "\033[94m",
        Level.QUEST: "\033[92m",
        Level.LOOT: "\033[93m",
        Level.CRIT: "\033[91m"
    }
    reset = "\033[0m" if color else ""
    prefix = f"{c.get(level, '')}{level.value} {get_timestamp()}{reset}"
    print(f"{prefix} {message}", file=sys.stdout)

class GameLogger:
    def __init__(self, name: str):
        self.name = name

    def info(self, msg: str):
        log_event(Level.QUEST, f"[{self.name}] {msg}")

    def alert(self, msg: str):
        log_event(Level.CRIT, f"!!! {self.name.upper()} ALERT: {msg} !!!")

def debug_log(data: any):
    if __debug__:
        log_event(Level.DEBUG, f"INSPECTING: {data}")