typeset -g POWERLEVEL9K_INSTANT_PROMPT=off

if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to your Oh My Zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# powerlevel10k theme (Needed download this theme and restart shell)
ZSH_THEME="powerlevel10k/powerlevel10k"

# zsh plugins
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  zsh-completions
  history-substring-search
  colored-man-pages
)

# OMZ import and locale import
source $ZSH/oh-my-zsh.sh
export LANG=en_US.UTF-8

# ssh editor choice
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='nvim'
fi

# git
alias gco="git checkout"
alias gb="git branch"
alias gcm="git commit -m"
alias gm="git merge"
alias gs="git status"
alias gad="git add ."
alias ga="git add"

# shell util
alias ff="fastfetch -c hypr"
alias fff="fastfetch -c groups"
alias cff="clear&&fastfetch -c hypr"
alias cfff="clear&&fastfetch -c groups"
alias b="btop"
alias h="htop"
alias c="clear"
alias erc="nvim /home/$USER/.zshrc"
alias cmx="cmatrix"

# programming
alias d="docker"
alias pyv="source ./.venv/bin/activate"
alias py="python3"
alias cg="cargo"
alias n="nvim"

#android-tools
alias fb="fastboot"
alias ad="adb"
alias arr="adb reboot recovery"
alias asl="adb reboot sideload"
alias ffb="fastboot flash boot"
alias ffr="fastboot flash recovery"
alias frr="fastboot reboot recovery"

# CD{1..6} aliases
alias cd2="cd ..&&cd .."
alias cd3="cd ..&&cd ..&&cd .."
alias cd4="cd ..&&cd ..&&cd ..&&cd .."
alias cd5="cd ..&&cd ..&&cd ..&&cd ..&&cd .."
alias cd6="cd ..&&cd ..&&cd ..&&cd ..&&cd ..&&cd .."

# memes
alias code10="echo Ой бля пузо спалил"
# z {dir_name} init
eval "$(zoxide init zsh)"


source $HOME/.local/bin/env
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh



fastfetch -c os &!


. "$HOME/.local/bin/env"
