import os
import shutil
import subprocess
from pathlib import Path
from container import shell as _shell

class fileController:
    def __init__(self) -> None:
        """
        Инициализация путей для работы с dotfiles.
        
        Определяет:
        - HOME: домашняя директория пользователя
        - SCRIPT_DIR: директория где лежит этот запущенный скрипт
        - DOTFILES_DIR: папка dotfiles на том же уровне что и скрипт
        - Пути к различным конфигам (zsh, nvim, kitty ,...)
        """
        self._shell_link = _shell
        self.HOME = Path.home()
        self.SCRIPT_DIR = Path(__file__).parent
        self.DOTFILES_DIR = self.SCRIPT_DIR.parent / "resources"
        
        # self.ZSH_CUSTOM = self.HOME / ".oh-my-zsh/custom"
        self.ZSHRC = self.HOME / ".zshrc"
        self.NVIM_CONFIG = self.HOME / ".config/nvim"
        self.KITTY_CONFIG = self.HOME / ".config/kitty"
        self.BTOP_CONFIG = self.HOME / ".config/btop"
        self.FASTFETCH_CONFIG = self.HOME / ".config/fastfetch"

        self.USER = self._shell_link.USER_HOSTNAME

    def copy_dotfile(self, source_name, target_path) -> bool:
        """
        Копировать один файл из папки dotfiles в систему.
        
        Создаёт бэкап существующего файла перед заменой.
        Автоматически создаёт родительские директории если нужно.
        
        Args:
            source_name (str): имя файла в папке dotfiles
            target_path (Path | str): путь куда копировать файл в системе
            
        Returns:
            bool: True если успешно, False если исходный файл не найден
        """
        source = self.DOTFILES_DIR / source_name
        
        if not source.exists():
            print(f"[!] Source file not found: {source}")
            return False
        
        target = Path(target_path)
        
        if target.exists():
            self.backup_file(target)
        
        target.parent.mkdir(parents=True, exist_ok=True)
        
        shutil.copy2(source, target)
        print(f"[+] Copied: {source} → {target}")
        return True
    
    def copy_dotdir(self, source_name, target_path) -> bool:
        """
        Копировать папку с конфигами из dotfiles в систему.
        
        Используется для конфигов которые состоят из нескольких файлов (nvim, kitty).
        Создаёт бэкап существующей папки перед заменой.
        
        Args:
            source_name (str): имя папки в dotfiles
            target_path (Path | str): путь куда копировать папку в системе
            
        Returns:
            bool: True если успешно, False если исходная папка не найдена
        """
        source = self.DOTFILES_DIR / source_name
        
        if not source.exists():
            print(f"[!] Source directory not found: {source}")
            return False
        
        target = Path(target_path)
        
        if target.exists():
            backup = Path(str(target) + ".backup")
            if backup.exists():
                shutil.rmtree(backup)
            shutil.copytree(target, backup)
            print(f"[+] Backup created: {backup}")
            shutil.rmtree(target)
        
        shutil.copytree(source, target)
        print(f"[+] Copied: {source} → {target}")
        return True

    @staticmethod 
    def backup_file(file_path) -> None:
        """
        Создает бэкап файла с суффиксом .backup.
        
        Args:
            file_path (Path): путь к файлу для бэкапа
        """
        if file_path.exists():
            backup = Path(str(file_path) + ".backup")
            shutil.copy2(file_path, backup)
            print(f"[+] Backup created: {backup}")


    # def install_dotfiles(self):
    #     """
    #     Установить все dotfiles из папки dotfiles в систему.
        
    #     Копирует:
    #     - .zshrc в домашнюю директорию
    #     - nvim конфиг в .config/nvim
    #     - kitty конфиг в .config/kitty
    #     - btop конфиг в .config/btop
    #     - fastfetch конфиг в .config/fastfetch

    #     Автоматически создаёт бэкапы существующих файлов.
    #     """
    #     print("\n[+] Installing dotfiles...")
        
    #     self.copy_dotfile(".zshrc", self.ZSHRC)
        
    #     self.copy_dotdir("nvim", self.NVIM_CONFIG)
        
    #     self.copy_dotdir("kitty", self.KITTY_CONFIG)
        
    #     self.copy_dotdir("btop", self.BTOP_CONFIG)
        
    #     self.copy_dotdir("fastfetch", self.FASTFETCH_CONFIG)

    #     print("[+] Dotfiles installed!")
