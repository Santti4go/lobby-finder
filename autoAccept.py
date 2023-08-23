from PIL import Image, ImageTk
import pyautogui
import time
import threading
import tkinter as tk

DEBUG_PRINT = True
RESOLUTION = [0, 0, 1920, 1080]

root = tk.Tk()
root.title("League of Legends - lobby finder")
ico = Image.open("./assets/lol_icon.ico")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

class Properties:
    BUTTON_OFFSET_PX = (0, -20)


def print_log(txt):
    global DEBUG_PRINT
    if DEBUG_PRINT:
        print(txt)


def getScreenshot(resolution, scale=1) -> Image:
    # Takes a screenshot based on provided region. 
    screenshot = pyautogui.screenshot(region=resolution)
    return screenshot


match_found_image = Image.open("./assets/accept_button.png")

SEARCH_LOBBY = True

def start_lobby():
    global SEARCH_LOBBY, thread_task
    SEARCH_LOBBY = True
    thread_task = threading.Thread(target=accept_lobby)
    thread_task.start()

def stop_lobby_search():
    global SEARCH_LOBBY
    SEARCH_LOBBY = False
    thread_task.join()

def accept_lobby():
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
            break
        else:
            time.sleep(1)



btn_initialize = tk.Button(root, text="Search for lobby",
                           width=30, height=8,
                           command=start_lobby)
btn_initialize.grid(column=0, row=0)

btn_stop = tk.Button(root, text="Stop searching lobby",
                           width=30, height=8,
                           command=stop_lobby_search)
btn_stop.grid(column=1, row=0)

root.mainloop()
