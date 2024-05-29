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
        except ValueError as e:
            print("Not a valid number.")


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


def get_site_input():
    sites = ["liverpool", "leeds", "manchester", "preston", "york"]
    sites_string = f"Available sites: "
    for site in sites:
        sites_string += site + " "
    while True:
        print(sites_string)
        site = input("Please enter a site: ").lower()
        if site in sites:
            print(site)
            return site
        print("Site not found: please enter a valid site name.")
