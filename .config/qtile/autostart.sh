#!/bin/sh

# wallpaper
feh --bg-fill ~/.config/qtile/wallpaper.jpg &
# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
