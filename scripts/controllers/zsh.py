from container import shell, files, loads

class zsh:
    def __init__(self) -> None:
        self.shell = shell
        self.zsh_is_installed: bool = True if shell.run_command("zsh --version").returncode == 0 else False
        self.config_is_installed: bool = False
        self.omz_is_installed: bool = True if shell.run_command("omz version").returncode == 0 else False 
        self.OMZ_INSTALLER_Load_SCRIPT: str = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
    
    def install(self) -> bool:
        if not self.zsh_is_installed:
            print(f"Installing zsh terminal from package manager")
            loads.download("pm", package_name="zsh")
            
            if shell.run_command("zsh -v").returncode == 0:
                print("[+] zsh installed!")
                self.zsh_is_installed = True
            else:
                print("[-] zsh not installed! try manual install zsh.")
                self.zsh_is_installed = False

    
        

        if not self.omz_is_installed:
            self.shell.run_command(self.OMZ_INSTALLER_Load_SCRIPT)
            
            if shell.run_command("omz version").returncode == 0:
                self.omz_is_installed = True
                print("[+] Oh-my-Zsh installed!")
            else:
                print("[-] Oh-my-Zsh not installed! Try manual install Oh-my-Zsh .")
        
        elif self.omz_is_installed:
            pass # TODO

        result = files.copy_dotfile(".zshrc", files.ZSHRC)    
        
        if result == True:
            print("[+] zshrc installed!")
            self.config_is_installed = True
        else:
            print("[-] zshrc not installed! Try manual replace .zshrc file.")
            self.config_is_installed = False

        return True if self.zsh_is_installed and self.config_is_installed and self.omz_is_installed else False
