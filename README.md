# cli-helper-45

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`cli-helper-45` is a high-performance Python CLI utility designed to automate server maintenance and player data management for dedicated gaming environments. It streamlines complex console commands into intuitive flags, reducing administrative overhead for multi-server operators.

### Features

*   **Log Analytics:** Instantly parse server logs to identify latency spikes, suspicious player behavior, or script crashes.
*   **Automated Backups:** Trigger scheduled snapshots of player data and world files with integrated compression.
*   **Live Status Dashboard:** Monitor real-time player counts, CPU load, and memory usage directly in your terminal.
*   **Batch Configuration:** Update server settings or whitelist files across multiple instances with a single execution command.

### Installation

Ensure you have Python 3.8+ installed. You can install the tool via pip:

```bash
# Clone the repository
git clone https://github.com/Developer/cli-helper-45.git
cd cli-helper-45

# Install dependencies
pip install -r requirements.txt

# Install globally
pip install .
```

### Usage

Once installed, use the `ch45` command to manage your server instances.

**Check current server status:**
```bash
ch45 status --instance "US-East-01"
```

**Generate a crash report:**
```bash
ch45 logs --analyze --last 50
```

**Backup world data:**
```bash
ch45 backup --target "/opt/game_servers/world_data" --compress
```

### Roadmap
*   Support for Discord Webhook integration for real-time alerts.
*   Plugin auto-updater for popular game frameworks.
*   Interactive TUI mode for easier navigation.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.