import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")
button1 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)
button2 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)
button3 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)
button4 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)
button5 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)
button6 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)
button7 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)
button8 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)
button9 = tk.Button(window, text="", font=('Arial', 20), width=5, height=2)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
def button_click(button):
    global player
    if button["text"] == "":
        if player == "X":
            button["text"] = "X"
            player = "O"
        else:
            button["text"] = "O"
            player = "X"
button1.config(command=lambda: button_click(button1))
button2.config(command=lambda: button_click(button2))
button3.config(command=lambda: button_click(button3))
button4.config(command=lambda: button_click(button4))
button5.config(command=lambda: button_click(button5))
button6.config(command=lambda: button_click(button6))
button7.config(command=lambda: button_click(button7))
button8.config(command=lambda: button_click(button8))
button9.config(command=lambda: button_click(button9))
player = "X"
player_label = tk.Label(window, text="Player " + player + "'s turn", font=('Arial', 16))
player_label.grid(row=3, columnspan=3)
def check_winner():
    global winner
    if (button1["text"] == button2["text"] == button3["text"] != "") or \
            (button4["text"] == button5["text"] == button6["text"] != "") or \
            (button7["text"] == button8["text"] == button9["text"] != "") or \
            (button1["text"] == button4["text"] == button7["text"] != "") or \
            (button2["text"] == button5["text"] == button8["text"] != "") or \
            (button3["text"] == button6["text"] == button9["text"] != "") or \
            (button1["text"] == button5["text"] == button9["text"] != "") or \
            (button3["text"] == button5["text"] == button7["text"] != ""):
        winner = player
        player_label.config(text="Player " + winner + " wins!")
        disable_buttons()
    elif "" not in [button1["text"], button2["text"], button3["text"], button4["text"], button5["text"],
                    button6["text"], button7["text"], button8["text"], button9["text"]]:
        player_label.config(text="It's a tie!")
        disable_buttons()
def disable_buttons():
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
        button.config(state="disabled")
def button_click(button):
    global player
    if button["text"] == "":
        if player == "X":
            button["text"] = "X"
            player = "O"
        else:
            button["text"] = "O"
            player = "X"
        check_winner()
window.mainloop()
