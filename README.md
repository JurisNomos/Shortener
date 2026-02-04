# Guessing
This is a simple console-based game built with Python. The program generates a random number within a custom range defined by the user, the user must guess what it is. The game provides feedback ("Too High" or "Too Low") to help guide the user to the correct answer.

I built this project to practice Python flow control (loops and conditionals), function and user input handling.

## Features
- **Randomized Logic:** Every game generates a new random number.
- **Input Validation:** Prevents the game from crashing if non-numeric data is entered.
- **Score Tracking:** Tells the user how many attempts it took to guess correctly.
- **Replayability:** Asks the user if they want to play again after finishing.

## How to Run
1. Ensure you have Python installed.
2. Download or clone this repository.
3. Open your terminal or command prompt.
4. Navigate to the project folder.
5. Run the game:
   ```bash
   python main.py
   ```

## Example Run
```text
Welcome Guessing!

Enter the lower bound: 1
Enter the upper bound: 5
You can attempts 5 times

Guessing number (1 ~ 5): 6
Invalid input, try again

Guessing number (1 ~ 5): #
Invalid input, please enter a valid number

Guessing number (1 ~ 5): 5
Too high

Guessing number (1 ~ 5): 4
Correct, you guessed the 4 in 2 attempts
Do you went to play again? (Yes / No): no
```