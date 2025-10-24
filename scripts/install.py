import os
import subprocess
from pathlib import Path

class manager:
    def __init__(self):
        self.HOME = Path.home()
        self.ZSH_CUSTOM = self.HOME / ".oh-my-zsh/custom"
        self.ZSHRC = self.HOME / ".zshrc"

    @staticmethod
    def run(cmd):
        print(f"→ {cmd}")
        subprocess.run(cmd, shell=True, check=False)

    def ensure_oh_my_zsh(self):
        if not (self.HOME / ".oh-my-zsh").exists():
            print("[+] Installing oh-my-zsh...")
            self.run('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
        else:
            print("[=] oh-my-zsh already installed.")

    def install_plugin(self, repo, folder_name):
        dest = self.ZSH_CUSTOM / "plugins" / folder_name
        if not dest.exists():
            self.run(f"git clone https://github.com/{repo}.git {dest}")
        else:
            print(f"[=] {folder_name} already exists.")

    def install_theme(self):
        theme_path = self.ZSH_CUSTOM / "themes" / "powerlevel10k"
        if not theme_path.exists():
            self.run(f"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git {theme_path}")
        else:
            print("[=] powerlevel10k already exists.")

    def fix_zshrc(self):
        if not self.ZSHRC.exists():
            print("[!] No .zshrc found, creating new one...")
            self.ZSHRC.write_text("")
        else:
            self.run(f"cp {self.ZSHRC} {self.ZSHRC}.backup")

        text = self.ZSHRC.read_text()

        lines = [l for l in text.splitlines() if "/home/trapplus/.local/bin/env" not in l]
        text = "\n".join(lines)

        if "plugins=(" not in text:
            text += "\nplugins=(git zsh-autosuggestions zsh-syntax-highlighting zsh-completions)\n"
        if "ZSH_THEME=" not in text:
            text += '\nZSH_THEME="powerlevel10k/powerlevel10k"\n'

        self.ZSHRC.write_text(text)
        print("[+] .zshrc fixed and updated.")

