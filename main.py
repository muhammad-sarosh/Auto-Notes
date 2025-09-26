# If on linux program must be run with root. Use the following command if you have a venv and replace
# 'linux_env' with the name of your venv. Otherwise replace './linux_env/bin/python' with 'python':
# sudo ./linux_env/bin/python main.py

import time
import keyboard
import platform

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

# Main
try:
    # Adjust delays according to preference
    DEFAULT_DELAY = 0.3
    REGION_SS_DELAY = 4

    # Adjust screenshot keybinds according to preference
    if platform.system() == "Windows":
        REGION_SS = 'win+shift+s'
        PRINT_SCREEN_KEY = 'print screen'
    elif platform.system() == "Linux":
        REGION_SS = 'win+shift+s'
        PRINT_SCREEN_KEY = 'compose'
    else:
        print('System not supported')
        exit()

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

    # Adjust hotkey binds according to preference. Try not to have more than 1 modifier
    # as the program might not work as intended then
    keyboard.add_hotkey("shift + 3", lambda: run_macro(switch_enter))
    keyboard.add_hotkey("shift + 1", lambda: run_macro(ss_switch_paste))
    keyboard.add_hotkey("shift + 4", lambda: run_macro(ss_switch_paste_long))
    keyboard.add_hotkey("shift + 2", lambda: run_macro(ss_switch_paste_enter))
    keyboard.add_hotkey("shift + 5", lambda: run_macro(ss_switch_paste_enter_long))
    keyboard.wait()
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()