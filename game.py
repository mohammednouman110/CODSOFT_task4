import tkinter as tk
import random
from tkinter import messagebox

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    messagebox.showinfo(
        "Result",
        f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}"
    )

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")

tk.Label(root, text="Choose one", font=("Arial", 14)).pack(pady=10)

for choice in choices:
    tk.Button(
        root,
        text=choice,
        font=("Arial", 12),
        width=15,
        command=lambda c=choice: play(c)
    ).pack(pady=5)

root.mainloop()