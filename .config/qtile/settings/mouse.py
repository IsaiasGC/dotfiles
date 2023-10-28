from libqtile.config import Drag, Click
from libqtile.command import lazy
from .keys import alt


mouse = [
    Drag(
        [alt],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    # Drag(
    #     [alt],
    #     "Button3",
    #     lazy.window.set_size_floating(),
    #     start=lazy.window.get_size()
    # ),
    Click([alt], "Button1", lazy.window.bring_to_front())
]
