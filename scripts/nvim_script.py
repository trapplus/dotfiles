"""
Neovim configuration manager.
Moves nvim configs to the appropriate location.
"""

from pathlib import Path
from scripts.base import DotfileScript


class NvimScript(DotfileScript):
    """Manages Neovim configuration files."""

    def __init__(self):
        """Initialize nvim script with source and target directories."""
        repo_root = Path(__file__).parent.parent
        source_dir = repo_root / "configs" / "nvim"
        target_dir = Path.home() / ".config" / "nvim"
        
        super().__init__("nvim", str(source_dir), str(target_dir))

    def apply(self) -> bool:
        """
        Apply neovim configuration (no special actions needed).
        
        Returns:
            True (always succeeds as no special action is required)
        """
        print("[nvim] Configuration moved successfully!")
        print("[nvim] Neovim will automatically load the new configuration on next launch.")
        print("[nvim] If you use lazy.nvim, plugins will be installed automatically on first run.")
        return True
