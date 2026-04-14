"""
Fish shell configuration manager.
Moves fish configs and sets fish as default shell.
"""

import subprocess
from pathlib import Path
from scripts.base import DotfileScript


class FishScript(DotfileScript):
    """Manages fish shell configuration files."""

    def __init__(self):
        """Initialize fish script with source and target directories."""
        repo_root = Path(__file__).parent.parent
        source_dir = repo_root / "configs" / "fish"
        target_dir = Path.home() / ".config" / "fish"
        
        super().__init__("fish", str(source_dir), str(target_dir))

    def apply(self) -> bool:
        """
        Set fish as the default shell for the current user.
        
        Returns:
            True if successful, False otherwise
        """
        print("[fish] Applying fish configuration...")
        
        # Find fish shell path
        try:
            result = subprocess.run(
                ["which", "fish"],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                print("[fish] WARNING: fish shell not found. Please install fish first.")
                print("[fish] You can install it with: sudo apt install fish (Debian/Ubuntu)")
                print("[fish] or: brew install fish (macOS)")
                return False
            
            fish_path = result.stdout.strip()
            print(f"[fish] Found fish at: {fish_path}")
            
            # Change default shell
            print("[fish] Changing default shell to fish...")
            result = subprocess.run(
                ["chsh", "-s", fish_path],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                print(f"[fish] WARNING: Could not change shell automatically: {result.stderr}")
                print(f"[fish] Please run manually: chsh -s {fish_path}")
            else:
                print("[fish] Default shell changed to fish successfully!")
                print("[fish] NOTE: Changes will take effect after you log out and log back in.")
            
            return True
            
        except Exception as e:
            print(f"[fish] ERROR: Failed to apply configuration: {e}")
            return False
