"""
Kitty terminal emulator configuration manager.
Moves kitty configs to the appropriate location.
"""

from pathlib import Path
from scripts.base import DotfileScript


class KittyScript(DotfileScript):
    """Manages kitty terminal configuration files."""

    def __init__(self):
        """Initialize kitty script with source and target directories."""
        repo_root = Path(__file__).parent.parent
        source_dir = repo_root / "configs" / "kitty"
        target_dir = Path.home() / ".config" / "kitty"
        
        super().__init__("kitty", str(source_dir), str(target_dir))

    def apply(self) -> bool:
        """
        Apply kitty configuration (no special actions needed).
        
        Returns:
            True (always succeeds as no special action is required)
        """
        print("[kitty] Configuration moved successfully!")
        print("[kitty] Kitty will automatically load the new configuration on next launch.")
        return True
