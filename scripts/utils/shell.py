from platform import system
from subprocess import run, CompletedProcess
import shutil

class ShellController:
    def __init__(self) -> None:
        self.SYSTEM: str = system().lower()
        if self.SYSTEM != "Linux":
            raise SystemError(f"Script is runned in not compitable system!")
        
        self.SHELL: str = str(self.run_command("echo $SHELL").stdout)
        self.USER_HOSTNAME: str = str(self.run_command("echo $USER").stdout)
        self.PM_INSTALL: str = (
            "sudo pacman -S --noconfirm" if shutil.which("pacman") else 
            "sudo apt install -y" 
        )
        
    @staticmethod 
    def run_command(
        command: str, 
        shell: bool = True, 
        capture_output: bool = True, 
        text : bool = True
        ) -> CompletedProcess:
        """
        Выполняет команду через subprocess.
        
        Args:
            command: str - Основная команда для выполнения.
            shell: bool - Для работы с shell атрибутами(&& , | , $(), /).
            capture_output: bool - Если нужен вывод команды.
            text : bool - Если нужен utf-8 текст.
        
        Returns:
            CompletedProcess - Обьект выполненой команды, освновные атрибуты - stderr, stdout, returncode.
        """
        result = run(
            command,
            shell=shell,  
            capture_output=capture_output, 
            text=text
            )

        if result.stderr:
            return result.stderr

        return result.stdout.strip()

    def clear_terminal(self) -> None:
        self.run_command(
            "clear", 
            shell=False, 
            capture_output=False, 
            text=False
            )
    
    def restart(self) -> None:
        self.run_command(
            "zsh", 
            shell=False, 
            capture_output=False, 
            text=False
            )
