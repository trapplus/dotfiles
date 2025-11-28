import sys

from controllers.btop import btop
from controllers.fastfetch import fastfetch
from controllers.kitty import kitty
from controllers.neovim import neovim
from controllers.zsh import zsh

import display_text

def main():
    current_controller: zsh | neovim | kitty | fastfetch | btop | None = None 

    choice: int = 0

    while True:
        print(display_text.text.mode_list.value)
        choice = int(input("Select mode:").strip())
        
        install(mode=choice, controller = current_controller) 



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
