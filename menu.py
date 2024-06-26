from sheets_utils import *
from utils import *
from input_validation import get_integer_input, get_list_input
from prettytable import PrettyTable
from help import display_help
import os
import platform


def stock_menu():
    """
    Displays stock menu and runs menu option functions.
    """
    print("- Current Stock Menu -\n")
    print("Welcome to the stock menu.")
    print("Here you can view a list of all stock,")
    print("see a cars details by entering its internal ID number, or search")
    print("through all stock for cars with matching entered key words.\n")
    print("Please select one of the following options:")
    print("1 - View List of All Stock")
    print("2 - View Car Information (ID number required)")
    print("3 - Search Stock by Key Words")
    print("0 - Return to Main Menu")

    while True:
        selected_option = get_integer_input("\nSelect an option " +
                                            "(1-3, 0 to main menu/quit): ")
        clear_terminal()
        match selected_option:
            case 0:
                main_menu()
                break
            case 1:
                print("- All Stock selected -\n")
                print("Retrieving vehicle information...\n")
                display_sheet_table("stock", 7)
                break
            case 2:
                print("- View Car Information selected -\n")
                print("Retrieving vehicle information...\n")
                find_car_by_id("stock")
                break
            case 3:
                print("- Search Stock selected -\n")
                print("Here you can search for terms separated by commas.")
                print("E.g. Make (Citroen, BMW) or colour (blue, red),")
                print("or year (2012, 2018) to name a few.")
                print("All matching cars will be displayed in a list.\n")
                print("Retrieving vehicle information...\n")
                search_car_by_criteria()
                break
            case _:
                print("Not a valid entry. Please try again.\n")

    return_to_main_menu()


def edit_menu():
    """
    Displays edit menu
    """
    print("- Add/Edit Vehicle Information -\n")
    print("Welcome to the add/edit menu.")
    print("You can add a new car to stock,")
    print("edit a car currently in stock, sell a car,")
    print("create a delivery request or delete a cars details.\n")
    print("Choose one of the following options:")
    print("1 - Add a new car to the stock sheet")
    print("2 - Edit a car currently in stock (Car ID Required)")
    print("3 - Mark a car as sold (Car ID Required)")
    print("4 - Create delivery request (Car ID Required)")
    print("5 - Delete a car from the stock sheet (Car ID Required)")
    print("0 - Return to Main Menu")

    while True:
        selected_option = get_integer_input("\nSelect an option" +
                                            "(1-5, 0 to main menu/quit): ")
        clear_terminal()
        match (selected_option):
            case 0:
                main_menu()
                break
            case 1:
                print("- Add A New Car To The Stock Sheet -\n")
                print("You will be asked to enter details one at a time.")
                print("Please ensure all details are correct,")
                print("you will be asked to confirm before submitting.\n")
                new_car_details = get_new_car_details()
                add_car_to_sheet(new_car_details, "stock")
                break
            case 2:
                print("- Edit A Car Currently In Stock-\n")
                print("Here you can edit the details of a car in stock.")
                print("The car ID is required to find the car in the" +
                      "stock sheet.")
                print("Once a car has been found," +
                      "you can enter the name of an attribute to change it.")
                print("After all changes have been made, " +
                      "they can be confirmed and saved.\n")
                edit_car_in_stock()
                break
            case 3:
                print("- Sell a Car -\n")
                print("To mark a car a sold, enter the car ID number.")
                print("You will be asked to enter the sale amount, " +
                      "buyers name and phone number.")
                print("Once confirmed, the car will be removed from the " +
                      "stock sheet and the sales")
                print("information will be added to the current months " +
                      "sales sheet.")
                print("Note, any deliveries requested or scheduled for the " +
                      "car will remain.")
                current_sales_sheet = get_current_sales_sheet_name()
                sell_car(current_sales_sheet)
                break
            case 4:
                print("- Request A Delivery -\n")
                print("You can enter a cars ID number to request a delivery.")
                print("You will be asked to enter a delivery location and a " +
                      "request date will be automatically generated.\n")
                delivery_request()
                break
            case 5:
                print("- Delete A Car From The Stock Sheet -\n")
                print("WARNING - Once a car has been deleted, it cannot be " +
                      "recovered and must be input as a new entry.")
                print("You will be asked to enter the cars ID number and " +
                      "confirm to delete the car from stock.\n")
                delete_car_from_sheet("stock")
                break
            case _:
                print("Not a valid entry. Please try again.\n")

    return_to_main_menu()


