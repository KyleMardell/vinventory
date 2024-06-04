from sheets_utils import *
from utils import *
from input_validation import get_integer_input, get_list_input
from prettytable import PrettyTable


def stock_menu():
    """
    Displays stock menu and runs menu option functions.
    """
    print("- Current Stock Menu -\n")
    print("Please select one of the following options:")
    print("1 - All Stock")
    print("2 - Find By ID")
    print("3 - Search Stock")

    while True:
        selected_option = get_integer_input("\nSelect an option (1-3, 0 to quit): ")

        match selected_option:
            case 0:
                clear_terminal()
                quit()
            case 1:
                clear_terminal()
                print("- All Stock selected -")
                print("Retrieving vehicle information...")
                display_sheet_table("stock", 9)
                break
            case 2:
                clear_terminal()
                print("- Find By ID selected -")
                print("Retrieving vehicle information...")
                find_car_by_id("stock")
                break
            case 3:
                clear_terminal()
                print("- Search Stock selected -")
                print("Retrieving vehicle information...")
                search_car_by_criteria()
                break
            case _:
                print("Please enter a valid number.")

    return_to_main_menu()


def sales_menu():
    """
    Displays Sales Menu
    """
    print("- Sales Reports -\n")
    print("Choose one of the following options:")
    print("1 - Current Month: Sales List")
    print("2 - Current Month: sales Report")
    print("3 - Sales History: Sales Lists")
    print("4 - Sales History: Sales Reports")

    while True:
        selected_option = get_integer_input("\nSelect an option (1-4, 0 to quit): ")

        match (selected_option):
            case 0:
                clear_terminal()
                quit()
            case 1:
                clear_terminal()
                print("- Current Month: Sales List -")
                current_sheet_name = get_current_sales_sheet_name()
                display_sheet_table(current_sheet_name, 12)
                break
            case 2:
                clear_terminal()
                print("- Current Month: Sales Report -")
                current_sheet_name = get_current_sales_sheet_name()
                generate_sales_report(current_sheet_name)
                break
            case 3:
                clear_terminal()
                print("- Sales History: Sales Lists -")
                print("Enter a year and month to display past sales data list.")
                sheet_name = create_sheet_name()
                clear_terminal()
                print(f"Searching for sheet name: {sheet_name}...")
                display_sheet_table(sheet_name, 11)
                break
            case 4:
                clear_terminal()
                print("- Sales History: Sales Reports -")
                print("Enter a year and month to display past sales data list.")
                sheet_name = create_sheet_name()
                clear_terminal()
                print(f"Searching for sheet name: {sheet_name}...")
                generate_sales_report(sheet_name)
                break
            case _:
                print("Not a valid entry. Please try again.")

    return_to_main_menu()


def deliveries_menu():
    """
    Displays deliveries options
    """
    print("- Deliveries Options -\n")
    print("Please select one of the following options:")
    print("1 - Full Delivery Report")
    print("2 - Requested Deliveries")
    print("3 - Scheduled Deliveries")
    print("4 - Completed Deliveries")
    print("5 - Create Delivery Request (Car ID Required)")

    while True:
        selected_option = get_integer_input("\nSelect an option (1-5, 0 to quit): ")

        match selected_option:
            case 0:
                clear_terminal()
                quit()
            case 1:
                clear_terminal()
                print("- Full Delivery Report -")
                display_deliveries_table()
                break
            case 2:
                clear_terminal()
                print("- Requested Deliveries -")
                display_deliveries_table(["requested"])
                break
            case 3:
                clear_terminal()
                print("- Scheduled Deliveries -")
                display_deliveries_table(["scheduled"])
                break
            case 4:
                clear_terminal()
                print("- Completed Deliveries -")
                display_deliveries_table(["delivered"])
                break
            case 5:
                clear_terminal()
                print("- Creating Delivery Request -")
                car_to_deliver = find_car_by_id("stock")
                get_continue(clear_terminal, return_to_main_menu)
                car_to_deliver.request_delivery()
                break
            case _:
                print("Not a valid entry, please try again.")

    return_to_main_menu()


def art():
    art = ['    .---------------.',
           '   /                 \\      - KM Car Sales - ',
           ' O/_____/________/____\O      Leeds',
           ' /__________+__________\\      Liverpool',
           '/    (#############)   \\      Manchester',
           '|[**](#############)[**]|     Preston',
           '\_______________________/     York',
           '|_""__|_,------,__|__""_|',
           "|_|     '.VinV.'      |_|  www.kmcarsales.co.uk", '']

    for line in art:
        print(line)


def main_menu():
    """
    Display welcome message and menu options
    """
    clear_terminal()
    print("- Welcome to VinVentory car management system -\n")
    art()
    print("Please select one of the following options:")
    print("1 - Current Stock")
    print("2 - Add/Edit Vehicle Info")
    print("3 - Sales Reports")
    print("4 - Deliveries")

    while True:
        selected_option = get_integer_input("\nSelect an option (1-4, 0 to quit): ")

        match selected_option:
            case 0:
                clear_terminal()
                quit()
            case 1:
                clear_terminal()
                stock_menu()
                break
            case 2:
                clear_terminal()
                print("Add/Edit Vehicle Info")
                new_car = get_new_car_details()
                add_car_to_stock(new_car)
                break
            case 3:
                clear_terminal()
                sales_menu()
                break
            case 4:
                clear_terminal()
                deliveries_menu()
                break
            case _:
                print("Not a valid entry, please try again.")


def return_to_main_menu():
    """
    Returns to main menu or quits on user input.
    """
    while True:
        answer = input(
            'Type "m" to return to the menu or "0" to quit.').lower()
        if answer == "0":
            clear_terminal()
            quit()
        elif answer == "m":
            clear_terminal()
            main_menu()
            return
        else:
            print("Not a valid input. Please try again.")
