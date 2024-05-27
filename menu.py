from sheets_utils import *
from utils import *
from input_validation import get_integer_input, get_list_input
from car import create_car_instances
from prettytable import PrettyTable


def stock_menu():
    """ 
    Displays stock menu and runs menu option functions.
    """
    print("Current Stock Menu")
    print("Please select one of the following options (1-3)")
    print("1 - All Stock")
    print("2 - Find By ID")
    print("3 - Search Stock")

    while True:
        selected_option = get_integer_input("Select an option (1-3): ")

        match selected_option:
            case 1:
                clear_terminal()
                print("Retrieving current stock sheet...")
                display_sheet_table("stock", 9)
                break
            case 2:
                clear_terminal()
                print("Find By ID selected...")
                find_car_by_id()
                break
            case 3:
                clear_terminal()
                print("Search Stock selected...")
                search_car_by_criteria()
                break
            case _:
                print("Please enter a valid number.")

    return_to_main_menu()

def sales_menu():
    """ 
    Displays Sales Menu
    """
    print("Sales Reports")
    print("Choose one of the following options (1-2)")
    print("1 - Current Month: Sales List")
    print("2 - Current Month: sales Report")
    print("3 - Sales History: Sales Lists")
    print("4 - Sales History: Sales Reports")

    while True:
        selected_option = get_integer_input("Select an option (1 - 4): ")
        
        match (selected_option):
            case 1:
                clear_terminal()
                print("Current Month: Sales List")
                current_sheet_name = get_current_sales_sheet_name()
                display_sheet_table(current_sheet_name, 12)
                break
            case 2:
                clear_terminal()
                print("Current Month: Sales Report")
                current_sheet_name = get_current_sales_sheet_name()
                generate_sales_report(current_sheet_name)
                break
            case 3:
                clear_terminal()
                print("Sales History: Sales Lists")
                print("Enter a year and month to display past sales data list")
                sheet_name = create_sheet_name()
                clear_terminal()
                print(f"Searching for sheet name: {sheet_name}...")
                display_sheet_table(sheet_name, 11)
                break
            case 4:
                clear_terminal()
                print("Sales History: Sales Reports")
                print("Enter a year and month to display past sales data list")
                sheet_name = create_sheet_name()
                clear_terminal()
                print(f"Searching for sheet name: {sheet_name}...")
                generate_sales_report(sheet_name)
                break
            case _:
                print("Not a valid entry. Please try again.")

    return_to_main_menu()


def main_menu():
    """ 
    Display welcome message and menu options
    """
    print("Welcome to VinVentory, used car management system.")
    print("Please select one of the following options (1-4)")
    print("1 - Current Stock")
    print("2 - Add/Edit Vehicle Info")
    print("3 - Sales Reports")
    print("4 - Delivery Reports")

    while True:
        selected_option = get_integer_input("Select an option (1-4): ")

        match selected_option:
            case 1:
                clear_terminal()
                stock_menu()
                break
            case 2:
                clear_terminal()
                print("Add/Edit Vehicle Info")
                break
            case 3:
                clear_terminal()
                print("Sales Reports")
                sales_menu()
                break
            case 4:
                clear_terminal()
                print("Delivery Reports")
                break
            case _:
                print("Not a valid entry, please try again.")


def return_to_main_menu():
    """ 
    Returns to main menu or quits on user input.
    """
    while True:
        answer = input(
            'Type "m" to return to the menu or "q" to quit.').lower()
        if answer == "q":
            clear_terminal()
            quit()
        elif answer == "m":
            clear_terminal()
            main_menu()
            return
        else:
            print("Not a valid input. Please try again.")
