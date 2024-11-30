import tkinter as tk
from tkinter import messagebox, ttk
import math

def solve():
    try:
        # Evaluate expression
        result = eval(exp_entry.get())
        history_text.config(state=tk.NORMAL)
        history_text.insert(tk.END, f"{exp_entry.get()} = {result}\n" )
        history_text.config(state=tk.DISABLED)
    except Exception as e:
        # Handle PEBKAC errors
        messagebox.showerror("Error",str(e))

def add_expression(op):
    exp_entry.insert(tk.END,op)

def show_help():
    help_text = (
        "With Otto Math, you can type the following:\n"
        "Add:           N + E\n"
        "Subtract:      N - E\n"
        "Multiply:      N * E\n"
        "Divide:        N / E\n"
        "Exponent:      N**E\n"
        "Modulo:        N % E\n"
        "Square Root:   math.sqrt(N)\n"
        "Remember PEMDAS. Replace N and E with actual numbers.\n\n"
        "Note: All expressions use the language of Python."
        )
    messagebox.showinfo("Help",help_text)

# Function to reset window
def reset_window():
    global rootMath
    rootMath.destroy()
    create_window()

# Create window
def create_window():
    global rootMath, exp_entry, history_text
    rootMath = tk.Tk()
    rootMath.title("Otto Math")

    # Expression entry
    exp_label = tk.Label(rootMath, text="Input:")
    exp_label.pack(pady=5)
    exp_entry = tk.Entry(rootMath, width=50)
    exp_entry.pack(pady=5)

    # History
    history_text = tk.Text(rootMath,height=10,width=50)
    history_text.config(state=tk.DISABLED)
    history_text.pack(pady=5,side="top")

    # Additional operation buttons
    button_frame = tk.Frame(rootMath)
    button_frame.pack(pady=5)
    sqrt_button = tk.Button(button_frame, text="Sq. Root", command=lambda: add_expression("math.sqrt("))
    sqrt_button.grid(row=0, column=0, padx=5)
    exp_button = tk.Button(button_frame, text="Exponent", command=lambda: add_expression("**"))
    exp_button.grid(row=0, column=1, padx=5)
    mod_button = tk.Button(button_frame, text="Modulo", command=lambda: add_expression("%"))
    mod_button.grid(row=0, column=2, padx=5)

    # Solve button
    solve_button = tk.Button(rootMath, text="Solve", command=solve)
    solve_button.pack(pady=5)

    # Help button
    help_button = tk.Button(rootMath, text="Help", command=show_help)
    help_button.pack(pady=5, side="right")

    # Reset button
    reset_button = tk.Button(rootMath, text="Reset", command=reset_window)
    reset_button.pack(pady=5)

    # Main loop
    rootMath.mainloop()

create_window()