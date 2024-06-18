from prettytable import PrettyTable

def display_help():
    """ 
    
    """
    table_fields = ["ID", "Make", "Model", "Year", "Milage", "Engine",
                        "Colour", "Status", "Price", "Cost", "Repairs", "Sold Price", "Buyer Name", "Buyer Contact", "Sale Date"]
    table_data = ["123", "Ford", "Fiesta", "2015", "18000", "1.2", "White", "York", "13500", "9000", "250", "12500", "Ken", "07123456789", "2024-04-10"]
    table = PrettyTable()
    table.field_names = table_fields
    table.add_row(table_data)
    
        
    print("- Help Section -\n")
    print("Welcome to VinVentory, the car sales management system.")
    print("VinVentory has the ability to store, create and edit information about cars for businesses using a simple Google Sheets worksheet.")
    print("This means we can easily add cars in stock, request deliveries and of course sell cars.")
    print("Please see each section for further information about how to use the VinVentory car management system.\n")
    
    print("\n- Home Menu - \n")
    print("From the home menu, you can navigate to each of the sub menus or exit the program.")
    print("Each sub menu is labelled and numbered for ease of navigation.")
    print("To navigate through the menus, simple enter the number of the corresponding menu item.")
    print("This will take you to the sub menu, or if already in a sub menu, to the intended function (i.e, adding a car to the system).")
    print("Enter 0 to return to the main menu, from a sub menu, or to exit the program from the main menu.")
    print("Each menu will be presented in a similar format as follows. (example used is the main menu)\n")
    print("Please select one of the following options:")
    print("1 - Current Stock Info")
    print("2 - Add/Edit/Sell Car")
    print("3 - Sales Reports")
    print("4 - Delivery Reports/Requests")
    print("5 - Help")
    print("0 - Exit Program")
    
    print("\n- Stock Menu -\n")
    print("The stock menu gives you the option to see all cars in stock in a table format,")
    print("view the information of a car in stock, or search for cars matching input terms.")
    print("When retrieving car information, it will often be displayed in a table format as in the following example.\n")
    print(table)
    print("\nWhen displaying multiple cars information, they will be appended to the table, such as when viewing all stock.")
    print("Searching By ID")
    print("In order to view a cars information such as in the example, you can search for a car by its ID number.")
    print("If you already know the ID number of a car in stock then you can enter it to view the information.")
    print("If yo do not know the ID number of a car, you can find it using the all stock table, or search using entered terms.")
    print("Searching By Terms")
    print("To search cars by terms, you can simply enter the terms you wish to search for, separated by commas.")
    print("I.e. 'white, silver, Ford")
    print("Using the example input, you will be given a list of all white and silver cars, as well as all Fords.")
    print("Using the search, if you know there is a ford in stock but need to find the ID number, you can do it this way.")
    print("Note: You will often need the ID number of a car to edit, delete, mark as sold, etc.")
    
    print("\n- Sales Reports Menu -\n")
    