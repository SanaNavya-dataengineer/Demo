import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("350x420")

player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

current_player = player1
current_symbol = "X"

board = [""] * 9


def check_winner():
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in wins:
        a, b, c = combo

        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Tie"

    return None


def button_click(index):
    global current_player, current_symbol

    if board[index] == "":
        board[index] = current_symbol
        buttons[index].config(text=current_symbol)

        winner = check_winner()

        if winner:
            if winner == "Tie":
                messagebox.showinfo(
                    "Game Over",
                    "It's a Tie!"
                )
            else:
                messagebox.showinfo(
                    "Game Over",
                    f"{current_player} Wins!"
                )

            reset_game()
            return

        if current_player == player1:
            current_player = player2
            current_symbol = "O"
        else:
            current_player = player1
            current_symbol = "X"

        player_label.config(
            text=f"{current_player}'s Turn ({current_symbol})"
        )


def reset_game():
    global current_player, current_symbol

    current_player = player1
    current_symbol = "X"

    for i in range(9):
        board[i] = ""
        buttons[i].config(text="")

    player_label.config(
        text=f"{player1}'s Turn (X)"
    )


player_label = tk.Label(
    root,
    text=f"{player1}'s Turn (X)",
    font=("Arial", 16, "bold")
)
player_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []

for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    btn.grid(
        row=i // 3,
        column=i % 3,
        padx=2,
        pady=2
    )

    buttons.append(btn)

reset_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game
)
reset_btn.pack(pady=15)

root.mainloop()