# Memory Matrix 🧠

A simple and fun memory matching game built with Python and Tkinter. Test your memory by finding all the matching pairs of symbols on a 6x4 grid! This project is a classic concentration game where players flip over cards to find matching symbols.

---

## Gameplay 🎮

The game starts by presenting a grid of hidden symbols. The player clicks on two cards (buttons) to reveal their underlying symbols:

1.  Click a card to reveal its symbol.
2.  Click a second card to reveal its symbol.
    * If the symbols on the two cards **match**, they will remain visible, and those cards will be disabled. You can then continue to find other pairs.
    * If the symbols **do not match**, they will be hidden again after a short delay (0.5 seconds), allowing you to try again.

The objective is to find and reveal all 12 matching pairs on the board. Once all pairs are found, a congratulatory message will appear.

---

## Features ✨

-   **Graphical User Interface (GUI):** Built using Python's standard `tkinter` library, making it accessible without extra installations.
-   **Symbol Matching:** Classic memory game mechanics with engaging symbol-based matching.
-   **Grid Size:** A 6x4 grid, providing 24 cards with 12 unique pairs of symbols to find.
-   **Visual Feedback:**
    -   Matched pairs stay revealed.
    -   Unmatched pairs flip back after a brief pause.
-   **Game Completion:** A clear message box congratulates the player upon successfully matching all pairs.
-   **Play Again Option:** After a game is completed, or initially, the player is prompted via the command line to play another round or quit.
-   **Randomized Layout:** Symbols are shuffled randomly for each new game, ensuring a different experience every time.

---

## Requirements 🛠️

-   **Python 3.x**
-   **Tkinter:** This library is typically included with standard Python installations. No separate installation is usually required.

---

## How to Play / Run the Game 🚀

1.  **Get the code:**
    * Clone the repository:
        ```bash
        git clone [https://github.com/Najil-najil/Memory_Matrix.git](https://github.com/Najil-najil/Memory_Matrix.git)
        ```
    * Or, download the `main.py` file directly from the repository: [Najil-najil/Memory_Matrix/main.py](https://github.com/Najil-najil/Memory_Matrix/blob/main/main.py)

2.  **Navigate to the directory** where you saved/cloned the file:
    ```bash
    cd Memory_Matrix
    ```

3.  **Run the `main.py` script** using Python:
    ```bash
    python main.py
    ```

4.  **Starting the Game:**
    * You will first see a prompt in your **command line terminal**:
        ```
        Welcome to Memory Matrix!
        Press 'y' to play or 'q' to quit:
        ```
    * Type `y` and press Enter to start the game. The Memory Matrix game window will appear.
    * If you type `q` and press Enter, the program will exit.

5.  **Playing:**
    * Click on any two buttons in the game window to reveal their symbols.
    * Try to find all the matching pairs!

6.  **Play Again?**
    * After successfully completing a game, a message box will appear. After closing it, you will be prompted in the **command line terminal**:
        ```
        Would you like to play again? (y/n):
        ```
    * Type `y` to start a new game or `n` to quit.

---

## Code Overview 📄

The entire game logic is contained within the `main.py` file. It utilizes:
-   `tkinter` for creating and managing the graphical user interface (game window, buttons).
-   `random` for shuffling the symbols on the game board.
-   `time` for pausing briefly when non-matching cards are shown.

**Key Functions:**

-   `start_game()`: Initializes the game window, shuffles symbols, creates the grid of buttons, and resets game variables.
-   `show_symbol(x, y)`: Handles the logic when a card (button) at grid position `(x, y)` is clicked. It reveals the symbol, checks for matches with a previously clicked card, disables matched pairs, or hides symbols if they don't match.
-   `close_game()`: Displays the "Game Completed!" message box and calls `play_again()`.
-   `play_again()`: Manages the command-line prompt asking the user if they wish to play another round.
-   The script also includes a main execution block that initially prompts the user to start the game or quit via the command line.

---

Enjoy the game! 🎉
