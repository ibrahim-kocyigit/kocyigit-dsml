# ============================================================
# INSTANT PROMPT (must be at the very top)
# ============================================================
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi


# ============================================================
# PATH
# ============================================================
typeset -U path PATH
export PATH="/opt/homebrew/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"   # uv tools (pyright, black, ruff, isort)

# ============================================================
# OH MY ZSH
# ============================================================
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(git)

source $ZSH/oh-my-zsh.sh


# ============================================================
# PLUGINS
# ============================================================
source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /opt/homebrew/share/zsh-autosuggestions/zsh-autosuggestions.zsh


# ============================================================
# SSH AGENT
# ============================================================
if [[ -z "$SSH_AUTH_SOCK" ]] || ! ssh-add -l &>/dev/null; then
  eval "$(ssh-agent -s)" > /dev/null 2>&1
  ssh-add --apple-use-keychain ~/.ssh/id_ed25519 > /dev/null 2>&1
fi


# ============================================================
# ALIASES
# ============================================================
alias lsl='ls -1a'

# ============================================================
# PROMPT (p10k — must be at the very bottom)
# ============================================================
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
