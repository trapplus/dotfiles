"""
Base class for dotfile management scripts.
Each config type (fish, kitty, nvim, fastfetch) should inherit from this class.
"""

import os
import shutil
from pathlib import Path
from typing import Optional


class DotfileScript:
    """Base class for managing dotfiles."""

    def __init__(self, config_name: str, source_dir: str, target_dir: str):
        """
        Initialize the dotfile script.

        Args:
            config_name: Name of the configuration (e.g., 'fish', 'kitty')
            source_dir: Directory where configs are stored in the repo
            target_dir: Target directory where configs should be installed
        """
        self.config_name = config_name
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir).expanduser()
        self.backup_dir: Optional[Path] = None

    def move(self) -> bool:
        """
        Move config files from source to target location.
        Creates backup of existing configs if they exist.

        Returns:
            True if successful, False otherwise
        """
        print(f"[{self.config_name}] Starting move operation...")

        if not self.source_dir.exists():
            print(f"[{self.config_name}] ERROR: Source directory does not exist: {self.source_dir}")
            return False

        # Create backup if target exists
        if self.target_dir.exists():
            self.backup_dir = self.target_dir.parent / f"{self.config_name}_backup"
            print(f"[{self.config_name}] Creating backup at: {self.backup_dir}")
            if self.backup_dir.exists():
                shutil.rmtree(self.backup_dir)
            shutil.copytree(self.target_dir, self.backup_dir, symlinks=True, ignore_dangling_symlinks=True)
            print(f"[{self.config_name}] Backup created successfully")

        # Remove existing target directory
        if self.target_dir.exists():
            print(f"[{self.config_name}] Removing existing target directory: {self.target_dir}")
            shutil.rmtree(self.target_dir)

        # Copy new configs (with symlinks support)
        print(f"[{self.config_name}] Copying configs from {self.source_dir} to {self.target_dir}")
        shutil.copytree(self.source_dir, self.target_dir, symlinks=True)
        print(f"[{self.config_name}] Move operation completed successfully")
        return True

    def apply(self) -> bool:
        """
        Apply the configuration after moving.
        Override this method in subclasses for specific actions.

        Returns:
            True if successful, False otherwise
        """
        print(f"[{self.config_name}] Apply operation completed (no action needed)")
        return True
