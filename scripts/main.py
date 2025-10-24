from install import manager

def main(mg: object):
    mg.ensure_oh_my_zsh()
    mg.install_plugin("zsh-users/zsh-autosuggestions", "zsh-autosuggestions")
    mg.install_plugin("zsh-users/zsh-syntax-highlighting", "zsh-syntax-highlighting")
    mg.install_plugin("zsh-users/zsh-completions", "zsh-completions")
    mg.install_theme()
    mg.fix_zshrc()
    print("\nDone! Restart terminal or run: `source ~/.zshrc`")

if __name__ == "__main__":
    MANAGER = manager()
    main(mg = MANAGER)
