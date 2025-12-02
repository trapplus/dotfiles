from typing import Literal

from scripts.container import shell as _shell


class downloadController:
    def __init__(self) -> None:
        self._shell_link = _shell

    def download(  # TODO: разделить интерфейсы загрузки на два разных метода
        self,
        mode: Literal["git", "pm"],
        repo_url: str | None = None,
        package_name: str | None = None,
    ) -> bool:
        """
        Метод для безопастной установки пакетов через поддерживаемые пакетники, или клонирования репозиториев.
        Args:
            mode - git or pm, при git будет использован - repo_url, при pm - package_name и подставлена соотвецтвующая методу команда.
            repo_url - Вспомогательный агрумент, при использование git режима.
            package_name - Вспомогательный агрумент, при использование pm режима.
        Returns:
            bool - Статус установки, False - ошибка, True - успешная установка.
        """
        if mode == "git":
            result = self._shell_link.run_command(f"git clone {repo_url}")
            if result.stderr:
                return False
            return True

        elif mode == "pm":
            result = self._shell_link.run_command(
                f"{self._shell_link.PM_INSTALL} {package_name}"
            )
            if result.stderr:
                return False
            return True
