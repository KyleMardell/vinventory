import sheets_utils
from sheets_utils import display_sheet_as_table, display_car_by_id, connect_to_sheet
from input_validation import get_integer_input, get_list_input
from car import create_car_instances

def find_car_by_id():
    found_id = False
    while not found_id:
        input_id = get_integer_input("Please enter a valid ID number: ")
        found_id = display_car_by_id("stock", input_id)
        
def search_car_by_criteria():
    data = connect_to_sheet("stock")
    stock_cars = create_car_instances(data[1:])
    search_terms = get_list_input("Enter search terms separated by comma's. ")
    print(search_terms)
    matching_cars = []
    for car in stock_cars:
        term_found = False
        for term in search_terms:
            if term in [str(value).lower() for value in car.car_as_list()]:
                term_found = True
                break
        if term_found:
            matching_cars.append(car)
            
        print(matching_cars)
        
    for car in matching_cars:
        car.display_info()
        
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
                display_sheet_as_table("stock")
                return_to_main_menu()
                break
            case 2:
                print("Find By ID selected...")
                find_car_by_id()
                return_to_main_menu()
                break
            case 3:
                print("Search Stock selected...")
                search_car_by_criteria()
                return_to_main_menu()
                break
            case _:
                print("Please enter a valid number.")

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