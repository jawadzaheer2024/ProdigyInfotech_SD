import tkinter as tk
from tkinter import ttk, messagebox
import random


# Function to start a new game
def start_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    result_label.config(text="")


# Function to check the user's guess
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1

        if guess < random_number:
            result_label.config(text="Too low! Try again.")
        elif guess > random_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Congratulations! You've guessed it in {attempts} attempts.")
            guess_entry.config(state="disabled")
            guess_button.config(state="disabled")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


# Create the main window
root = tk.Tk()
root.title("Guessing Game")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Style configuration
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TEntry", font=("Helvetica", 12))

# Create and place the widgets
ttk.Label(root, text="Guess the number between 1 and 100:").pack(pady=20)
guess_entry = ttk.Entry(root, width=10, font=("Helvetica", 12))
guess_entry.pack(pady=5)

guess_button = ttk.Button(root, text="Submit Guess", command=check_guess)
guess_button.pack(pady=20)

result_label = ttk.Label(root, text="", background="#f0f0f0", font=("Helvetica", 12))
result_label.pack(pady=10)

ttk.Button(root, text="New Game", command=start_game).pack(pady=10)

# Start a new game
start_game()

# Run the application
root.mainloop()
