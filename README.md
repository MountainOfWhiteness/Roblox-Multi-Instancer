![RMI](rmi.png)

wanna run a zillion roblox accounts at once? this tiny python script's got your back. perfect for alts and testing.

## what it does (the good stuff)

*   ✨ **zero setup:** download, run, boom. it's that easy.
*   🪶 **lightweight:** like, 50 lines of python. tiny wow.
*   🖼️ **fancy colors:** because looking good matters ofc.
*   🪟 **windows only (for now):** sorry, mac/linux. we'll get there.

## how it works (the magic)

okay, so roblox has this thing called a "mutex." it's like a lock that says "only one roblox at a time!" this script yoinks that lock and holds onto it, so roblox *thinks* there's only one instance running.  sneaky, right?

## how to use it (super simple)

1.  grab the latest release [here](releases).
2.  run `RMI.exe`.
3.  open roblox in your browser and log into all your accounts and press play with the tool open.
4.  unleash the roblox horde. they'll all play nice together.

## build it yourself (for the code wizards)

1.  install the good stuff:

    ```bash
    pip install pywin32 colorama
    ```

2.  make it happen:

    ```bash
    pyinstaller --onefile rmultinstance.py 
    ```

3.  your baby will be in the `dist` folder.

## important stuff (listen up)

*   **anticheat warning:**  using this *might* get you in trouble with the roblox police. use with caution – blah blah blah you get the point...


## can't get it to work?(issues)

something went boom? tell us about it! go ahead, be dramatic. give us the low-down on the drama! Create an [issue here](https://github.com/MountainOfWhiteness/Roblox-Multi-Instancer/issues), preferably before the apocalypse hits.
## license

mit license – do what you want with it. im chill.

made with ❤️ by mountainofwhiteness
