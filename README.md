# Intro to Python at Ohlone

Collection of introductory Python exercises and small GUIs from an Ohlone College class.

## Projects
- `printMeFirst/`: first program that outputs a short greeting.
- `fileCounter/`: counts files in a directory tree and demonstrates argument parsing.
- `menuFunctions/`: menu-driven CLI showcasing functions and loops.
- `mortgageGui/`: simple Tkinter mortgage calculator.
- `olympicRings/`: turtle graphics drawing of the Olympic symbol.
- `taxrate/`: applies tax rates to salary inputs.
- `whileLoopInterest/`: compound interest simulation using while loops.
- `dictionary/`: dictionary lookups plus linked zipped backup `dictionary.zip`.

Each folder also has a zipped snapshot (e.g., `menuFunctions.zip`) for quick sharing or rollback.

## Running
From the repo root run the Python script inside the directory you want to explore. Examples:

```bash
python3 menuFunctions/menu_functions.py
python3 fileCounter/file_counter.py
python3 mortgageGui/mortgage_gui.py
```

If a directory has multiple scripts, start with the one whose name matches the folder purpose or whose docstring indicates it is the entry point.

## Notes
- Most scripts expect standard Python 3 without third-party dependencies (Tkinter is required for GUI apps).
- Zipped copies contain the same scripts plus any assets, so you can unzip to inspect older snapshots.
