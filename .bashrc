#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias grep='grep --color=auto'
alias cat='bat --style=plain --paging=never'
alias ls='exa --group-directories-first'
alias tree='exa -T'

[ -f ~/.fzf.bash ] && source ~/.fzf.bash

eval "$(starship init bash)"
