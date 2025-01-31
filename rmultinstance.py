import win32api
import win32event
import sys
from colorama import init, Fore, Style

# Initialize colorama
init()

def display_ascii_art():
    ascii_art = r"""
     _________  ________ 
| ___ \  \/  |_   _|
| |_/ / .  . | | |  
|    /| |\/| | | |  
| |\ \| |  | |_| |_ 
\_| \_\_|  |_/\___/ 
                               
    roblox multi instancer
            """ + Fore.RED + "MaraK" + Style.RESET_ALL
    print(Fore.GREEN + ascii_art + Style.RESET_ALL)

def main():
    display_ascii_art()

    # Create and hold the ROBLOX_singletonMutex
    mutex_handle = win32event.CreateMutex(None, True, "ROBLOX_singletonMutex")

    if mutex_handle is None:
        print("failed to create mutex. error:", win32api.GetLastError())
        return 1

    print("multiple roblox instances are now " + Fore.GREEN + "allowed" + Style.RESET_ALL + "!")
    print("press enter to " + Fore.RED + "exit" + Style.RESET_ALL + " and release the mutex...")
    input()

    # Release the mutex
    if mutex_handle:
        win32event.ReleaseMutex(mutex_handle)
        win32api.CloseHandle(mutex_handle)
        print("mutex released. " + Fore.RED + "exiting" + Style.RESET_ALL + "...")

    return 0

if __name__ == "__main__":
    sys.exit(main())