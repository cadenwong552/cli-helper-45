# cli-helper-45

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`cli-helper-45` is a lightweight Python command-line utility designed to streamline game server management and local session configuration. It eliminates repetitive setup tasks by providing rapid, automated triggers for environment variables and process handling.

### Features

*   **Process Governor:** Automatically detects and optimizes CPU affinity for high-performance game executables to minimize frame stutter.
*   **Config Injector:** Seamlessly syncs local game settings files with cloud backups or custom preset directories.
*   **Quick-Launch Hooks:** Enables pre-launch cleanup of cache directories and temporary logs with a single command.
*   **Latency Diagnostic:** Built-in network check to ping specific game server regions before launching your session.

### Installation

Requires Python 3.8+ and `pip`.

```bash
# Clone the repository
git clone https://github.com/Developer/cli-helper-45.git
cd cli-helper-45

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x cli_helper.py
```

### Usage

Use the helper to prepare your environment and launch your game automatically.

```bash
# Clean cache and apply performance profile for 'TitanFall-2'
python cli_helper.py --optimize --game "TitanFall-2"

# View real-time latency for European server regions
python cli_helper.py --ping --region eu-west
```

To see all available commands and flags, run:

```bash
python cli_helper.py --help
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.