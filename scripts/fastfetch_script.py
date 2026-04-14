"""
Fastfetch configuration manager.
Moves fastfetch configs to the appropriate location.
"""

from pathlib import Path
from scripts.base import DotfileScript


class FastfetchScript(DotfileScript):
    """Manages fastfetch configuration files."""

    def __init__(self):
        """Initialize fastfetch script with source and target directories."""
        repo_root = Path(__file__).parent.parent
        source_dir = repo_root / "configs" / "fastfetch"
        target_dir = Path.home() / ".config" / "fastfetch"
        
        super().__init__("fastfetch", str(source_dir), str(target_dir))

    def apply(self) -> bool:
        """
        Apply fastfetch configuration (no special actions needed).
        
        Returns:
            True (always succeeds as no special action is required)
        """
        print("[fastfetch] Configuration moved successfully!")
        print("[fastfetch] Fastfetch will automatically load the new configuration on next run.")
        return True
