import sys
import logging

class GameStateError(Exception):
    """Custom exception for catastrophic gaming engine crashes."""
    pass

def safety_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyboardInterrupt, SystemExit) as e:
            logging.critical("Player ragequit detected: %s", e)
            sys.exit(1)
        except Exception as e:
            logging.error("Engine instability caught: %s", type(e).__name__)
            return None
    return wrapper

class ExecutionManager:
    def __init__(self):
        self.telemetry = []

    @safety_wrapper
    def execute_command(self, cmd_input):
        if not isinstance(cmd_input, str):
            raise GameStateError("Invalid input type: bytes/ints are not allowed")
        
        # Process gaming command
        tokens = cmd_input.split()
        if not tokens:
            return "Empty buffer"
        
        self.telemetry.append(tokens[0])
        return f"Command {tokens[0]} successfully executed"

    def handle_missing_assets(self, asset_path):
        try:
            with open(asset_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            logging.warning("Asset load failed: %s", asset_path)
            return "{ 'status': 'placeholder_texture' }"
        except PermissionError:
            return "{ 'status': 'access_denied' }"