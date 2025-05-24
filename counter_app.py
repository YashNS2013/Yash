import tkinter as tk
from tkinter import font

# Functions
def increment():
    try:
        value = int(number_label["text"])
        number_label.config(text=str(value + 1))
    except ValueError:
        number_label.config(text="0")

def decrement():
    try:
        value = int(number_label["text"])
        if value > 0:  # Optional: prevent negative numbers
            number_label.config(text=str(value - 1))
    except ValueError:
        number_label.config(text="0")

def reset():
    number_label.config(text="0")

# Root window setup
root = tk.Tk()
root.title("COUNTER")
root.geometry("300x250")
root.resizable(True, True)

# Header
symbol_font = font.Font(size=36, weight="bold", family="Arial")
header = tk.Label(root, text="🔢 COUNTER", font=symbol_font, pady=10)
header.pack()

# Number display
number_font = font.Font(size=36, weight="bold")
number_label = tk.Label(root, text="0", font=number_font, pady=10)
number_label.pack()

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Increment button
plus_button = tk.Button(
    button_frame, text="+", command=increment, width=5, height=2,
    bg="blue", fg="white", font=("Arial", 18)
)
plus_button.grid(row=0, column=0, padx=10)

# Decrement button
minus_button = tk.Button(
    button_frame, text="-", command=decrement, width=5, height=2,
    bg="blue", fg="white", font=("Arial", 18)
)
minus_button.grid(row=0, column=1, padx=10)

# Reset button
reset_button = tk.Button(
    button_frame, text="Reset", command=reset, width=12, height=2,
    bg="gray", fg="white", font=("Arial", 12)
)
reset_button.grid(row=1, column=0, columnspan=2, pady=10)

# Keyboard bindings
root.bind("<Up>", lambda event: increment())
root.bind("<Down>", lambda event: decrement())

# Run the app
root.mainloop()
