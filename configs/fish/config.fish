# --- Fish Prompt Configuration ---
function fish_prompt -d "Write out the prompt"
    # This shows up as USER@HOST /home/user/ >, with the directory colored
    printf '%s@%s %s%s%s > ' $USER $hostname \
        (set_color $fish_color_cwd) (prompt_pwd) (set_color normal)
end

# --- Interactive Session Config ---
if status is-interactive
    # No greeting
    set fish_greeting

    # Starship Prompt (Init)
    if command -q starship
        starship init fish | source
    end

    # Quickshell Sequences (Hyprland integration)
    if test -f ~/.local/state/quickshell/user/generated/terminal/sequences.txt
        cat ~/.local/state/quickshell/user/generated/terminal/sequences.txt
    end

    # --- Aliases ---

    # Terminal & Shell Utils
    alias clear "printf '\033[2J\033[3J\033[1;1H'"
    alias celar "printf '\033[2J\033[3J\033[1;1H'"
    alias claer "printf '\033[2J\033[3J\033[1;1H'"
    alias c "clear"
    alias q "exit" 
    # System & Monitoring
    alias ls 'eza --icons'
    alias b 'btop'
    alias cmx 'cmatrix'
    
    # Fastfetch
    alias ff 'fastfetch -c hypr'
    alias fff 'fastfetch -c groups'
    alias cff 'clear; fastfetch -c hypr'
    alias cfff 'clear; fastfetch -c groups'

    # Editor
    alias n 'nvim'
    alias nano 'nvim'
    alias erc 'nvim ~/.config/fish/config.fish'

    # Multiplexors
    alias t 'tmux'
    alias j 'zellij'

    # Package Manager
    alias pamcan 'pacman'

    # Custom/Scripts
    alias mtk 'uv run ~/mtkclient/mtk.py'
    alias qss 'qs -c ii'

    # --- Git ---
    alias g 'git'
    alias gco 'git checkout'
    alias gb 'git branch'
    alias gcm 'git commit -m'
    alias gs 'git status'
    alias gad 'git add .'

    # --- Programming ---
    alias d 'docker'
    alias py 'python3'
    alias cg 'cargo'
    
    # Python Venv Activation Function
    function pyv
        if test -f ./.venv/bin/activate.fish
            source ./.venv/bin/activate.fish
        else if test -f ./.venv/bin/activate
            bash -c "source ./.venv/bin/activate && exec fish"
        else
            echo "Virtual environment not found"
        end
    end

    # --- Android Tools ---
    alias fb 'fastboot'
    alias bl 'fastboot'
    alias ad 'adb'

    # --- Navigation (CD shortcuts) ---
    alias cd2 'cd ..; cd ..'
    alias cd3 'cd ..; cd ..; cd ..'
    alias cd4 'cd ..; cd ..; cd ..; cd ..'
    alias cd5 'cd ..; cd ..; cd ..; cd ..; cd ..'
    alias cd6 'cd ..; cd ..; cd ..; cd ..; cd ..; cd ..'

    # --- Games ---
    alias dota2 'steam -applaunch 570'

    # --- Hardware (RGB) ---
    alias rgboff 'openrgb -p off'
    alias rgbon 'openrgb -p main'

end

# --- Environment Variables (PATH) ---
# Fish automatically handles PATH as a list, no colons needed

set -x PATH $HOME/.local/bin $PATH
set -x PATH $PATH $HOME/.pub-cache/bin
set -x PATH $HOME/.npm-global/bin $PATH

# Flyctl
set -x FLYCTL_INSTALL "$HOME/.fly"
set -x PATH $FLYCTL_INSTALL/bin $PATH

# Editor Logic (SSH Detection)
if test -n "$SSH_CONNECTION"
    set -x EDITOR 'nvim'
else
    set -x EDITOR 'vim'
end

# --- Tools Initialization ---

# Zoxide 
if command -q zoxide
    zoxide init fish | source
end
