
#  MEMORY MATRIX - FINAL PROJECT

# 1️. Modules needed
    # random
    # time
    # tkinter

# 2️. Create a function named `show_symbol(x, y)`:
    # Show symbol on button click
    # If first click ➝ store position
    # If second click ➝ check match
        # If matched ➝ disable both
        # If not matched ➝ hide after delay
    # If all pairs matched ➝ call close_game()

# 3️. Create a function named `close_game()`:
    # Show success message
    # Destroy current game window
    # Call play_again()

# 4️. Create a function named `start_game()`:
    # Initialize variables
    # Create main game window (Tk)
    # Shuffle and assign 24 symbols (12 pairs)
    # Create 6x4 grid of buttons
    # Launch mainloop()

# 5️. Create a function named `play_again()`:
    # Ask user in terminal if they want to play again (y/n)
        # If yes ➝ restart game using start_game()
        # If no ➝ exit with a goodbye message

# 6️. Main program:
    # Show welcome message
    # Ask if user wants to play or quit
    # Start game based on input


import random
import time
from tkinter import Tk, Button, DISABLED, messagebox

def show_symbol(x, y):
    global first, previousx, previousy, matched_pairs
    
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previousx = x
        previousy = y
        first = False
    else:
        # Check if symbols match
        if buttons[previousx, previousy]['text'] == buttons[x, y]['text']:
            buttons[previousx, previousy]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
            matched_pairs += 1
            
            # Check if game is complete
            if matched_pairs == total_pairs:
                win.after(500, close_game)
        else:
            time.sleep(0.5)
            buttons[previousx, previousy]['text'] = ' '
            buttons[x, y]['text'] = ' '
        
        first = True

def close_game():
    messagebox.showinfo("Game Completed!", "Congratulations! You've matched all pairs!")
    win.destroy()
    play_again()

def start_game():
    global win, first, previousx, previousy, buttons, button_symbols, matched_pairs, total_pairs
    
    # Initialize game state
    first = True
    previousx = 0
    previousy = 0
    buttons = {}
    button_symbols = {}
    matched_pairs = 0
    
    # Create game window
    win = Tk()
    win.title('Memory Matrix')
    win.resizable(width=False, height=False)
    
    # Prepare symbols
    symbols = [u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
               u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728',
               u'\u2702', u'\u2705', u'\u2708', u'\u2709', u'\u270A', u'\u270B',
               u'\u270C', u'\u270F', u'\u2712', u'\u2714', u'\u2716', u'\u2728']
    
    total_pairs = len(symbols) // 2
    random.shuffle(symbols)
    
    # Create buttons with large symbols
    large_font = ('Arial', 24, 'bold')
    
    for x in range(6):
        for y in range(4):
            button = Button(
                command=lambda x=x, y=y: show_symbol(x, y),
                width=5, # size of gird
                height=4,
                font=large_font
            )
            button.grid(column=x, row=y)
            buttons[x, y] = button
            button_symbols[x, y] = symbols.pop()
    
    win.mainloop()

def play_again():
    while True:
        choice = input("\nWould you like to play again? (y/n): ").strip().lower()
        if choice == 'y':
            start_game()
            break
        elif choice == 'n':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Main game loop
print("Welcome to Memory Matrix!")
while True:
    choice = input("Press 'y' to play or 'q' to quit: ").strip().lower()
    
    if choice == 'y':
        start_game()
        break
    elif choice == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'q'.")
