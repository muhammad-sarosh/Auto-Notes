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
- **Multiple screenshot modes** (full window & specific region)
- **Automatic app switching** between YouTube and Discord
- **Customizable delays** to accommodate different system speeds
- **Optional auto-send** feature for immediate posting

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
   - Position windows so you can easily switch between them

3. **Use keyboard shortcuts:**
   - `Shift + 1`: Screenshot → Switch to Discord → Paste → Switch back
   - `Shift + 2`: Screenshot → Switch to Discord → Paste → Send → Switch back
   - `Shift + 3`: Switch to Discord → Send message → Switch back
   - `Shift + 4`: Region screenshot (longer delay) → Switch → Paste → Switch back
   - `Shift + 5`: Region screenshot → Switch → Paste → Send → Switch back

4. **Stop the program:** Press `Ctrl+C` in the terminal

## ⚙️ Configuration

You can customize the program by modifying these variables in `main.py`:

```python
# Timing adjustments
DEFAULT_DELAY = 0.3      # General delay between actions
SS_DELAY = 2             # Time to take a quick screenshot
SS_LONG_DELAY = 4        # Time to select a specific region

# Keyboard shortcuts (modify as needed)
keyboard.add_hotkey("shift + 1", lambda: run_macro(ss_switch_paste))
# ... customize other shortcuts
```

## 🖥️ Platform-Specific Notes

### Windows
- Uses `Win+Shift+S` for screenshots (Windows Snipping Tool)
- No special permissions required

### Linux
- Uses configurable screenshot shortcuts (default: `Win+Shift+W` for full window, `Win+Shift+S` for region)
- **Requires root privileges** due to keyboard hook limitations
- Run with: `sudo ./linux_env/bin/python main.py`

## 🛠️ Troubleshooting

**Program doesn't respond to shortcuts:**
- Make sure the program is running and the terminal shows no errors
- Try running as administrator (Windows) or with sudo (Linux)

**Screenshots not working:**
- Verify your system's screenshot shortcuts match the program configuration
- Adjust `SS_DELAY` if the screenshot tool needs more time to activate

**App switching issues:**
- **Window focus setup is critical**: The program uses `Alt+Tab` to switch between windows, which switches to the last focused window. Make sure your browser (YouTube) and Discord are the last two applications you've used before starting the program, so `Alt+Tab` switches correctly between them
- Ensure both YouTube and Discord are open and not minimized
- Adjust `DEFAULT_DELAY` if window switching is too fast/slow for your system