# ============================================================
# FISH CONFIGURATION
# ============================================================

# --- Fish Prompt (fallback если starship не найден) ---
function fish_prompt -d "Write out the prompt"
    printf '%s@%s %s%s%s > ' $USER $hostname \
        (set_color $fish_color_cwd) (prompt_pwd) (set_color normal)
end

# --- Кеширование init-скриптов (starship, zoxide и т.д.) ---
# Генерирует init один раз, при обновлении бинарника — пересоздаёт кеш
function _cache_init
    set -l cmd $argv[1]
    set -l cache_file ~/.cache/fish/$cmd.fish
    set -l bin (command -s $cmd)

    # Если команда не найдена — пропускаем
    if test -z "$bin"
        return
    end

    # Если кеша нет или бинарник обновился — пересоздаём
    if not test -f $cache_file; or test $bin -nt $cache_file
        mkdir -p ~/.cache/fish
        $bin init fish > $cache_file
    end

    source $cache_file
end

function _qss_init
    # Quickshell Sequences (Hyprland integration)
    # Запускаем в фоне (&) чтобы не блокировать старт терминала
    if test -f ~/.local/state/quickshell/user/generated/terminal/sequences.txt
        cat ~/.local/state/quickshell/user/generated/terminal/sequences.txt &
    end
end


# --- Интерактивная сессия ---
if status is-interactive
    
    set fish_greeting

    # Starship Prompt (через кеш — ~10x быстрее чем | source каждый раз)
    _cache_init starship
    
    # --------------------------------------------------------
    # Fastfetch при старте 
    # Не запускать в: tmux, zellij, zed, ssh
    # --------------------------------------------------------
    if not set -q TMUX
        and not set -q ZELLIJ
        and not set -q ZED_TERM
        and not set -q SSH_CONNECTION
        fastfetch -c os
    end
    
    _qss_init
     
    # --------------------------------------------------------
    # Aliases — Terminal & Shell Utils
    # --------------------------------------------------------
    alias clear "printf '\033[2J\033[3J\033[1;1H'"
    alias celar "printf '\033[2J\033[3J\033[1;1H'"
    alias claer "printf '\033[2J\033[3J\033[1;1H'"
    alias c     "clear"
    alias q     "exit"
    alias r     "reset"

    # --------------------------------------------------------
    # Aliases — System & Monitoring
    # --------------------------------------------------------
    alias ls  'eza --icons'
    alias b   'btop'
    alias cmx 'cmatrix'

    # --------------------------------------------------------
    # Aliases — Fastfetch
    # --------------------------------------------------------
    alias ff   'fastfetch -c hypr'
    alias fff  'fastfetch -c groups'
    alias cff  'clear; fastfetch -c hypr'
    alias cfff 'clear; fastfetch -c groups'

    # --------------------------------------------------------
    # Aliases — Editor
    # --------------------------------------------------------
    alias nano 'nvim'
    alias erc  'nvim ~/.config/fish/config.fish'

    # --------------------------------------------------------
    # Aliases — Multiplexers
    # --------------------------------------------------------
    alias t 'tmux'
    alias j 'zellij'

    # --------------------------------------------------------
    # Aliases — Package Manager
    # --------------------------------------------------------
    alias pamcan 'pacman'
    alias pm     'pacman'

    # --------------------------------------------------------
    # Aliases — Custom / Scripts
    # --------------------------------------------------------
    alias mtk 'uv run ~/mtkclient/mtk.py'
    alias qss 'qs -c ii'

    # --------------------------------------------------------
    # Aliases — Git
    # --------------------------------------------------------
    alias g   'git'
    alias gco 'git checkout'
    alias gb  'git branch'
    alias gcm 'git commit -m'
    alias gs  'git status'
    alias gad 'git add .'
    alias ga  'git add'
    alias gc  'git clone'

    # --------------------------------------------------------
    # Aliases — Programming
    # --------------------------------------------------------
    alias d  'docker'
    alias py 'python3'
    alias cg 'cargo'
    alias m  'make'
    alias p  'pnpm'
    alias n  'npm'

    # --------------------------------------------------------
    # Aliases — Android Tools
    # --------------------------------------------------------
    alias fb 'fastboot'
    alias bl 'fastboot'
    alias ad 'adb'

    # --------------------------------------------------------
    # Aliases — Navigation (CD shortcuts)
    # --------------------------------------------------------
    alias cd2 'cd ..; cd ..'
    alias cd3 'cd ..; cd ..; cd ..'
    alias cd4 'cd ..; cd ..; cd ..; cd ..'
    alias cd5 'cd ..; cd ..; cd ..; cd ..; cd ..'
    alias cd6 'cd ..; cd ..; cd ..; cd ..; cd ..; cd ..'

    # --------------------------------------------------------
    # Aliases — Hardware (RGB)
    # --------------------------------------------------------
    alias rgboff 'openrgb -p off'
    alias rgbon  'openrgb -p main_white'
    alias po     'openrgb -p off && poweroff'

    # --------------------------------------------------------
    # Function — Python venv активация
    # --------------------------------------------------------
    function pyv
        if test -f ./.venv/bin/activate.fish
            source ./.venv/bin/activate.fish
        else if test -f ./.venv/bin/activate
            bash -c "source ./.venv/bin/activate && exec fish"
        else
            echo "Virtual environment not found"
        end
    end

    function reset
        command reset && _qss_init
    end
end

# ============================================================
# Environment Variables — PATH
# ============================================================
# fish_add_path пишет в universal variables (один раз навсегда),
# то есть НЕ выполняется при каждом старте — гораздо быстрее чем set -x PATH
# Если запускаешь первый раз — просто выполни этот конфиг, пути запомнятся.
fish_add_path ~/.local/bin
fish_add_path ~/.npm-global/bin
fish_add_path ~/.pub-cache/bin

# ============================================================
# Environment Variables — Editor
# ============================================================
# nvim по SSH, vim локально
if test -n "$SSH_CONNECTION"
    set -x EDITOR 'nvim'
else
    set -x EDITOR 'vim'
end

# ============================================================
# Tools Initialization
# ============================================================
# Zoxide (через кеш — аналогично starship)
_cache_init zoxide
