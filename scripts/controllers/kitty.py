from container import shell, files, loads

class kitty:
    def __init__(self) -> None:
        self.shell = shell
        self.kitty_is_installed: bool = True if shell.run_command("kitty -v").returncode == 0 else False
        self.config_is_installed: bool = False
        self.KITTY_INSTALLER_URL = "https://sw.kovidgoyal.net/kitty/installer.sh"
    
    def install(self) -> bool:
        if not self.kitty_is_installed:
            print(f"Installing kitty terminal from '{self.KITTY_INSTALLER_URL}'...")
            result = shell.run_command(f"curl -L {self.KITTY_INSTALLER_URL} | sh /dev/stdin")
            
            if result.returncode == 0 and not result.stderr:
                print("[+] Kitty installed!")
                self.kitty_is_installed = True
            
            else:
                print(f"Error! Installing kitty terminal from package manager...")
                alt_result = loads.download("pm", package_name="kitty")
                if alt_result == True:
                    print("[+] Kitty installed!")
                    self.kitty_is_installed = True
        
                else:
                    print("[-] Kitty not installed! try manual install kitty.")
                    self.kitty_is_installed = False
    
        result = files.copy_dotdir("kitty",files.KITTY_CONFIG)    
        
        if result == True:
            print("[+] Kitty config installed!")
            self.config_is_installed = True
        else:
            print("[-] Kitty config not installed! Try manual replace kitty config directory.")
            self.config_is_installed = False

            
        return True if self.kitty_is_installed and self.config_is_installed else False
