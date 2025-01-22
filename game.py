"""
File containing game logic
"""

import os
import sys
import platform
from termcolor import colored


def clear_screen():
    """
    Clear console screen
    """
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def rainbow_text(text):
    """
    Generate rainobw text
    """
    rainbow_colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    colored_text = ""
    color_index = 0
    for char in text:
        colored_text += colored(char, rainbow_colors[color_index])
        color_index = (color_index + 1) % len(rainbow_colors)
    return colored_text


def ask_for_another_game():
    """
    Ask user for another game
    """
    while True:
        user_choice = input(
            colored(
                "Do you want to play another game. Press 'y' to play another game or press 'n' to exit : ",
                "yellow",
            )
        )
        if str(user_choice) and (
            str(user_choice).lower() != "y" or str(user_choice).lower() != "n"
        ):
            if str(user_choice) == "y":
                clear_screen()
                from main import main

                return main()
            if str(user_choice) == "n":
                return sys.exit(0)
        print(colored("Invalid Input", "red"))


def display_loose(word):
    """
    Display Loose message and prompt if user wants to quit or play another game
    """
    clear_screen()
    print(
        colored(
            "=======================================================================================",
            "red",
        )
    )
    print(
        colored(
            """
                    __   __            _                         
                    \ \ / /__  _   _  | |    ___   ___  ___  ___ 
                     \ V / _ \| | | | | |   / _ \ / _ \/ __|/ _ /
                      | | (_) | |_| | | |__| (_) | (_) \__ \  __/
                      |_|\___/ \__,_| |_____\___/ \___/|___/\___|
         """,
            "red",
        )
    )
    print(
        colored(
            "=======================================================================================",
            "red",
        )
    )
    print(colored(f"Correct word is : '{word}'", "green"))
    ask_for_another_game()


def display_won():
    """
    Display Win message and prompt if user wants to quit or play another game
    """
    clear_screen()
    print(
        rainbow_text(
            "======================================================================================="
        )
    )
    print(
        rainbow_text(
            """
                    __   __           __        __
                    \ \ / /__  _   _  \ \      / /__  _ __  
                     \ V / _ \| | | |  \ \ /\ / / _ \| '_ \ 
                      | | (_) | |_| |   \ V  V / (_) | | | |
                      |_|\___/ \__,_|    \_/\_/ \___/|_| |_|
        """
        )
    )
    print(
        rainbow_text(
            "======================================================================================="
        )
    )
    ask_for_another_game()


def verify_won(word, gussed_characters):
    """
    Verify if user already won
    """
    word = list(set(list(word)))
    word.sort(key=str.lower)
    gussed_characters = list(gussed_characters)
    gussed_characters.sort(key=str.lower)
    if word == gussed_characters:
        return True
    return False


def verify_user_guess(user_guess, gussed_characters, word, tries):
    """
    Verify user made guess
    """
    if user_guess in gussed_characters:
        clear_screen()
        display_stats(word, gussed_characters, tries)
        print(colored("Character already been gussed", "red"))
    elif user_guess in list(word):
        gussed_characters.add(user_guess)
        clear_screen()
        display_stats(word, gussed_characters, tries)
        print(colored(f"'{user_guess}' is a correct guess.", "green"))
    else:
        clear_screen()
        display_stats(word, gussed_characters, tries)
        print(colored("Your guess is wrong, Try again.", "red"))
    return gussed_characters


def ask_user():
    """
    Ask user to guess the character in the word
    """
    user_guess = input("Please guess the character in the word : ")
    if user_guess.isdigit() or not str(user_guess) or len(user_guess) != 1:
        print(colored("Invalid character", "red"))
        return ask_user()
    return user_guess


def gen_placeholder_for_word(word, gussed_characters):
    """
    Display the representative string for the word
    """
    rep = []
    for char in word:
        if char in gussed_characters:
            rep.append(char)
            continue
        rep.append("-")
    return "".join(rep)


def display_stats(word, gussed_characters, tries):
    """
    Display stats for user
    """
    word_representation = gen_placeholder_for_word(word, gussed_characters)
    stats_string = f"Word size : {len(word)}          {word_representation}          Remaining Tries : {tries}"
    total_display_length = len(stats_string) + 10
    calc_top_half = int((total_display_length - 3) / 2)
    top_half = "=".join(["="] * calc_top_half)
    calc_bottom_half = int(calc_top_half * 2 + 3)
    bottom = "=".join(["="] * calc_bottom_half)
    calc_center = int((total_display_length - len(stats_string)))
    centerc = " ".join([" "] * calc_center)
    print(colored(f"{top_half.replace("="," ")}Hangman game", "green"))
    print(colored(f"{top_half} Stats {top_half}", "yellow"))
    print()
    print(colored(f"{centerc}{stats_string}", "green"))
    print()
    print(colored(bottom, "yellow"))


def play_game(word):
    """
    Game logic goes here
    """
    gussed_characters = set()
    won = False
    tries = len(word) + 2
    clear_screen()
    display_stats(word, gussed_characters, tries)
    while tries > 0 and not won:
        user_guess = ask_user()
        tries -= 1
        gussed_characters = verify_user_guess(
            user_guess, gussed_characters, word, tries
        )
        won = verify_won(word, gussed_characters)
        if won:
            display_stats(word, gussed_characters, tries)
            print(colored(f"Correct word was {word}", "green"))
            display_won()
            return
    if tries <= 0:
        print(colored("you loose", "red"))
        display_loose(word)
