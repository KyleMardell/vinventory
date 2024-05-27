from sheets_utils import *
from input_validation import get_integer_input, get_list_input
from car import create_car_instances
from prettytable import PrettyTable

def find_car_by_id():
    """ 
    Search for a car by ID number
    """
    found_id = False
    while not found_id:
        input_id = get_integer_input("Please enter a valid ID number: ")
        found_id = display_car_by_id("stock", input_id)
        
def search_car_by_criteria():
    """ 
    Search for a car by criteria.
    Gets the list of cars in stock and asks the user to input a list of desired criteria. 
    Creates a table of cars with matching criteria.
    """
    data = connect_to_sheet("stock")
    stock_cars = create_car_instances(data[1:])
    matching_cars = []
    
    while matching_cars == []:
        
        search_terms = get_list_input("Enter search terms / desired features separated by comma's. (E.g. 'Red, Ford,' or '2020, white, volvo') ")

        for car in stock_cars:
            term_found = False
            for term in search_terms:
                if term in [str(value).lower() for value in car.car_as_list()] and car.status.lower() != "reserved":
                    term_found = True
                    break
            if term_found:
                matching_cars.append(car)
            
        if matching_cars == []:
            print("No matches found.")
            continue
        else:
            table = PrettyTable()
            table.field_names = table.field_names = ["ID", "Make", "Model", "Year", "Milage", "Engine", "Colour", "Status", "Price", "Cost", "Repairs"]
            for car in matching_cars:
                table.add_row(car.car_as_list()[:11])
            print(table)
        
def stock_menu():
    print("Current Stock Menu")
    print("Please select one of the following options (1-3)")
    print("1 - All Stock")
    print("2 - Find By ID")
    print("3 - Search Stock")
    
    while True:
        selected_option = get_integer_input("Select an option (1-3): ")
        
        match selected_option:
            case 1:
                print("All Stock selected...")
                display_sheet_table("stock", 9)
                break
            case 2:
                print("Find By ID selected...")
                find_car_by_id()
                break
            case 3:
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
    print("1 - Current months full sales report")
    print("2 - Sales report history")
    
    selected_option = get_integer_input("Select an option (1 or 2): ")
    
    if (selected_option == 1):
        print("Current Months Sales Report")
        display_sheet_table("sold-current", 12)
    elif (selected_option == 2):
        print("Sales Report History")
    else:
        print("Not a valid entry. Please try again.")
    
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
                print("Current Stock")
                stock_menu()
                break
            case 2:
                print("Add/Edit Vehicle Info")
                break
            case 3:
                print("Sales Reports")
                sales_menu()
                break
            case 4:
                print("Delivery Reports")
                break
            case _:
                print("Not a valid entry, please try again.")
                
def return_to_main_menu():
    """ 
    Returns to main menu or quits on user input.
    """
    answer = input('Type "m" to return to the menu or "q" to quit.').lower()
    if answer == "q":
        quit()
    elif answer == "m":
        main_menu()
    else:
        print("Not a valid input. Please try again.")