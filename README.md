![Screenshot From 2025-01-31 18-00-16](https://github.com/user-attachments/assets/8d002f3e-d7f8-41ae-9488-890676a781d6)


# Hangman Game

Welcome to the Hangman game! This is a fun and interactive word-guessing game where you have to guess a secret word based on category selections. As you guess, you’ll have limited attempts before the game ends. Can you guess the word before you run out of tries? Let’s find out!

## Features

- **Multiple Word Categories**: Choose from different categories of words like Fruits, Vegetables, Countries, Cities, and Animals.
- **Random Word Option**: If you're feeling adventurous, you can let the game pick a random category for you.
- **Interactive Gameplay**: You’ll get to know your stats, including the current word length and remaining tries.
- **Guess the Word**: You are given a number of tries to guess the word, one letter at a time.

## Game Flow

1. When you start the game, you'll be asked to choose a category from the following options:
    - **0**: Random
    - **1**: Fruits
    - **2**: Vegetables
    - **3**: Countries
    - **4**: Cities
    - **5**: Animals

2. Once you make your selection, the game will display a word with the number of characters as underscores (e.g., _ _ _ _).

3. You will have 6 chances to guess the word by typing in a letter. Each incorrect guess will reduce your remaining tries.

4. As you guess letters, the game will update and show the current state of the word (with correct guesses filled in).

5. You win if you guess the word within the allowed number of tries. If you run out of tries, the game will end.

## Example Gameplay

```
==================================================================================
----------------------------------Welcome to Hangman Game-------------------------
==================================================================================
What type of words would you like to guess? Select from the given preferences.
Press '0' for 'Random'
Press '1' for 'Fruits'
Press '2' for 'Vegetables'
Press '3' for 'Countries'
Press '4' for 'Cities'
Press '5' for 'Animals'
Your Choice : 1

============================================================ Stats =============================================================

                   Word size : 4          ----          Remaining Tries : 6

=================================================================================================================================
Please guess the character in the word : 
```
## How to Run the Game

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/Shaheryarkhalid/Hangman
    ```
2. Navigate to the project folder:
    ```
    cd Hangman
    ```
3. Run the game:
    ```
    python main.py
    ```
or simply 
    ```
    ./main.py
    ```
## Requirements
    Python 3.x
## License
    This project is licensed under the MIT License – see the LICENSE file for details.
