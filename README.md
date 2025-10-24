# Dotfiles Setup

This repository contains personal configuration files (**dotfiles**) for:

* **Neovim** — minimal and efficient text editor setup.
* **Kitty** — fast, GPU-accelerated terminal emulator.
* **Zsh** — shell configuration with Oh My Zsh and useful plugins.

## 🧠 Overview

Each configuration file is designed for a consistent and streamlined experience across systems. The setup focuses on performance, clarity, and minimalism.

## ⚙️ Components

### 📝 Neovim

* Syntax highlighting and indentation.
* Transparent background.
* Relative line numbers.
* Smart indentation and clipboard sync.
* Lightweight statusline (lightline or airline).

### 💻 Kitty

* Transparent background.
* Simple, distraction-free design.
* Custom keybindings for workspace navigation.

### 🐚 Zsh

* Based on **Oh My Zsh**.
* Plugins:

  * `zsh-autosuggestions`
  * `zsh-syntax-highlighting`
  * `zsh-completions`
* Theme: `powerlevel10k`
* Custom aliases and environment tweaks.

## 🚀 Installation

Clone this repository and copy configuration files to your home directory:

```bash
git clone https://gitlab.com/<your-username>/dotfiles.git
cd dotfiles
cp -r .config/nvim ~/.config/
cp -r .config/kitty ~/.config/
cp .zshrc ~/
```

### 🧩 Automated Installer

You can also use the included **Python installation script** to automatically install dependencies, copy configs, and fix missing plugins:

```bash
python3 install.py
```

The script will:

* Install or update **Oh My Zsh** and required plugins.
* Copy all configuration files to the correct directories.
* Apply Neovim, Kitty, and Zsh setups automatically.

## 🛠 Dependencies

Make sure the following are installed:

* Neovim
* Kitty
* Zsh
* Git
* Oh My Zsh
* Fonts: `MesloLGS NF` (for Powerlevel10k)

## 📬 Notes

Fork or modify these dotfiles to match your workflow. Contributions and suggestions are welcome!
