import flet as ft
import keyboard
import time
import platform
import threading
from types import SimpleNamespace

# ─────────────────────── Keyboard Macros Setup ───────────────────────

# Adjust delays according to preference
DEFAULT_DELAY = 0.3
REGION_SS_DELAY = 4

running = False # Global flag to control keyboard listener thread
listener_thread = None

# Adjust screenshot keybinds according to preference
if platform.system() == "Windows":
    REGION_SS = 'win+shift+s'
    PRINT_SCREEN_KEY = 'print screen'
elif platform.system() == "Linux":
    REGION_SS = 'win+shift+s'
    PRINT_SCREEN_KEY = 'compose'
else:
    REGION_SS = 'win+shift+s'
    PRINT_SCREEN_KEY = 'print screen'

def run_macro(steps):
    for step in steps:
        # Releasing modifiers to prevent interference
        for modifier in ['ctrl', 'alt', 'shift', 'win']:
            keyboard.release(modifier)
        # Use custom delay if given, else use default. Run function if given
        if isinstance(step, tuple):
            combo, delay = step
            keyboard.press_and_release(combo)
            time.sleep(delay)
        elif isinstance(step , str):
            keyboard.press_and_release(step)
            time.sleep(DEFAULT_DELAY)
        elif callable(step):
            step()
        else:
            raise ValueError(f"Unsupported step type: {step}")

# Adjust keybinds according to preference (default alt + print screen)
# Extra delays are necessary for linux
def full_ss():
    keyboard.press("alt")
    time.sleep(0.05)
    keyboard.press(PRINT_SCREEN_KEY)
    time.sleep(0.5)
    keyboard.release("alt")
    keyboard.release(PRINT_SCREEN_KEY)
    time.sleep(1)

def go_to_textbox():
    for _ in range(6):
        keyboard.press_and_release('tab')
        time.sleep(0.1)

def start_keyboard_listener():
    global running
    try:
        # switch_enter might not work properly on linux with the 'shift + {number}' binds
        switch_enter = [
            "alt+tab",
            "enter",
            "alt+tab"
        ]

        ss_switch_paste = [
            full_ss,
            "alt+tab",
            "ctrl+v",
            "alt+tab"
        ]

        ss_switch_paste_long = [
            (REGION_SS, REGION_SS_DELAY),
            "alt+tab",
            "ctrl+v",
            "alt+tab"
        ]

        ss_switch_paste_enter = [
            full_ss,
            "alt+tab",
            "ctrl+v",
            "enter",
            "alt+tab"
        ]

        ss_switch_paste_enter_long = [
            (REGION_SS, REGION_SS_DELAY),
            "alt+tab",
            "ctrl+v",
            "enter",
            "alt+tab"
        ]

        switch_go_to_last_attachment = [
            "alt+tab",
            "tab",
            "up",
            "end",
            go_to_textbox,
            "escape",
            "alt+tab"
        ]

        switch_delete_last_attachment = [
            "alt+tab",
            "tab",
            "up",
            "end",
            "backspace",
            "escape",
            "alt+tab"
        ]

        # Adjust hotkey binds according to preference. Try not to have more than 1 modifier
        # as the program might not work as intended then
        keyboard.add_hotkey("shift + 3", lambda: run_macro(switch_enter))
        keyboard.add_hotkey("shift + 1", lambda: run_macro(ss_switch_paste))
        keyboard.add_hotkey("shift + 4", lambda: run_macro(ss_switch_paste_long))
        keyboard.add_hotkey("shift + 2", lambda: run_macro(ss_switch_paste_enter))
        keyboard.add_hotkey("shift + 5", lambda: run_macro(ss_switch_paste_enter_long))
        keyboard.add_hotkey("shift + 6", lambda: run_macro(switch_go_to_last_attachment))
        keyboard.add_hotkey("shift + 7", lambda: run_macro(switch_delete_last_attachment))

        while running:
            time.sleep(0.1)
    finally:
        keyboard.unhook_all()
        time.sleep(0.1)

# ─────────────────────── Flet UI Setup ───────────────────────
colors = SimpleNamespace(
    white = "#EFEFEF",
    black = "#0c0c0c",
    green = "#00ae77",
    green_2 = "#039567",
    red = ft.Colors.RED_700,
    red_2 = ft.Colors.RED_900
)

class CustomButton(ft.Container):
    def __init__(self, text, icon, default_color, hover_color, visible=True, callback=None):
        super().__init__()

        button = ft.ElevatedButton(
            text=text,
            expand=True,
            icon=icon,
            icon_color=colors.white,
            on_click=callback,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
                text_style=ft.TextStyle(size=25, weight=ft.FontWeight.W_600),
                color=colors.white,
                icon_size=30,
                bgcolor={
                    ft.ControlState.DEFAULT: default_color,
                    ft.ControlState.HOVERED: hover_color
                }
                
            )
        )

        self.content = ft.Column(
            [button],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH
        )

        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.with_opacity(0.3, default_color),
            offset=ft.Offset(0, 4),
        )
        self.expand = True
        self.padding = 8
        self.visible = visible

def main(page: ft.Page):
    def on_window_close(e):
        global running
        page.window.visible = False
        keyboard.unhook_all()
        time.sleep(0.1)
        running = False
        page.window.destroy()

    def run_callback(e):
        global running, listener_thread
        nonlocal run_button, stop_button

        running = True
        run_button.visible = False
        stop_button.visible = True
        
        listener_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
        listener_thread.start()

        page.update()

    def stop_callback(e):
        global running
        nonlocal run_button, stop_button

        running = False
        stop_button.visible = False
        run_button.visible = True

        page.update()

    page.title = "Auto Notes"
    page.window.width = 285
    page.window.height = 140
    page.window.center()
    page.bgcolor = colors.black
    page.window.prevent_close = True
    page.window.on_event = lambda e: on_window_close(e) if e.data == "close" else None

    run_button = CustomButton(
        text="Run",
        icon=ft.Icons.PLAY_ARROW_ROUNDED,
        default_color=colors.green,
        hover_color=colors.green_2,
        callback=run_callback
    )

    stop_button = CustomButton(
        text="Stop",
        icon=ft.Icons.STOP, 
        default_color=colors.red,
        hover_color=colors.red_2,
        visible=False,
        callback=stop_callback
    )

    page.add(run_button, stop_button)
    page.update()

ft.app(target=main)