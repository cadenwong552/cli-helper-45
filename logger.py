import datetime
import typing

class GameLogger:
    """Custom logger for gaming cli telemetry."""
    
    def __init__(self, prefix: str = "[GAMER-45]") -> None:
        self.prefix: str = prefix

    def log(self, message: str, level: str = "INFO") -> None:
        """Formats and prints event logs to stdout."""
        timestamp: str = datetime.datetime.now().strftime("%H:%M:%S")
        formatted: str = f"{self.prefix} {timestamp} | {level} | {message}"
        print(formatted)

    def debug_frame(self, frame_data: typing.Dict[str, float]) -> None:
        """Visual representation of frame timings for debugging."""
        bar: str = "|" * int(frame_data.get("ms", 0))
        self.log(f"FPS_FRAME_TIME: {bar} {frame_data.get('ms')}ms", "DEBUG")

    def alert_critical(self, error: Exception) -> typing.NoReturn:
        """Raises exception after logging internal error state."""
        self.log(f"CRITICAL_FAIL: {str(error)}", "FATAL")
        raise error

def get_logger(name: str = "default") -> GameLogger:
    """Factory function for consistent logger instantiation."""
    return GameLogger(f"[{name.upper()}]")