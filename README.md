# `Shell Utils` Dotfiles Setup

This repository contains personal configuration files (**dotfiles**) for:

* **Neovim** — minimal and efficient text editor setup.
* **Kitty** — fast, GPU-accelerated terminal emulator.
* **Zsh** — shell configuration with Oh My Zsh and useful plugins.
* **Btop** — Btop utiliy for system monitoring
* **Fastfetch** — Beautiful system stat fetch

## 🧠 Overview

Each configuration file is designed for a consistent and streamlined experience across systems. The setup focuses on performance, clarity, and minimalism.

## 🛠 Dependencies

Make sure the following are installed:

* Linux(Linux or WSL), Mac OS(Darwin) or BSD like system(freeBSD or openBSD) 
* Git
* Fonts: `MesloLGS NF` (for Powerlevel10k)

## 🚀 Installation

Clone this repository and run python script for automatic installation:

```Shell
git clone https://github.com/trapplus/dotfiles.git
cd dotfiles
python3 main.py
```
**In not arch/debiad based distros** - 
Install `zsh`, `btop`, `fastfetch`, `kitty`, `neovim` and run this command:

***Exit from new shell** after first setup if you want go next step of installing!*
```shell
cp resources/.zshrc ~/&&cp -r resources/kitty ~/.config&&cp -r resources/nvim ~/.config&&cp -r resources/btop ~/.config&&cp -r resources/fastfetch ~/.config&&mkdir -p ~/.zsh/plugins&&cd ~/.zsh/plugins&&git clone https://github.com/zsh-users/zsh-autosuggestions&&git clone https://github.com/zsh-users/zsh-syntax-highlighting&&git clone https://github.com/zsh-users/zsh-completions&&curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
```

## 📬 Notes

Fork or modify these dotfiles to match your workflow. Contributions and suggestions are welcome!
