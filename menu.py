import sheets_utils
from sheets_utils import display_sheet_as_table, display_car_info, connect_to_sheet

def stock_menu():
    print("Current Stock Menu")
    print("Please select one of the following options (1/2)")
    print("1 - All Stock")
    print("2 - Search Stock")
    
    while True:
        selected_option = input("Select an option (1/2): ")
        
        match selected_option:
            case "1":
                print("All Stock selected...")
                SHEET = connect_to_sheet()
                display_sheet_as_table(SHEET, "stock")
                return_to_main_menu()
                break
            case "2":
                print("Search Stock selected...")
                return_to_main_menu()
                break

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
        selected_option = input("Select an option (1-4): ")
        
        match selected_option:
            case "1":
                print("Current Stock")
                stock_menu()
                break
            case "2":
                print("Add/Edit Vehicle Info")
                break
            case "3":
                print("Sales Reports")
                break
            case "4":
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