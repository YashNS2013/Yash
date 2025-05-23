import tkinter as tk
from tkinter import messagebox
try:
    import androidhelper as sl4a
except ImportError:
    sl4a = None

class LKGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LKG Practice App")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Welcome to LKG Practice App!", font=("Arial", 16))
        self.label.pack(pady=10)

        self.alphabet_button = tk.Button(root, text="Practice Alphabets", command=self.practice_alphabets, font=("Arial", 14))
        self.alphabet_button.pack(pady=10)

        self.number_button = tk.Button(root, text="Practice Numbers", command=self.practice_numbers, font=("Arial", 14))
        self.number_button.pack(pady=10)

    def practice_alphabets(self):
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.quiz("Alphabet", alphabets)

    def practice_numbers(self):
        numbers = "1234567890"
        self.quiz("Number", numbers)

    def quiz(self, category, items):
        def check_answer():
            user_input = entry.get().strip()
            if user_input == current_item:
                messagebox.showinfo("Correct!", f"Good job! {current_item} is correct.")
                self.quiz(category, items)
            else:
                messagebox.showerror("Incorrect", f"Oops! The correct answer was {current_item}.")

        current_item = items[len(items) // 2]  # Pick a middle item for simplicity
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title(f"{category} Quiz")
        quiz_window.geometry("300x200")

        question_label = tk.Label(quiz_window, text=f"What is this {category.lower()}? {current_item}", font=("Arial", 14))
        question_label.pack(pady=10)

        entry = tk.Entry(quiz_window, font=("Arial", 14))
        entry.pack(pady=10)

        submit_button = tk.Button(quiz_window, text="Submit", command=check_answer, font=("Arial", 14))
        submit_button.pack(pady=10)

if __name__ == "__main__":
        if sl4a:
            droid = sl4a.Android()
            droid.makeToast("LKG Practice App is running!")
        else:
            print("SL4A not available. Running as a standard Tkinter app.")
    try:
        droid = sl4a.Android()
        droid.makeToast("LKG Practice App is running!")
    except ImportError:
        print("SL4A not available. Running as a standard Tkinter app.")
    if "linux" in root.tk.call("tk", "windowingsystem"):
        print("Running on Linux.")
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Application closed.")