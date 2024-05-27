import re

def get_integer_input(message):
    while True:
        user_input = input(message)
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid number.")

def get_list_input(message):
    while True:
        user_input = input(message).lower()
        if user_input == "":
            print("No value entered")
            continue
        input_list = [word.strip() for word in user_input.split(",")]
        return input_list