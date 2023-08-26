from PIL import Image, ImageTk
import pyautogui
import time
import threading
import tkinter as tk
import sys
from os import path

class Properties:
    BUTTON_OFFSET_PX = (0, -20)
    RESOLUTION = [0, 0, 1920, 1080]

def print_log(txt):
    global DEBUG_PRINT
    if DEBUG_PRINT:
        print(txt)


def getScreenshot(resolution, scale=1) -> Image:
    # Takes a screenshot based on provided region. 
    screenshot = pyautogui.screenshot(region=resolution)
    return screenshot


DEBUG_PRINT = True
SEARCH_LOBBY = False

# To work with the bundled app
if hasattr(sys, '_MEIPASS'):
    base_path = path.join(sys._MEIPASS, "assets/")
else:
    base_path = "./assets/"

root = tk.Tk()
root.title("League of Legends - lobby finder")

ico = Image.open(path.join(base_path, "lol_icon.ico"))
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
match_found_image = Image.open(path.join(base_path, "accept_button.png"))


def start_lobby_search():
    """Run the search for lobby on a new thread."""
    global SEARCH_LOBBY, THREAD_TASK
    # To avoid starting several threads
    if not SEARCH_LOBBY:
        SEARCH_LOBBY = True
        THREAD_TASK = threading.Thread(target=accept_lobby)
        THREAD_TASK.start()


def stop_lobby_search():
    """Stops the thread searching for lobby."""
    global SEARCH_LOBBY
    try:
        # Clean the variable
        SEARCH_LOBBY = False
        THREAD_TASK.join()
    except NameError:
        pass

def accept_lobby():
    """Search for a lobby."""
    global SEARCH_LOBBY
    start_time = time.time()

    while SEARCH_LOBBY:
        button_pos_aux = pyautogui.locateOnScreen(match_found_image, confidence=0.65)
        if button_pos_aux:
            button_pos = pyautogui.center(button_pos_aux) + Properties.BUTTON_OFFSET_PX
            pyautogui.moveTo(button_pos)
            pyautogui.click(button="left", clicks=1, interval=0.1)
            print_log(f"Match founded! \t \
                    Elapsed time: {time.time()-start_time}")
            SEARCH_LOBBY = False
        else:
            time.sleep(1)

def on_closing():
    """Handle closing event."""
    stop_lobby_search()
    root.destroy()

btn_initialize = tk.Button(root, text="Search for lobby",
                           width=30, height=8, activebackground="green",
                           command=start_lobby_search)
btn_initialize.grid(column=0, row=0, sticky="nsew")

btn_stop = tk.Button(root, text="Stop searching lobby",
                           width=30, height=8, activebackground="green",
                           command=stop_lobby_search)
btn_stop.grid(column=1, row=0, sticky="nsew")

# To make the buttons resize them self
root.grid_columnconfigure([0,1], weight=1)
root.grid_rowconfigure(0, weight=1)

# Configure callback when closing the window
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
