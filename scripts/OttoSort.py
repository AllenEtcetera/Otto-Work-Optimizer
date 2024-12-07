import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
import pyautogui
from pathlib import Path
from collections import Counter

def open_file():
    # Open file open thingy
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
    # Relay file path
    if file_path:
        print(f"File opened: {file_path}")
        # Put path text in entry box
        file_entry.delete(0,tk.END)
        file_entry.insert(0,file_path)
    else:
        print("No file selected")

def open_target():
    # Open file open thingy
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
    # Relay file path
    if file_path:
        print(f"File opened: {file_path}")
        # Put path text in entry box
        target_entry.delete(0,tk.END)
        target_entry.insert(0,file_path)
    else:
        print("No file selected")

def data_sort_by_line():
    input_file = file_entry.get()
    output_file = target_entry.get()
    with open(input_file, 'r') as file:
        lines = file.readlines()
    sorted_lines = []
    for line in lines:
        words = line.split()
        word_counts = Counter(words)
        if sort_combo.get() == 'Alphabetical Ascending':
            words.sort()
            sorted_line = ' '.join(words)
            sorted_lines.append(f"{sorted_line}\n")
        elif sort_combo.get() == 'Alphabetical Descending':
            words.sort(reverse=True)
            sorted_line = ' '.join(words)
            sorted_lines.insert(0, f"{sorted_line}\n")
        elif sort_combo.get() == 'Length Ascending':
            words.sort(key=len)
            sorted_line = ' '.join(words)
            sorted_lines.append(f"{sorted_line}\n")
        elif sort_combo.get() == 'Length Descending':
            words.sort(key=len, reverse=True)
            sorted_line = ' '.join(words)
            sorted_lines.insert(0, f"{sorted_line}\n")
        elif sort_combo.get() == 'Frequency Ascending':
            sorted_words = sorted(word_counts.keys(), key=lambda word: word_counts[word])
            sorted_line = ' '.join(sorted_words)
            sorted_lines.append(f"{sorted_line}\n")
        elif sort_combo.get() == 'Frequency Descending':
            sorted_words = sorted(word_counts.keys(), key=lambda word: word_counts[word], reverse=True)
            sorted_line = ' '.join(sorted_words)
            sorted_lines.insert(0, f"{sorted_line}\n")
    with open(output_file, 'w') as file:
        file.writelines(sorted_lines)
    messagebox.showinfo("Otto Sort Complete", f"Sorted data will be found in {output_file}.")

def data_sort():
    input_file = file_entry.get()
    output_file = target_entry.get()
    with open(input_file, 'r') as file:
        lines = file.readlines()
    all_words = []
    for line in lines:
        words = line.split()
        all_words.extend(words)
        word_counts = Counter(all_words)
        if sort_combo.get() == 'Alphabetical Ascending':
            all_words.sort()
        elif sort_combo.get() == 'Alphabetical Descending':
            all_words.sort(reverse=True)
        elif sort_combo.get() == 'Length Ascending':
            all_words.sort(key=len)
        elif sort_combo.get() == 'Length Descending':
            all_words.sort(key=len, reverse=True)
        elif sort_combo.get() == 'Frequency Ascending':
            all_words = sorted(word_counts.keys(), key=lambda word: word_counts[word])
        elif sort_combo.get() == 'Frequency Descending':
            all_words = sorted(word_counts.keys(), key=lambda word: word_counts[word], reverse=True)
    with open(output_file, 'w') as file:
        file.write(' '.join(all_words) + '\n')
    messagebox.showinfo("Otto Sort Complete", f"Sorted data will be found in {output_file}.")

# Function to reset the window
def reset_window():
    global rootSort
    rootSort.destroy()
    create_window()

# Make window
def create_window():
    # Global for inter-functional access
    global rootSort, file_entry, target_entry, sort_combo
    # Window w/ title
    rootSort = tk.Tk()
    rootSort.title("Otto Sort")
    
    # File entry
    file_label = tk.Label(rootSort, text="File:")
    file_label.pack(pady=5)
    file_button = tk.Button(rootSort, text="Browse...", command=open_file)
    file_button.pack(pady=5)
    file_entry = tk.Entry(rootSort, width=50)
    file_entry.pack(pady=5)

    # Target file entry
    target_label = tk.Label(rootSort, text="Target file:")
    target_label.pack(pady=5)
    target_button = tk.Button(rootSort, text="Browse...", command=open_target)
    target_button.pack(pady=5)
    target_entry = tk.Entry(rootSort, width=50)
    target_entry.pack(pady=5)
    
    sort_types = ['Alphabetical Ascending', 'Alphabetical Descending', 'Length Ascending', 'Length Descending', 'Frequency Ascending', 'Frequency Descending']
    sort_label = tk.Label(rootSort, text="Sort data by:")
    sort_label.pack(pady=5)
    sort_combo = ttk.Combobox(rootSort, values=sort_types, width=50)
    sort_combo.pack(pady=5)

    # Sort button
    sort_button = tk.Button(rootSort, text="Sort Data", command=data_sort)
    sort_button.pack(pady=5)
    # Sort With Maintained Structure button
    sort_button = tk.Button(rootSort, text="Sort Data With Line Confinement", command=data_sort_by_line)
    sort_button.pack(pady=5)
    # Reset button
    reset_button = tk.Button(rootSort, text="Reset", command=reset_window)
    reset_button.pack(pady=5,side="bottom")
    # Main loop
    rootSort.mainloop()

create_window()