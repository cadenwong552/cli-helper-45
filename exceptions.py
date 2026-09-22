import random
import time
from typing import Callable, Any, Optional

class GamingCLIError(Exception):
    """Base exception for CLI helper gaming glitches and edge cases."""
    def __init__(self, message: str, glitch_code: int = 0xDEAD):
        super().__init__(message)
        self.glitch_code = glitch_code
        self.timestamp = time.time()

    def try_konami_recovery(self, sequence: list[str]) -> bool:
        """Attempts edge-case recovery using sequence input."""
        expected = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]
        return [s.lower() for s in sequence] == expected

class BossFightTimeoutError(GamingCLIError):
    """Raised when a CLI task takes longer than an enrage timer."""
    def __init__(self, boss_name: str, elapsed_seconds: float):
        self.boss_name = boss_name
        self.elapsed = elapsed_seconds
        msg = f"Enrage timer hit! Boss '{boss_name}' wiped the party after {elapsed_seconds:.1f}s."
        super().__init__(msg, glitch_code=0x4040)

    def generate_loot_compensation(self) -> dict[str, Any]:
        """Provide edge-case consolation prize on crash."""
        prizes = ["Potion of Retry", "Scroll of Stack Trace", "Consolation XP (+10)"]
        return {"compensation": random.choice(prizes), "status": "wiped"}

class SaveDataCorruptError(GamingCLIError):
    """Triggered during severe serialization issues or edge cases."""
    def __init__(self, file_path: str, payload_checksum: str):
        self.file_path = file_path
        self.checksum = payload_checksum
        super().__init__(f"Save corrupted at '{file_path}' (hash: {payload_checksum[:8]})", glitch_code=0xBADF00D)

    def auto_rollback(self, backup_handler: Optional[Callable[[str], bool]] = None) -> bool:
        """Attempts automated rollback strategy for missing or corrupt save files."""
        if backup_handler:
            return backup_handler(self.file_path)
        return False

def handle_gaming_edge_case(exc: Exception, recovery_callback: Optional[Callable] = None) -> Any:
    """Edge case processor wrapping unexpected crashes into gaming context."""
    if isinstance(exc, GamingCLIError):
        if isinstance(exc, BossFightTimeoutError):
            return exc.generate_loot_compensation()
        return {"error": str(exc), "code": hex(exc.glitch_code)}
    
    wrapped = GamingCLIError(f"Wild unexpected exception appeared: {type(exc).__name__} -> {exc}")
    if recovery_callback:
        return recovery_callback(wrapped)
    return {"error": str(wrapped), "code": hex(wrapped.glitch_code)}
