from ..container import files, loads, shell


class neovim:
    def __init__(self) -> None:
        self.shell = shell
        self.nvim_is_installed: bool = (
            True if shell.run_command("nvim -v").returncode == 0 else False
        )
        self.config_is_installed: bool = False

    def install(self) -> bool:
        if not self.nvim_is_installed:
            print("Installing neovim terminal from package manager")
            loads.download("pm", package_name="neovim")

            if shell.run_command("nvim -v").returncode == 0:
                print("[+] neovim installed!")
                self.nvim_is_installed = True
            else:
                print("[-] neovim not installed! try manual install neovim.")
                self.nvim_is_installed = False

        result = files.copy_dotdir("neovim", files.NVIM_CONFIG)

        if result:
            print("[+] neovim config installed!")
            self.config_is_installed = True
        else:
            print(
                "[-] neovim config not installed! Try manual replace neovim config directory."
            )
            self.config_is_installed = False

        return True if self.nvim_is_installed and self.config_is_installed else False
