#!/bin/bash

# Dotfiles Installation Script
# This script checks for uv and runs the main.py installation script

set -e

echo "========================================"
echo "Dotfiles Installer"
echo "========================================"
echo ""

# Check if uv is installed
if command -v uv &> /dev/null; then
    echo "✓ uv found: $(which uv)"
    echo ""
    echo "Running: uv sync"
    uv sync
    echo ""
    echo "Running: uv run main.py"
    cd "$(dirname "$0")/scripts"
    uv run python main.py
else
    echo "✗ uv not found!"
    echo ""
    echo "Please install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo ""
    echo "Or install via pip:"
    echo "  pip install uv"
    echo ""
    exit 1
fi

echo ""
echo "========================================"
echo "Installation complete!"
echo "========================================"
