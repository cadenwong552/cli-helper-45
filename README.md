# cli-helper-45

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`cli-helper-45` is a high-performance Python CLI utility designed to streamline game server administration and asset management. It minimizes latency in configuration deployment, allowing developers to manage multi-environment gaming backend states with single-command efficiency.

### Features

*   **Server State Snapshotting:** Quickly capture and export local dev-server configurations into JSON blueprints for rapid deployment.
*   **Asset Compression Pipeline:** Automated batch processing to minify textures and compress audio files without losing metadata.
*   **Integrated RCON Controller:** Built-in shell interface for executing remote console commands across distributed game server clusters.
*   **Schema Validation:** Real-time checking of YAML game-logic files to prevent syntax-related runtime crashes before you deploy.

### Installation

Ensure you have Python 3.9+ installed. You can install the tool directly from PyPI:

```bash
pip install cli-helper-45
```

Alternatively, for local development:

```bash
git clone https://github.com/Developer/cli-helper-45.git
cd cli-helper-45
pip install -r requirements.txt
python setup.py install
```

### Basic Usage

Manage your server configurations directly from the terminal. To validate your current configuration file, use:

```bash
cli-helper-45 validate --config ./game_server.yaml
```

To sync your current local assets to a remote staging server:

```bash
cli-helper-45 sync --target staging --path ./assets/textures/
```

To send a global message to your players via the integrated RCON console:

```bash
cli-helper-45 rcon --host 127.0.0.1 --cmd "say 'Server maintenance in 5 minutes!'"
```

### License

Distributed under the MIT License. See `LICENSE` for more information.