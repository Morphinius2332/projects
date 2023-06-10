import random
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Define the options
options = ["rock", "paper", "scissors"]

# Define the function to handle user's choice
def play_game(user_choice):
    # Get computer's choice
    computer_choice = random.choice(options)
    computer_label.config(text=f"Computer chooses {computer_choice}.")

    # Determine the winner
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

# Create the user interface
label = tk.Label(root, text="Choose rock, paper, or scissors:")
label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack()

computer_label = tk.Label(root, text="")
computer_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
