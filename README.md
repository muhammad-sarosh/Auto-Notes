# Auto Notes - YouTube Lecture Screenshot Tool

A Python automation tool designed to streamline taking screenshots of YouTube lecture slides and quickly sharing them in Discord channels. Perfect for students who want to efficiently capture and organize lecture content for later review.

## 🎯 Purpose

When watching educational content on YouTube, manually taking screenshots and sharing them in Discord can be tedious and interrupt your focus. This tool automates the process with simple keyboard shortcuts, allowing you to:

- Take quick screenshots of lecture slides
- Automatically switch to Discord and paste the screenshot
- Continue watching without losing focus on the video
- Build a collection of lecture notes in your Discord channel

## ✨ Features

- **Cross-platform support** (Windows & Linux)
- **Configurable keyboard shortcuts** (default: Shift + 1-5)
- **Multiple screenshot modes** (full window via Alt+Print Screen & specific region via snipping tool)
- **Automatic app switching** between YouTube and Discord
- **Customizable delays** to accommodate different system speeds

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Discord application
- YouTube (or any video platform) in a web browser

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Auto-Notes.git
cd Auto-Notes
```

2. Create a virtual environment (recommended):
```bash
# Windows
python -m venv windows_env
windows_env\Scripts\activate

# Linux
python -m venv linux_env
source linux_env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. **Start the program:**
   ```bash
   # Windows
   python main.py
   
   # Linux (requires root for keyboard access)
   sudo ./linux_env/bin/python main.py
   ```

2. **Set up your windows:**
   - Open YouTube lecture in your browser
   - Open Discord and navigate to your notes channel
   - Position windows so if you press Alt + Tab you would switch between your browser and discord

3. **Use keyboard shortcuts:**
   - `Shift + 1`: Full window screenshot → Switch to Discord → Paste → Switch back
   - `Shift + 2`: Full window screenshot → Switch to Discord → Paste → Send → Switch back
   - `Shift + 3`: Switch to Discord → Send message → Switch back
   - `Shift + 4`: Region screenshot (longer delay) → Switch → Paste → Switch back
   - `Shift + 5`: Region screenshot → Switch → Paste → Send → Switch back

4. **Stop the program:** Press `Ctrl+C` in the terminal

## ⚙️ Configuration

You can customize the program by modifying these variables in `main.py`:

```python
# Timing adjustments
DEFAULT_DELAY = 0.3        # General delay between actions
REGION_SS_DELAY = 4        # Time to select a specific region

# Screenshot methods
def full_ss():
    keyboard.press("alt")
    time.sleep(0.05)
    keyboard.press(PRINT_SCREEN_KEY)
    time.sleep(0.5)
    keyboard.release("alt")
    keyboard.release(PRINT_SCREEN_KEY)
    time.sleep(1)

# Keyboard shortcuts (modify as needed)
keyboard.add_hotkey("shift + 1", lambda: run_macro(ss_switch_paste))
# ... customize other shortcuts
```

## 🖥️ Platform-Specific Notes

### Windows
- Uses `Alt+Print Screen` for full window screenshots (built into Windows)
- Uses `Win+Shift+S` for region screenshots (Windows Snipping Tool)
- No special permissions required

### Linux
- Uses `Alt+Print Screen` for full window screenshots
- Uses `Meta+Shift+S` for region screenshots
- **Requires root privileges** due to keyboard hook limitations
- Run with: `sudo ./linux_env/bin/python main.py`

## 🛠️ Troubleshooting

**Program doesn't respond to shortcuts:**
- Make sure the program is running and the terminal shows no errors
- Try running as administrator (Windows) or with sudo (Linux)

**Screenshots not working:**
- Verify your system's screenshot shortcuts match the program configuration
- For full window screenshots: Ensure `Alt+Print Screen` works on your system
- For region screenshots: Adjust `REGION_SS_DELAY` if the snipping tool needs more time to activate

**App switching issues:**
- **Window focus setup is critical**: The program uses `Alt+Tab` to switch between windows, which switches to the last focused window. Make sure your browser (YouTube) and Discord are the last two applications you've used before starting the program, so `Alt+Tab` switches correctly between them
- Ensure both YouTube and Discord are open and not minimized
- Adjust `DEFAULT_DELAY` if window switching is too fast/slow for your system
