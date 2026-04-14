"""
Main entry point for dotfile installation.
Runs move() and apply() methods for all configuration scripts.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.fish_script import FishScript
from scripts.kitty_script import KittyScript
from scripts.nvim_script import NvimScript
from scripts.fastfetch_script import FastfetchScript


def main():
    """Run all dotfile installation scripts."""
    print("=" * 60)
    print("Dotfile Installation Script")
    print("=" * 60)
    print()

    # Initialize all scripts
    scripts = [
        FishScript(),
        KittyScript(),
        NvimScript(),
        FastfetchScript(),
    ]

    results = {}

    # Run move() for all scripts
    print("\n>>> Running MOVE operations...\n")
    print("-" * 60)
    for script in scripts:
        success = script.move()
        results[script.config_name] = {"move": success, "apply": False}
        print()

    # Run apply() for all scripts
    print("\n>>> Running APPLY operations...\n")
    print("-" * 60)
    for script in scripts:
        if results[script.config_name]["move"]:
            success = script.apply()
            results[script.config_name]["apply"] = success
        else:
            print(f"[{script.config_name}] Skipping apply (move failed)")
            results[script.config_name]["apply"] = False
        print()

    # Summary
    print("\n" + "=" * 60)
    print("INSTALLATION SUMMARY")
    print("=" * 60)
    
    all_success = True
    for config_name, result in results.items():
        status = "✓" if result["move"] and result["apply"] else "✗"
        move_status = "✓" if result["move"] else "✗"
        apply_status = "✓" if result["apply"] else "✗"
        print(f"{status} {config_name}: move={move_status}, apply={apply_status}")
        
        if not (result["move"] and result["apply"]):
            all_success = False

    print("=" * 60)
    if all_success:
        print("✓ All configurations installed successfully!")
    else:
        print("✗ Some configurations failed to install. Check the logs above.")
    print("=" * 60)

    return 0 if all_success else 1


if __name__ == "__main__":
    exit(main())
