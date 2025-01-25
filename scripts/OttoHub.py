import os
import shutil
import sys
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pyautogui
import subprocess
import threading
import time
import tkcalendar
from plyer import notification
import simpleaudio as sa
from pynput import keyboard
from pathlib import Path
from collections import Counter

# About
def about_otto():
    about_text = (
        "Welcome to Otto Work Optimizer!\n\n"
        "OttoInput gives the user a means to repeat a set of inputs a fixed number of times.\n"
        "OttoList generates a list for the user, converting text or providing a premade list. It can also format the list in various programming languages.\n"
        "OttoMath is a programming calculator that uses standard Python language.\n"
        "OttoNotes is a note program with the option to encrypt text.\n"
        "OttoOverwrite is a program that overwrites or appends data, using data from a user-selected file.\n"
        "OttoReminder reminds the user of a task to be done, at random intervals.\n"
        "OttoSort sorts text data in a file by various different means.\n"
        "OttoHour notifies the user of an hour passing.\n\n"
        "This program was made by Allen Rutledge using Python 3. It's free to use."
        )
    messagebox.showinfo("About Otto",about_text)
def toggle_hourpass():
    global notif_on
    notif_on = not notif_on
    status = "ON" if notif_on else "OFF"
    toggle_button.config(text=f"OttoHour {status}")
    if notif_on:
        def notify():
            while notif_on:
                time.sleep(3600) #3600 is 1 hour
                if notif_on:
                    
                    str(BASE_DIR / 'scripts' / 'hourpass.wav')
                    notification.notify(
                        title='Otto Hour',
                        message='An hour has passed.',
                        timeout=10  # seconds
                    )
        threading.Thread(target=notify,daemon=True).start()

# Base directory of the executable or script
BASE_DIR = Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else Path(__file__).resolve().parent

# Create window
def create_window():
    global rootHub, toggle_button, notif_on
    notif_on = False
    rootHub = tk.Tk()
    rootHub.title("Otto Work Optimizer")
    # Otto Input button
    input_button = tk.Button(rootHub, text="Input", command=lambda:subprocess.Popen(['python', str(BASE_DIR / 'scripts' / 'OttoInput.py')]))
    input_button.grid(row=0,column=0,pady=5,padx=5)
    # Otto List button
    input_button = tk.Button(rootHub, text="List", command=lambda:subprocess.Popen(['python', str(BASE_DIR / 'scripts' / 'OttoList.py')]))
    input_button.grid(row=0,column=1,pady=5,padx=5)
    # Otto Math button
    input_button = tk.Button(rootHub, text="Math", command=lambda:subprocess.Popen(['python', str(BASE_DIR / 'scripts' / 'OttoMath.py')]))
    input_button.grid(row=0,column=2,pady=5,padx=5)
    # Otto Note button
    input_button = tk.Button(rootHub, text="Notes", command=lambda:subprocess.Popen(['python', str(BASE_DIR / 'scripts' / 'OttoNote.py')]))
    input_button.grid(row=1,column=0,pady=5,padx=5)
    # Otto Overwrite button
    input_button = tk.Button(rootHub, text="Overwrite", command=lambda:subprocess.Popen(['python', str(BASE_DIR / 'scripts' / 'OttoOverwrite.py')]))
    input_button.grid(row=1,column=1,pady=5,padx=5)
    # Otto Remind button
    input_button = tk.Button(rootHub, text="Remind", command=lambda:subprocess.Popen(['python', str(BASE_DIR / 'scripts' / 'OttoRemind.py')]))
    input_button.grid(row=1,column=2,pady=5,padx=5)
    # Otto Sort button
    input_button = tk.Button(rootHub, text="Sort", command=lambda:subprocess.Popen(['python', str(BASE_DIR / 'scripts' / 'OttoSort.py')]))
    input_button.grid(row=2,column=1,pady=5,padx=5)
    # Hour pass button
    toggle_button = tk.Button(rootHub,text="OttoHour OFF",command=toggle_hourpass)
    toggle_button.grid(row=2,column=2,pady=5,padx=5)
    # About button
    input_button = tk.Button(rootHub, text="About", command=about_otto)
    input_button.grid(row=3,column=1,pady=10,padx=10)
    # Main loop
    rootHub.mainloop()
create_window()
