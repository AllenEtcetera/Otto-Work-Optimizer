import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import pyautogui
from pynput import keyboard

# Get the user inputs
def get_inputs():
    inputs = [entry.get() for entry in entry_list]
    special_keys = [combo.get() for combo in combo_list]
    repeats = repeat_var.get()
    for i, (user_input, special_key) in enumerate(zip(inputs, special_keys), start=1):
        print(f"Input {i}: {user_input}")
        print(f"Special Key {i}: {special_key}")
    print(f"Repetitions: {repeats}")
    # Hotkey
    hotkey = simpledialog.askstring("Hotkey", "Enter the hotkey to start the repetition")
    if hotkey:
        messagebox.showinfo("Hotkey Set", f"Press '{hotkey}' to start the repetition.")
        start_key_listener(hotkey, inputs, special_keys, int(repeats))

# Activate repetition
def repeat_inputs(inputs, special_keys, repeats):
    for _ in range(repeats):
        for user_input, special_key in zip(inputs, special_keys):
            if user_input:  # Check if user_input is not blank
                pyautogui.typewrite(user_input)
            if special_key:  # Check if special_key is not blank
                pyautogui.press(special_key)

# Add input fields
def add_input_field():
    if len(entry_list) < 10:
        new_entry = tk.Entry(rootInput)
        new_combo = ttk.Combobox(rootInput, values=special_keys_list, width=15)
        new_entry.bind("<Key>")
        new_entry.pack(pady=2)
        new_combo.pack(pady=2)
        entry_list.append(new_entry)
        combo_list.append(new_combo)
    else:
        add_button.destroy() # Remove button if 10 fields

# Start key listener
def start_key_listener(hotkey, inputs, special_keys, repeats):
    def on_key_press(key):
        try:
            if key.char == hotkey:  # Characters
                repeat_inputs(inputs, special_keys, repeats)
                return False  # Stop listener
        except AttributeError:
            if key.name == hotkey:  # Special keys
                repeat_inputs(inputs, special_keys, repeats)
                return False  # Stop listener
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()

# Function to reset the window
def reset_window():
    global rootInput
    rootInput.destroy()
    create_window()

# Make window
def create_window():
    # Global for inter-functional access
    global rootInput, entry_list, combo_list, repeat_var, special_keys_list, add_button
    # Window w/ title
    rootInput = tk.Tk()
    rootInput.title("Otto Input")
    entry_list = []
    combo_list = []
    special_keys_list = ['space', 'home', 'backspace', 'delete', 'enter', 'shift', 'ctrl', 'alt', 'tab', 'esc', 'up','down']
    # Labels and entries
    repeat_var = tk.StringVar(value="01")
    repeat_label = tk.Label(rootInput, text="Repetitions:")
    repeat_combo = ttk.Combobox(rootInput, textvariable=repeat_var, values=[f"{i:02}" for i in range(1, 1001)], width=5)
    repeat_label.pack(side="top")
    repeat_combo.pack(side="top")
    # Add input button
    add_button = tk.Button(rootInput, text="Add Input Field", command=add_input_field)
    add_button.pack(pady=5,side="top")
    # Submit button
    submit_button = tk.Button(rootInput, text="Submit", command=get_inputs)
    submit_button.pack(pady=10,side="bottom")
    # Reset button
    reset_button = tk.Button(rootInput, text="Reset", command=reset_window)
    reset_button.pack(pady=5,side="bottom")
    # Main loop
    rootInput.mainloop()

create_window()