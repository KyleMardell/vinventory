import re


def get_integer_input(message):
    """ 
    Tries to convert user input to int
    Displays error message upon incorrect input
    Returns input as int if valid
    """
    while True:
        user_input = input(message)
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid number.")


def get_list_input(message):
    """ 
    Returns a list of strings from user input, separated by commas.
    """
    while True:
        user_input = input(message).lower()
        if user_input == "":
            print("No value entered")
            continue
        input_list = [word.strip() for word in user_input.split(",")]
        return input_list
