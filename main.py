import sys

import scripts.display_text as dt
from scripts.controllers.btop import btop
from scripts.controllers.fastfetch import fastfetch
from scripts.controllers.kitty import kitty
from scripts.controllers.neovim import neovim
from scripts.controllers.zsh import zsh


def exit(code: int, message: str | None = None):
    if message:
        print(f"Exit code: {code}, Reasone:{message}")

    sys.exit(code)


def main():
    exit(1, "Currently scri[t is not work! Wait at update")

    current_controller: zsh | neovim | kitty | fastfetch | btop | None = None

    choice: int = 0

    while True:
        print(dt.text.mode_list.value)
        choice = int(input("Select mode:").strip())
        install(mode=choice, controller=current_controller)


def install(mode: int, controller: zsh | neovim | kitty | fastfetch | btop | None):
    match mode:
        case 1:
            controller = btop()
            # controller.install()
        case 2:
            controller = fastfetch()
            # controller.install()
        case 3:
            controller = kitty()
            controller.install()
        case 4:
            controller = neovim()
            controller.install()
        case 5:
            controller = zsh()
            controller.install()
        case 0:
            print("Exitting...")
            sys.exit(0)
        case _:
            print("Uncorrect choice!")


if __name__ == "__main__":
    main()
