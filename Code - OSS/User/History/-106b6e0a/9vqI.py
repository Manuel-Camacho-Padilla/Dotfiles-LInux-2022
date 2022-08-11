from libqtile import widget
from libqtile import qtile
from libqtile import bar
from libqtile.config import Screen
from modules.keys import terminal
import os


# PANEL
catppuccin = {
    "flamingo": "#F2CDCD",
    "mauve": "#DDB6F2",
    "pink": "#F5C2E7",
    "maroon": "#E8A2AF",
    "red": "#F28FAD",
    "peach": "#F8BD96",
    "yellow": "#FAE3B0",
    "green": "#ABE9B3",
    "teal": "#B5E8E0",
    "blue": "92CDFB",
    "sky": "#89DCEB",
    "white": "#D9E0EE",
    "gray0": "#6E6C7E",
    "black1": "#1A1826",
}

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=16,
    padding=3,
    foreground=catppuccin["black1"],
)
extension_defaults = widget_defaults.copy()


def get_widgets(primary=False):
    widgets = [
        widget.Spacer(length=3, background="#00000000"),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background="#00000000",
        ),
        widget.TextBox(
            text="異",
            mouse_callbacks={"Button1": lazy.spawn("rofi -show run")},
            background=catppuccin["pink"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["red"],
        ),
        widget.CurrentLayoutIcon(
            padding=1,
            scale=0.8,
            background=catppuccin["red"],
            custom_icon_paths=["/home/mjs/.config/qtile/icons/"],
        ),
        widget.CurrentLayout(background=catppuccin["red"]),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["red"],
            background=catppuccin["peach"],
        ),
        widget.GroupBox(
            highlight_method="text",
            background=catppuccin["peach"],
            highlight_color=[catppuccin["peach"], catppuccin["peach"]],
            other_screen_border=catppuccin["gray0"],
            other_current_screen_border=catppuccin["white"],
            this_current_screen_border=catppuccin["white"],
            this_screen_border=catppuccin["gray0"],
            inactive=catppuccin["black1"],
        ),
        widget.TextBox(
            text="", padding=0, fontsize=30, foreground=catppuccin["peach"]
        ),
        widget.WindowName(fontsize=12, foreground=catppuccin["black1"]),
        widget.TextBox(text="", padding=0, fontsize=30, foreground=catppuccin["teal"]),
        widget.Volume(
            fmt="墳 {}",
            mute_command="amixer -D pulse set Master toggle",
            background=catppuccin["teal"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["green"],
            background=catppuccin["teal"],
        ),
        widget.CPU(
            format=" {load_percent:04}%",
            mouse_callbacks={"Button1": lazy.spawn("kitty -e htop")},
            background=catppuccin["green"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["yellow"],
            background=catppuccin["green"],
        ),
        widget.CapsNumLockIndicator(fmt=" {}", background=catppuccin["yellow"]),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["peach"],
            background=catppuccin["yellow"],
        ),
        widget.Clock(format=" %a %d %b %Y, %H:%M", background=catppuccin["peach"]),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["red"],
            background=catppuccin["peach"],
        ),
        widget.Battery(
            format="{char} {percent:2.0%}",
            charge_char="",
            discharge_char="",
            full_char="",
            unknown_char="",
            empty_char="",
            show_short_text=False,
            background=catppuccin["red"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background=catppuccin["red"],
        ),
        widget.TextBox(
            text="﫼",
            mouse_callbacks={
                "Button1": lazy.spawn("dm-tool lock"),
                "Button3": lazy.shutdown(),
            },
            background=catppuccin["pink"],
        ),
        widget.Spacer(length=10, background=catppuccin["pink"]),
        widget.TextBox(
            text="",
            mouse_callbacks={
                "Button1": lazy.spawn("systemctl suspend"),
                "Button2": lazy.spawn("systemctl restart"),
                "Button3": lazy.spawn("systemctl poweroff"),
            },
            background=catppuccin["pink"],
        ),
        widget.TextBox(
            text="",
            padding=0,
            fontsize=30,
            foreground=catppuccin["pink"],
            background="#00000000",
        ),
        widget.Spacer(length=3, background="#00000000"),
    ]
    if primary:
        widgets.insert(10, widget.Systray())
    return widgets





screens = [
    Screen(
        top=bar.Bar(
            get_widgets(primary=True),
            24,
            background="#00000000",
            margin=[2, 0, 0, 0],
        ),
    ),
    Screen(
        top=bar.Bar(
            # Use everything except the systray, which would crash
            get_widgets(primary=False),
            24,
            background="#00000000",
            margin=[2, 0, 0, 0],
        )
    ),
]