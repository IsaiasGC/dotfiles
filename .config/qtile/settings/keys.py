# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy
from libqtile.utils import guess_terminal


mod = "mod4"
alt = "mod1"

terminal = guess_terminal("alacritty")

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([alt], "Down", lazy.layout.down()),
    ([alt], "Up", lazy.layout.up()),
    ([alt], "Left", lazy.layout.left()),
    ([alt], "Right", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle fullscreen
    ([mod], "f", lazy.window.toggle_fullscreen()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Switch between windows
    ([alt], "Tab", lazy.layout.next()),
    ([alt, "shift"], "Tab", lazy.layout.previous()),

    # Switch between groups
    ([mod], "Left", lazy.group.prevgroup()),
    ([mod], "Right", lazy.group.nextgroup()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("firefox-developer-edition")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "t", lazy.spawn(terminal)),
    ([mod], "Return", lazy.spawn(terminal)),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

   
    # Volumen
    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
