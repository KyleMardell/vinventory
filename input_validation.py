import re  # regular expressions
from datetime import datetime


def get_integer_input(message):
    """
    Tries to convert user input to int
    Displays error message upon incorrect input
    Returns input as int if valid
    """
    while True:
        user_input = input(message + "\n")
        try:
            number = int(user_input)
            if number >= 0:
                return number
            else:
                print("Error: Must be a positive number.")
        except ValueError as e:
            print("Error: Not a valid number.")


def get_string_input(message):
    """
    Checks that the user entered characters only.
    No numbers or special characters.
    Returns input capitalized if true,
    otherwise repeatedly asks for correct input.
    """
    letters = r'^[a-z,A-Z]+$'
    while True:
        user_input = input(message + "\n")

        if re.fullmatch(letters, user_input):
            return user_input.capitalize()
        else:
            print("Input must not contain numbers, or special characters.")


def get_list_input(message):
    """
    Returns a list of strings from user input, separated by commas.
    """
    while True:
        user_input = input(message + "\n").lower()
        if user_input == "":
            print("Error: No value entered")
            continue
        input_list = [word.strip() for word in user_input.split(",")]
        return input_list


def get_site_input(current_site):
    """
    Gets the site input from the user, checks that the input is not
    the same as the current site, and exists in a list of all sites.
    """
    all_sites = ["liverpool", "leeds", "manchester", "preston", "york"]
    sites_string = f"Available sites: "
    for site in all_sites:
        if site not in current_site.lower():
            sites_string += site.capitalize() + " "
    while True:
        print(sites_string)
        site = input("Please enter a site: " + "\n").lower()
        if site in current_site.lower():
            print(f"Error: {site.capitalize()} is the current site.")
            print("Please enter a different site.")
            continue
        if site in all_sites:
            return site.capitalize()
        print("Site not found: please enter a valid site name.")


def get_continue(clear_terminal, return_to_main_menu):
    """
    Asks the user if they want to continue y/n input
    if 'n' the user is asked to return to menu or quit.
    """
    while True:
        answer = input("Would you like to continue (y/n)? " + "\n").lower()
        match answer:
            case "y":
                print("Continuing")
                clear_terminal()
                break
            case "n":
                print("Exiting")
                clear_terminal()
                return_to_main_menu()
                break
            case _:
                print("Not a valid entry, please try again.")


def get_year_input(message):
    """
    Returns a year as a 4 digit number if user input is in range
    """
    current_date = datetime.now()
    current_year = current_date.year
    while True:
        user_input = get_integer_input(message)
        if 1910 <= user_input <= current_year:
            return user_input
        else:
            print("Error: Date is out of range.")


def get_colour_input(message):
    """
    Returns a colour, checks is user input is
    in a list of common colours.
    If user input colour is not in the list,
    they are asked to confirm the input.
    """

    car_colours = ["black", "white", "grey", "silver", "red",
                   "pink", "orange", "blue", "purple", "green", "yellow"]

    while True:
        user_input = input(message + "\n").lower()

        if user_input in car_colours:
            return user_input.capitalize()
        else:
            print(f"{user_input}, is not in our common colour list.")
            answer = input("Would you like to continue? (y/n): " + "\n").lower()
            while True:
                if answer == "y":
                    return user_input.capitalize()
                elif answer == "n":
                    print("Cancelled.")
                    break
                else:
                    print("Not a valid entry, please try again.")
                    continue


def get_location_input(message):
    """
    Returns a location, confirms user input is a valid location.
    """
    locations = ["leeds", "liverpool", "manchester", "preston", "york"]

    while True:
        user_input = input(message + "\n").lower()

        if user_input in locations:
            return user_input.capitalize()
        else:
            print("Error: Location is invalid.")


def get_price_input(message, cost, repairs):
    """
    Returns the price of a vehicle.
    Checks the input is a whole number.
    """
    while True:
        user_input = get_integer_input(message)

        if user_input > (cost + repairs) * 1.2:
            return user_input
        elif cost + repairs <= user_input <= (cost + repairs) * 1.2:
            answer = input(f"The price of £{user_input} is less than " +
                           "20% calculated profit. " +
                           "Is this correct? (y/n): \n").lower()
            if answer == "y":
                return user_input
            else:
                print("Cancelled.")
                continue
        else:
            print("Error: Price must be larger than " +
                  "total cost including repairs.")
