# cli-helper-45

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

`cli-helper-45` is a lightweight command-line utility designed to streamline game modding, server management, and asset compilation workflows. It bridges the gap between raw Python automation and high-performance gaming environments without adding overhead.

## Features

- **Automated Mod Sorting:** Scans your local game directory and resolves load order conflicts for complex mod lists using custom dependency graphs.
- **Dedicated Server Watchdog:** Monitors headless server processes, auto-restarts on unexpected crashes, and pushes real-time status alerts to Discord webhooks.
- **Asset Bulk Compressor:** Converts high-resolution texture packs and audio files into game-optimized formats (DDS/XWMA) utilizing multi-core CPU parallelization.
- **Config Profile Switcher:** Instantly swaps between competitive, casual, and cinematic configuration presets with a single terminal command.

## Installation

Ensure you have Python 3.8 or higher installed on your system. Install the tool globally via pip:

```bash
pip install cli-helper-45
```

Alternatively, install from source for local development:

```bash
git clone https://github.com/Developer/cli-helper-45.git
cd cli-helper-45
pip install -e .
```

## Basic Usage

Initialize the helper inside your target game directory:

```bash
cli-helper-45 init --game "SkyrimSE"
```

To automatically sort your active mods and output a diagnostic report:

```bash
cli-helper-45 mods sort --verify --output report.txt
```

Launch the server watchdog with a custom configuration file and webhook integration:

```bash
cli-helper-45 server start --config prod_server.json --webhook "https://discord.com/api/webhooks/your-webhook-url"
```

For a complete list of available commands and flags, run:

```bash
cli-helper-45 --help
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.