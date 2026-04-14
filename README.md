# Dotfiles Management Scripts

This repository contains automated scripts for managing dotfiles configurations.

## Structure

```
├── configs/           # Configuration files
│   ├── fish/         # Fish shell configs
│   ├── kitty/        # Kitty terminal configs
│   ├── nvim/         # Neovim configs
│   └── fastfetch/    # Fastfetch configs
├── scripts/          # Installation scripts
│   ├── base.py              # Base class for all scripts
│   ├── fish_script.py       # Fish shell manager
│   ├── kitty_script.py      # Kitty terminal manager
│   ├── nvim_script.py       # Neovim manager
│   ├── fastfetch_script.py  # Fastfetch manager
│   ├── main.py              # Main entry point
│   └── installer.sh         # One-line installer
├── install.sh        # Local installation script
└── pyproject.toml    # Python project configuration
```

## Quick Install (One-Line)

```bash
curl -fsSL https://raw.githubusercontent.com/trapplus/dotfiles/main/scripts/installer.sh | bash
```

## Manual Installation

### Prerequisites

1. **Install uv** (Python package manager):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/trapplus/dotfiles.git
   cd dotfiles
   ```

3. **Run the installation**:
   ```bash
   ./install.sh
   ```

### What the installer does

1. Checks if `uv` is installed
2. Runs `uv sync` to set up the Python environment
3. Runs `uv run python main.py` which:
   - Moves all config files to their appropriate locations (`~/.config/`)
   - Creates backups of existing configs
   - Sets fish as the default shell (for fish config)

## Configuration Locations

| Config Type | Source Directory | Target Directory |
|------------|------------------|------------------|
| Fish | `configs/fish/` | `~/.config/fish/` |
| Kitty | `configs/kitty/` | `~/.config/kitty/` |
| Neovim | `configs/nvim/` | `~/.config/nvim/` |
| Fastfetch | `configs/fastfetch/` | `~/.config/fastfetch/` |

## Scripts Overview

### `scripts/base.py`
Base class that provides common functionality for all config managers:
- `move()` - Copies configs from repo to target location, creates backups
- `apply()` - Applies configuration (override in subclasses)

### `scripts/fish_script.py`
Manages fish shell configuration:
- Moves fish configs to `~/.config/fish/`
- Changes default shell to fish using `chsh`

### `scripts/kitty_script.py`
Manages kitty terminal configuration:
- Moves kitty configs to `~/.config/kitty/`

### `scripts/nvim_script.py`
Manages Neovim configuration:
- Moves nvim configs to `~/.config/nvim/`

### `scripts/fastfetch_script.py`
Manages fastfetch configuration:
- Moves fastfetch configs to `~/.config/fastfetch/`

### `scripts/main.py`
Main entry point that runs all installation scripts:
- Executes `move()` for all configs
- Executes `apply()` for all configs
- Shows installation summary

## Notes

- **Backup**: Existing configurations are backed up to `~/.config/<name>_backup/`
- **Shell Change**: After changing the default shell to fish, you need to log out and log back in for changes to take effect
- **Permissions**: Some operations may require sudo privileges (like changing the default shell)

## Customization

To add support for new configuration types:

1. Create a new file in `scripts/` directory (e.g., `myapp_script.py`)
2. Inherit from `DotfileScript` base class
3. Override `apply()` method if special actions are needed
4. Add your script to `scripts/main.py`

Example:
```python
from pathlib import Path
from scripts.base import DotfileScript

class MyAppScript(DotfileScript):
    def __init__(self):
        repo_root = Path(__file__).parent.parent
        source_dir = repo_root / "configs" / "myapp"
        target_dir = Path.home() / ".config" / "myapp"
        super().__init__("myapp", str(source_dir), str(target_dir))
```
