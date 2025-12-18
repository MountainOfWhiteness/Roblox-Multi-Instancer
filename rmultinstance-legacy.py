import win32api
import win32event
import win32gui
import win32process
import psutil
import sys
import tkinter as tk
from tkinter import messagebox
from colorama import init, Fore, Style, Back
import time
import threading

# Initialize colorama
init()

def display_ascii_art():
    ascii_art = r"""
    ╔══════════════════════════════════════╗
    ║                                      ║
    ║      ██████  ███    ███ ██          ║
    ║      ██   ██ ████  ████ ██          ║
    ║      ██████  ██ ████ ██ ██          ║
    ║      ██   ██ ██  ██  ██ ██          ║
    ║      ██   ██ ██      ██ ██          ║
    ║                                      ║
    ║         ROBLOX MULTI INSTANCER       ║
    ║                                      ║
    ║    » by mountainofwhiteness          ║
    ║    »       yours truly               ║
    ║                                      ║
    ║                                      ║
    ╚══════════════════════════════════════╝
    """
    print(Fore.CYAN + ascii_art + Style.RESET_ALL)

def is_roblox_running():
    """Check if Roblox processes are running"""
    roblox_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in ['robloxplayerbeta.exe', 'roblox.exe', 'robloxstudio.exe']:
                roblox_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return roblox_processes

def terminate_roblox_processes():
    """Terminate all Roblox processes"""
    terminated = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in ['robloxplayerbeta.exe', 'roblox.exe', 'robloxstudio.exe']:
                process = psutil.Process(proc.info['pid'])
                process.terminate()
                terminated.append(proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return terminated

def show_warning_popup():
    """Show a warning popup when Roblox is already running"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    result = messagebox.askyesno(
        "Roblox Multi-Instancer Warning",
        "⚠️ Roblox is currently running!\n\n"
        "For RMI to work properly, Roblox needs to be closed first.\n"
        "This allows RMI to properly work before Roblox starts.\n\n"
        "Would you like to close Roblox now and continue?",
        icon='warning'
    )
    
    root.destroy()
    return result

def print_status(message, status_type="info"):
    """Print formatted status messages"""
    if status_type == "success":
        print(f"[{Fore.GREEN}✓{Style.RESET_ALL}] {message}")
    elif status_type == "warning":
        print(f"[{Fore.YELLOW}⚠{Style.RESET_ALL}] {message}")
    elif status_type == "error":
        print(f"[{Fore.RED}✗{Style.RESET_ALL}] {message}")
    elif status_type == "info":
        print(f"[{Fore.CYAN}i{Style.RESET_ALL}] {message}")

def print_separator():
    print(Fore.BLUE + "─" * 50 + Style.RESET_ALL)

def monitor_mutex(mutex_handle):
    """Monitor the mutex :D"""
    try:
        while True:
            time.sleep(5)  # Check every 5 seconds
            if mutex_handle is None:
                break
    except KeyboardInterrupt:
        pass

def main():
    display_ascii_art()
    print_separator()
    
    # Check if Roblox is already running
    running_processes = is_roblox_running()
    
    if running_processes:
        print_status("Roblox processes detected:", "warning")
        for proc in running_processes:
            print(f"    • {proc['name']} (PID: {proc['pid']})")
        
        print_separator()
        
        # Show popup warning
        if show_warning_popup():
            print_status("Terminating Roblox processes...", "info")
            terminated = terminate_roblox_processes()
            
            if terminated:
                print_status(f"Successfully closed: {', '.join(set(terminated))}", "success")
                time.sleep(2)  # Wait for processes to fully terminate
            else:
                print_status("No processes were terminated", "warning")
        else:
            print_status("User chose not to close Roblox", "info")
            print_status("RMI may not work properly with Roblox already running", "warning")
            print_status("Consider closing Roblox manually and restarting RMI", "info")
            print_separator()
            print("Press Enter to exit...")
            input()
            return 1

    print_separator()
    
    # Create and hold the fkn mutex
    print_status("Creating singleton mutex...", "info")
    mutex_handle = win32event.CreateMutex(None, True, "ROBLOX_singletonMutex")

    if mutex_handle is None:
        print_status(f"Failed to create mutex. Error: {win32api.GetLastError()}", "error")
        return 1

    print_status("Mutex created successfully!", "success")
    print_separator()
    
    # Success message with enhanced formatting
    print(f"\n{Back.GREEN}{Fore.BLACK} RMI ENABLED {Style.RESET_ALL}")
    print(f"\n{Fore.GREEN} Multiple Roblox instances are now allowed!{Style.RESET_ALL}")
    print(f"{Fore.CYAN} You can now run Roblox on multiple accounts simultaneously{Style.RESET_ALL}")

    
    print_separator()
    print(f"{Fore.MAGENTA}🔧 Instructions:{Style.RESET_ALL}")
    print("   1. Keep this window open")
    print("   2. Launch Roblox as many times as needed")
    print("   3. Each instance will run independently")
    print_separator()
    
    # Start monitoring thread
    monitor_thread = threading.Thread(target=monitor_mutex, args=(mutex_handle,), daemon=True)
    monitor_thread.start()
    
    print(f"\n{Fore.RED}Press Enter to exit and release the mutex...{Style.RESET_ALL}")
    
    try:
        input()
    except KeyboardInterrupt:
        pass

    # Release the mutex
    print_status("Releasing mutex...", "info")
    if mutex_handle:
        win32event.ReleaseMutex(mutex_handle)
        win32api.CloseHandle(mutex_handle)
        print_status("Mutex released successfully", "success")

    print_status("RMI shutting down...", "info")
    print(f"\n{Fore.GREEN}Thank you for using RMI!{Style.RESET_ALL}")
    time.sleep(1)
    
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
        sys.exit(1)
