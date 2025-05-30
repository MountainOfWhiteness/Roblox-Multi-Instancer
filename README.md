![RMI](rmi.png)

Run multiple Roblox accounts at the same time. Useful for alts, testing, or just messing around.

## Features
- **Easy to use** - Download and run, that's it
- **Lightweight** - Small Python script, no bloat
- **Process detection** - Warns you if Roblox is already running
- **Auto-close** - Can close Roblox for you if needed
- **Windows only** - Mac/Linux support maybe later sorry :/

## How it works
Roblox uses a mutex (system lock) to prevent multiple instances. This tool grabs that lock first, tricking Roblox into thinking it's the only one running.

## Usage
1. Download the latest release from [releases](releases)
2. Run `RMI.exe`
3. If Roblox is already open, the tool will ask if you want to close it
4. Keep the tool running and launch Roblox normally
5. Open more Roblox instances as needed

**Important:** Run RMI before opening Roblox, not after.

## Building from source
1. Install dependencies:
   ```bash
   pip install pywin32 colorama psutil
   ```
2. Build executable:
   ```bash
   pyinstaller --onefile --name="RobloxMultiInstancer" rmultinstance.py
   ```
3. Find your exe in the `dist` folder

## Disclaimer
This tool modifies how Roblox runs. Use at your own risk. I'm not responsible if you get banned or something breaks.

## Issues
Found a bug? [Create an issue](https://github.com/MountainOfWhiteness/Roblox-Multi-Instancer/issues) with details about what went wrong.

## License
MIT License - do whatever you want with it.

Made by MountainOfWhiteness