def sales_menu():
    """
    Displays Sales Menu
    """
    print("- Sales Reports -\n")
    print("Welcome to the sales report menu.")
    print("From here you can view a list of all cars " +
          "sold in the current or a past month.")
    print("You can also generate a report of a months sales. " +
          "This will display information")
    print("such as, number of cars sold, total monthly profit, " +
          "average profit per car, etc.")
    print("When viewing sales history data, you must input the year " +
          "and month you wish to view.")
    print("Note, earliest sales data sheet is 2/2024 (m/yyyy).\n")
    print("Choose one of the following options:")
    print("1 - Current Month: Sales List")
    print("2 - Current Month: Sales Report")
    print("3 - Sales History: Sales Lists")
    print("4 - Sales History: Sales Reports")
    print("0 - Return to Main Menu")

    while True:
        selected_option = get_integer_input("\nSelect an option " +
                                            "(1-4, 0 to main menu/quit): ")
        clear_terminal()
        match (selected_option):
            case 0:
                main_menu()
                break
            case 1:
                print("- Current Month: Sales List -\n")
                current_sheet_name = get_current_sales_sheet_name()
                sheet_exists = display_sheet_table(current_sheet_name, 15)
                if not sheet_exists:
                    create_new_sales_sheet(current_sheet_name)
                break
            case 2:
                print("- Current Month: Sales Report -\n")
                current_sheet_name = get_current_sales_sheet_name()
                sheet_exists = generate_sales_report(current_sheet_name)
                if not sheet_exists:
                    create_new_sales_sheet(current_sheet_name)
                break
            case 3:
                print("- Sales History: Sales Lists -\n")
                print("Enter a year and month to display " +
                      "past sales data list.")
                sheet_name = create_sheet_name()
                clear_terminal()
                print(f"Searching for sheet name: {sheet_name}...")
                display_sheet_table(sheet_name, 15)
                break
            case 4:
                print("- Sales History: Sales Reports -\n")
                print("Enter a year and month to display " +
                      "past sales data report.")
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
    print("Welcome to the deliveries menu.")
    print("Here you can view a full delivery report, "
          "or see a list of requested, scheduled")
    print("and completed deliveries. You can also request " +
          "a new delivery.\n")
    print("Please select one of the following options:")
    print("1 - Full Delivery Report")
    print("2 - Requested Deliveries")
    print("3 - Scheduled Deliveries")
    print("4 - Completed Deliveries")
    print("5 - Create Delivery Request (Car ID Required)")
    print("0 - Return to Main Menu")

    while True:
        selected_option = get_integer_input("\nSelect an option " +
                                            "(1-5, 0 to main menu/quit): ")
        clear_terminal()
        match selected_option:
            case 0:
                main_menu()
                break
            case 1:
                print("- Full Delivery Report -\n")
                display_deliveries_table()
                break
            case 2:
                print("- Requested Deliveries -\n")
                display_deliveries_table(["requested"])
                break
            case 3:
                print("- Scheduled Deliveries -\n")
                display_deliveries_table(["scheduled"])
                break
            case 4:
                print("- Completed Deliveries -\n")
                display_deliveries_table(["delivered"])
                break
            case 5:
                print("- Creating Delivery Request -\n")
                delivery_request()
                break
            case _:
                print("Not a valid entry, please try again.")

    return_to_main_menu()


def art():
    art = ['    .---------------.',
           '   /                 \\      - KM Car Sales - ',
           ' O/_____/________/____\\       Leeds',
           ' /__________+__________\\      Liverpool',
           '/    (#############)   \\      Manchester',
           '|[**](#############)[**]|     Preston',
           '\\ ____________________ //     York',
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
    print("1 - Current Stock Info")
    print("2 - Add/Edit/Sell Car")
    print("3 - Sales Reports")
    print("4 - Delivery Reports/Requests")
    print("5 - Help")
    print("0 - Exit Program")

    while True:
        selected_option = get_integer_input("\nSelect an option " +
                                            "(1-5, 0 to quit): ")
        clear_terminal()
        match selected_option:
            case 0:
                quit()
            case 1:
                stock_menu()
                break
            case 2:
                edit_menu()
                break
            case 3:
                sales_menu()
                break
            case 4:
                deliveries_menu()
                break
            case 5:
                display_help()
                return_to_main_menu()
            case _:
                print("Not a valid entry, please try again.")


def return_to_main_menu():
    """
    Returns to main menu or quits on user input.
    """
    while True:
        print()
        answer = input('Type "m" to return to the menu ' +
                       'or "0" to quit.\n').lower()
        clear_terminal()
        if answer == "0":
            quit()
        elif answer == "m":
            main_menu()
            return
        else:
            print("Not a valid input. Please try again.")
