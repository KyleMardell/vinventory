import re

def get_integer_input(message):
    while True:
        user_input = input(message)
        try:
                return int(user_input)
        except ValueError:
            print("Please enter a valid number.")
