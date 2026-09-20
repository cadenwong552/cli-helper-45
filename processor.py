import re
from typing import Callable, Any, Generator

class CommandValidationError(Exception):
    """Raised when a gaming CLI command fails dynamic validation."""
    pass

class GamingInputProcessor:
    def __init__(self) -> None:
        self._validators: list[tuple[re.Pattern, Callable[[tuple[str, ...]], dict[str, Any]]]] = [
            (
                re.compile(r"^move\s+(north|south|east|west)\s+(\d+)$", re.IGNORECASE),
                lambda m: {"action": "move", "direction": m[0].lower(), "steps": int(m[1])}
            ),
            (
                re.compile(r"^use\s+item:([a-z0-9_]+)(?:\s+on\s+([a-z0-9_]+))?$", re.IGNORECASE),
                lambda m: {"action": "use", "item": m[0], "target": m[1] or "self"}
            ),
            (
                re.compile(r"^cast\s+([a-z]+)\s+lvl:([1-9]|10)$", re.IGNORECASE),
                lambda m: {"action": "cast", "spell": m[0].lower(), "level": int(m[1])}
            )
        ]

    def validate_raw_input(self, raw_input: str) -> dict[str, Any]:
        clean_str = raw_input.strip()
        if not clean_str:
            raise CommandValidationError("Empty CLI command entered.")

        for pattern, parser in self._validators:
            match = pattern.match(clean_str)
            if match:
                return parser(match.groups())

        raise CommandValidationError(f"Unrecognized game command syntax: '{clean_str}'")

    def main_loop(self, input_stream: Generator[str, None, None]) -> Generator[dict[str, Any], None, None]:
        """Stream processor for gaming CLI inputs with embedded validation pipeline."""
        for raw_cmd in input_stream:
            try:
                validated_payload = self.validate_raw_input(raw_cmd)
                yield {"status": "ok", "data": validated_payload}
            except CommandValidationError as err:
                yield {"status": "error", "message": str(err), "raw": raw_cmd}

if __name__ == "__main__":
    commands = (
        "move NORTH 12",
        "cast fireball lvl:5",
        "use item:health_potion on rogue",
        "fly to sky",
        ""
    )
    processor = GamingInputProcessor()
    for result in processor.main_loop((cmd for cmd in commands)):
        print(result)
