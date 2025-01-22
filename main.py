#!/usr/bin/python3
"""
Hangman game starting point. 
"""
import json
import random
import sys
from termcolor import colored
from game import clear_screen, play_game


WORD_TYPES = {
    "random": 0,
    "fruits": 1,
    "vegetables": 2,
    "countries": 3,
    "cities": 4,
    "animals": 5,
}


def display_placeholder_for_word(word):
    """
    Display the representative string for the word
    """
    rep = []
    for _ in word:
        rep.append("-")
    print(colored(f"Chossen word is : {''.join(rep)}", "green"))


def get_predefined_words():
    """
    get all of the predefined words
    """
    try:
        with open("./Words.json", "r", encoding="utf-8") as words_json:
            words = json.load(words_json)
            return words
    except IOError:
        print(
            colored(
                "Error reading predefined words. Please try running program again or try reinstalling,",
                "red",
            )
        )
        sys.exit(1)


def get_random_word():
    """
    get random word
    """
    all_words = []
    predefined_words = get_predefined_words()
    for key in predefined_words:
        all_words.extend(predefined_words[key])
    random_word_index = random.randrange(0, len(all_words))
    return all_words[random_word_index]


def get_word_from_category(word_type):
    """
    get word based on user prefrences
    """
    predefined_words = get_predefined_words()
    user_prefered_category = predefined_words[word_type]
    random_word_index = random.randrange(0, len(user_prefered_category))
    return user_prefered_category[random_word_index]


def get_word(word_type):
    """
    get word for the game
    """
    word = ""
    if int(word_type):
        for key, value in WORD_TYPES.items():
            if int(word_type) == value:
                word_type = key
                break
        word = get_word_from_category(word_type)
    else:
        word = get_random_word()
    return word


def get_user_prefrences():
    """
    User Prefrences
    """
    user_prefrences = {}
    print(
        colored(
            "What type of words would like to guess, select from given prefrences.",
            "blue",
        )
    )
    for key, value in WORD_TYPES.items():
        print(colored(f" Press '{value}' for '{key.capitalize()}'", "yellow"))
    user_input = ""
    while not user_input.isdigit() or int(user_input) not in WORD_TYPES.values():
        user_input = input("Your Choice : ")
        print(colored("Invalid input", "red"))
    user_prefrences["word_type"] = user_input
    return user_prefrences


def display_welcome_greetings():
    """
    User Prefrences
    """
    print(
        colored(
            "==================================================================================",
            "green",
        )
    )
    print(
        colored(
            "----------------------------------Welcome to Hangman Game-------------------------",
            "yellow",
        )
    )
    print(
        colored(
            "==================================================================================",
            "green",
        )
    )


def main():
    """
    Main function
    """
    clear_screen()
    display_welcome_greetings()
    user_prefrences = get_user_prefrences()
    word = get_word(user_prefrences["word_type"])
    display_placeholder_for_word(word)
    play_game(word)
    sys.exit(1)


if __name__ == "__main__":
    main()
