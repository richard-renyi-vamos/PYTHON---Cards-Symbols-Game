import tkinter as tk
from tkinter import messagebox
import random

def card_clicked(card_num):
    global first_card_clicked, first_card_index, second_card_clicked, second_card_index
    global cards, matches

    if first_card_clicked is None:
        first_card_clicked = cards[card_num]
        first_card_index = card_num
        buttons[card_num].config(text=first_card_clicked, state='disabled')
    elif second_card_clicked is None:
        second_card_clicked = cards[card_num]
        second_card_index = card_num
        buttons[card_num].config(text=second_card_clicked, state='disabled')
        
        # Check for a match
        if first_card_clicked == second_card_clicked:
            matches += 1
            if matches == len(cards) // 2:
                messagebox.showinfo("Congratulations", "You've matched all the cards!")
        else:
            # If not a match, hide the cards after a short delay
            root.after(500, hide_cards)

def hide_cards():
    buttons[first_card_index].config(text='', state='active')
    buttons[second_card_index].config(text='', state='active')
    reset_globals()

def reset_globals():
    global first_card_clicked, first_card_index, second_card_clicked, second_card_index
    first_card_clicked = None
    first_card_index = None
    second_card_clicked = None
    second_card_index = None

root = tk.Tk()
root.title("Memory Card Game")

cards = ['A', 'B', 'C', 'A', 'B', 'C', 'D', 'D', 'E']  # Example cards - modify as needed
random.shuffle(cards)

first_card_clicked = None
first_card_index = None
second_card_clicked = None
second_card_index = None
matches = 0

buttons = []
for i in range(9):
    button = tk.Button(root, text='', width=5, height=2,
                       command=lambda idx=i: card_clicked(idx))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()
