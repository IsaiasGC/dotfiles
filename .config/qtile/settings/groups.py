# Qtile workspaces

from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-md-discord, 
# nf-dev-codeigniter, 
# nf-dev-terminal, 
# nf-custom-folder, 
# nf-oct-tools, 

spaces: dict[str, list[Match]] = {
    "   ": [Match(wm_class="firefox")],
    " 󰙯 ": [Match(wm_class="discord")],
    "  ": [Match(wm_class="code")],
    "  ": [Match(wm_class="alacritty")],
    "  ": [Match(wm_class="thunar")],
    " 󱁤 ": [],
}

groups = [Group(label, matches=match) for label, match in spaces.items()]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
