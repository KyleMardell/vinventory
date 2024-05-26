import re

def get_integer_input(message):
    while True:
        user_input = input(message)
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid number.")

def get_list_input(message):
    user_input = input(message).lower()
    input_list = [word.strip() for word in user_input.split(",")]
    print(input_list)
    return input_list