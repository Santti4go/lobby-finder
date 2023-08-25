from cx_Freeze import setup, Executable

base = None

executables = [Executable("lobby_finder.py", base=base)]

packages = ["threading", "time", "PIL", "tkinter", "pyautogui"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Lobby finder",
    options = options,
    version = "0.1.0",
    description = 'League of Legends - Lobby finder',
    executables = executables
)
