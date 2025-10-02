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
alias gc="git checkout"
alias gb="git branch"
alias gcm="git commit -m"
alias gm="git merge"
# shell util
alias ff="fastfetch"
alias cff="clear&&fastfetch"
alias b="btop"
alias h="htop"
alias c="clear"
alias erc="nvim /home/$USER/.zshrc"

# programming
alias d="docker"
alias pyvenv="source ./.venv/bin/activate"
alias py="python3"
alias cg="cargo"

# CD{1..6} aliases
alias cd2="cd ..&&cd .."
alias cd3="cd ..&&cd ..&&cd .."
alias cd4="cd ..&&cd ..&&cd ..&&cd .."
alias cd5="cd ..&&cd ..&&cd ..&&cd ..&&cd .."
alias cd6="cd ..&&cd ..&&cd ..&&cd ..&&cd ..&&cd .."

# z {dir_name} init
eval "$(zoxide init zsh)"


source $HOME/.local/bin/env
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh



fastfetch -c os &!


. "$HOME/.local/bin/env"
