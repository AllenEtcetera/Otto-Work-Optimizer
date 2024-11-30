import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
import pyautogui
from pathlib import Path

def open_overwrite_file():
    # Open file open thingy
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
    # Relay file path
    if file_path:
        print(f"File opened: {file_path}")
        # Put path text in entry box
        overwrite_entry.delete(0,tk.END)
        overwrite_entry.insert(0,file_path)
    else:
        print("No file selected")
def open_target_folder():
    file_path = filedialog.askdirectory(title="Select a folder")
    if file_path:
        print(f"Folder opened: {file_path}")
        folder_entry.delete(0,tk.END)
        folder_entry.insert(0,file_path)
    else:
        print("No folder selected")

def split_extension(overwrite_path):
    path = Path(overwrite_path)
    # Check if the path has a suffix
    if path.suffix:
        return path.suffix
    else:
        return "Dude, that's not a file path."

# Add data function
def folder_appender():
    folder_path = folder_entry.get()
    overwrite_path = overwrite_entry.get()
    if messagebox.askyesno("Otto Replace",f"Add data from {overwrite_path} onto all data in files from {folder_path}?"):
        file_suffix = split_extension(overwrite_path)
        # Read data to be appended
        with open(overwrite_path, 'r') as overwrite_file:
            new_data = overwrite_file.read()
        # Loop through all files in folder
        num = 0
        for filename in os.listdir(folder_path):
            if filename.endswith(file_suffix):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'a') as existing_file:
                    existing_file.write(new_data)
                num += 1
                print(f"File #{num} appended.")
        if num == 0:
            messagebox.showinfo("Otto Append Failed", "No files in folder with matching extension. No data has been altered.")
        messagebox.showinfo("Otto Append Complete", f"{num} file(s) in folder appended with new content.")
    else:
        messagebox.showinfo("Otto Append Failed", "Process canceled by user. No data has been altered.")

# Replace data function
def folder_replacer():
    folder_path = folder_entry.get()
    overwrite_path = overwrite_entry.get()
    if messagebox.askyesno("Otto Replace",f"Replace all data in {folder_path} with {overwrite_path}?"):
        file_suffix = split_extension(overwrite_path)
        # Loop through all files in folder
        num = 0
        for filename in os.listdir(folder_path):
            if filename.endswith(file_suffix):
                file_path = os.path.join(folder_path, filename)
                # Copy and replace
                shutil.copyfile(overwrite_path, file_path)
                num += 1
                print(f"File #{num} replaced.")
        if num == 0:
            messagebox.showinfo("Otto Replace Failed", "No files in folder with matching extension. No data has been altered.")
        messagebox.showinfo("Otto Replace Complete", f"{num} file(s) in folder replaced with new content.")
    else:
        messagebox.showinfo("Otto Replace Failed", "Process canceled by user. No data has been altered.")

# Function to reset the window
def reset_window():
    global rootOver
    rootOver.destroy()
    create_window()

# Make window
def create_window():
    # Global for inter-functional access
    global rootOver, overwrite_entry, folder_entry, file_entry
    # Window w/ title
    rootOver = tk.Tk()
    rootOver.title("Otto Overwrite")
    
    # Overwrite entry
    overwrite_label = tk.Label(rootOver, text="Data used:")
    overwrite_label.pack(pady=5)
    overwrite_button = tk.Button(rootOver, text="Browse...", command=open_overwrite_file)
    overwrite_button.pack(pady=5)
    overwrite_entry = tk.Entry(rootOver, width=50)
    overwrite_entry.pack(pady=5)
    # Folder entry
    folder_label = tk.Label(rootOver, text="Folder/file path to overwrite:")
    folder_label.pack(pady=5)
    folder_button = tk.Button(rootOver, text="Browse...", command=open_target_folder)
    folder_button.pack(pady=5)
    folder_entry = tk.Entry(rootOver, width=50)
    folder_entry.pack(pady=5)
    # Append Data button
    append_button = tk.Button(rootOver, text="Append Data", command=folder_appender)
    append_button.pack(pady=5)
    # Replace button
    replace_button = tk.Button(rootOver, text="Replace Data", command=folder_replacer)
    replace_button.pack(pady=5)
    # Reset button
    reset_button = tk.Button(rootOver, text="Reset", command=reset_window)
    reset_button.pack(pady=5,side="bottom")
    # Main loop
    rootOver.mainloop()

create_window()