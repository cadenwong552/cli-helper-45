import json
import os
from datetime import datetime
class GameLogger:
    def __init__(self, log_path="gaming.log", max_buffer=500):
        self.log_path = log_path
        self.max_buffer = max_buffer
        self.buffer = []
        self.failure_streak = 0
    def record(self, category, payload, user=None):
        try:
            if not category or not isinstance(category, str): category = "unknown"
            if not isinstance(payload, dict): payload = {"value": str(payload)}
            if user is not None and not isinstance(user, (str, int)): user = str(user)
            entry = {"ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "cat": category.upper(), "data": payload, "usr": user}
            self.buffer.append(entry)
            if len(self.buffer) > self.max_buffer: self._merge_events()
            self._save_entry(entry)
        except Exception as err:
            self._manage_failure(err, category, payload)
    def _merge_events(self):
        summary = {"count": len(self.buffer), "types": {}}
        for e in self.buffer:
            t = e.get("cat", "UNK")
            summary["types"][t] = summary["types"].get(t, 0) + 1
        self.buffer = [{"ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "cat": "SUMMARY", "data": summary, "usr": "system"}]
    def _save_entry(self, entry):
        try:
            with open(self.log_path, "a") as log_file: log_file.write(json.dumps(entry) + "\n")
            self.failure_streak = 0
        except PermissionError:
            if entry not in self.buffer: self.buffer.append(entry)
        except OSError as os_err:
            msg = str(os_err).lower()
            if "no such file" in msg or "directory" in msg:
                try:
                    d = os.path.dirname(self.log_path)
                    if d and not os.path.exists(d): os.makedirs(d)
                except: pass
                self._save_entry(entry)
            else:
                self.failure_streak += 1
                if self.failure_streak >= 3:
                    self.buffer.clear()
                    self.failure_streak = 0
                    try:
                        if os.path.isfile(self.log_path): os.unlink(self.log_path)
                    except: pass
        except (TypeError, ValueError):
            entry["data"] = {"converted": str(entry.get("data", ""))}
            if self.buffer: self.buffer[-1] = entry
            self._save_entry(entry)
    def _manage_failure(self, err, category, payload):
        fail_entry = {"ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "cat": "FAILURE", "data": {"reason": str(err), "attempted": category, "info": str(payload)[:100]}, "usr": "logger"}
        self.buffer.append(fail_entry)
        try: print("Game log error handled: " + str(err))
        except Exception: self.buffer.append({"ts": "now", "cat": "CRIT", "data": {}, "usr": None})
    def fetch_recent(self, count=5):
        try:
            if os.path.exists(self.log_path):
                with open(self.log_path, "r") as f: lines = [l for l in f.read().strip().split("\n") if l]
                parsed = [json.loads(line) for line in lines[-count:]]
                return parsed
            return self.buffer[-count:] if self.buffer else []
        except Exception:
            return self.buffer[-count:] if self.buffer else []