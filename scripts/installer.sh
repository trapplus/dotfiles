#!/bin/bash

# One-line Dotfiles Installer
# Usage: curl -fsSL <URL_TO_THIS_SCRIPT> | bash
#
# This script:
# 1. Clones the dotfiles repository
# 2. Navigates to the directory
# 3. Runs the installation script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Dotfiles One-Line Installer${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Default repository URL (replace with your actual GitHub repo)
REPO_URL="${DOTFILES_REPO_URL:-https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git}"
BRANCH="${DOTFILES_BRANCH:-main}"

# Check if repository URL was provided
if [ "$REPO_URL" = "https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git" ]; then
    echo -e "${RED}ERROR: Repository URL not configured!${NC}"
    echo ""
    echo "Please set the DOTFILES_REPO_URL environment variable:"
    echo "  export DOTFILES_REPO_URL=https://github.com/your-username/your-repo.git"
    echo ""
    echo "Or modify this script with your actual repository URL."
    echo ""
    exit 1
fi

# Install git if not present
if ! command -v git &> /dev/null; then
    echo -e "${YELLOW}Git not found. Installing git...${NC}"
    if command -v apt-get &> /dev/null; then
        sudo apt-get update && sudo apt-get install -y git
    elif command -v yum &> /dev/null; then
        sudo yum install -y git
    elif command -v brew &> /dev/null; then
        brew install git
    else
        echo -e "${RED}ERROR: Could not install git automatically.${NC}"
        echo "Please install git manually and run this script again."
        exit 1
    fi
fi

# Install uv if not present
if ! command -v uv &> /dev/null; then
    echo -e "${YELLOW}uv not found. Installing uv...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Source the uv environment
    if [ -f "$HOME/.local/bin/env" ]; then
        source "$HOME/.local/bin/env"
    elif [ -f "$HOME/.cargo/env" ]; then
        source "$HOME/.cargo/env"
    fi
    
    # Add to PATH for current session
    export PATH="$HOME/.local/bin:$PATH"
fi

# Clone the repository
REPO_NAME=$(basename "$REPO_URL" .git)
TARGET_DIR="$HOME/$REPO_NAME"

if [ -d "$TARGET_DIR" ]; then
    echo -e "${YELLOW}Directory $TARGET_DIR already exists.${NC}"
    read -p "Do you want to remove it and clone again? (y/N) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$TARGET_DIR"
    else
        echo -e "${YELLOW}Using existing directory...${NC}"
    fi
fi

if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${GREEN}Cloning repository from: $REPO_URL${NC}"
    git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$TARGET_DIR"
fi

# Navigate to the directory
cd "$TARGET_DIR"

echo ""
echo -e "${GREEN}Running installation script...${NC}"
echo ""

# Run the install.sh script
./install.sh

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Installation complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${YELLOW}NOTE: If you changed your default shell, please log out and log back in for changes to take effect.${NC}"
echo ""
