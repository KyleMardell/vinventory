from prettytable import PrettyTable


def display_help():
    # function to display a help file with an explanation of how each section of the app works
    """ 
    displays the help text
    """
    table_fields = ["ID", "Make", "Model", "Year", "Milage", "Engine",
                    "Colour", "Status", "Price", "Cost", "Repairs", "Sold Price", "Buyer Name", "Buyer Contact", "Sale Date"]
    table_data = ["123", "Ford", "Fiesta", "2015", "18000", "1.2", "White",
                  "York", "13500", "9000", "250", "12500", "Ken", "07123456789", "2024-04-10"]
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
    print("\nSearching By ID")
    print("In order to view a cars information such as in the example, you can search for a car by its ID number.")
    print("If you already know the ID number of a car in stock then you can enter it to view the information.")
    print("If yo do not know the ID number of a car, you can find it using the all stock table, or search using entered terms.")
    print("\nSearching By Terms")
    print("To search cars by terms, you can simply enter the terms you wish to search for, separated by commas.")
    print("I.e. 'white, silver, Ford")
    print("Using the example input, you will be given a list of all white and silver cars, as well as all Fords.")
    print("Using the search, if you know there is a ford in stock but need to find the ID number, you can do it this way.")
    print("Note: You will often need the ID number of a car to edit, delete, mark as sold, etc.")

    print("\n- Sales Reports Menu -\n")
    print("There are 4 options in the sales reports menu, 2 displaying tables of sold cars, and 2 displaying profit reports.")
    print("When choosing the current months sales table or report, if the current sales sheet does not already exist,")
    print("you will be notified and an empty sales sheet will be created.")
    print("Sales tables will be displayed in the table format shown above. The sales report will show information such as,")
    print("the number of cars sold, the total cost of cars sold, the total takings and profit of all cars, etc.")
    print("\nPast Sales Table/Report")
    print("In order to display a past sales sheet table or report, you must enter the")
    print("year and month of the sheet you wish to view.")
    print("If the sales sheet you are trying to access does not exist, an error will be shown.")

    print("\n- Add/Edit Menu -\n")
    print("From here you can do many functions, such as add, edit or delete a car in stock,")
    print("mark a car as sold and request a delivery.")
    print("Each function operates differently, with some similarities between each for ease of use.")
    print("\nAdd Car To Stock")
    print("When adding a car to stock, you will be asked o enter all the relevant information such as,")
    print("make, model, year, milage, colour, etc.")
    print("Most of the entered values are checked to make sure they are in the correct format,")
    print("and an error message will be shown if an unexpected value is given.")
    print("The user must make sure all entered information is correct before submitting.")
    print("\nEdit Car in Stock")
    print("In order to edit a car in stock, you must provide the ID number of the car, which can be found as explained above.")
    print("You will then be asked to enter which detail you wish to edit, such as colour, year etc.")
    print("Once you have entered the detail you wish to edit, you can then enter the new value.")
    print("You can edit multiple details before saving by entering 0")
    print("\nDelete Car in Stock")
    print("Warning!")
    print("Once a car has been deleted, it cannot be retrieved, and must be entered into the system as a new car if required.")
    print("In order to delete a car from the stock sheet, toy must provide the car Id which can be found as described above.")
    print("The car will be deleted and feedback will be given to confirm.")
    print("\nSell A Car")
    print("In order to mark a car as sold you will need to provide the ID number of the car.")
    print("You will then be asked to enter the sales details such as sale amount, buyer name etc.")
    print("Once all details have been entered and confirmed, the car will be added to the current sales sheet,")
    print("and deleted from the stock sheet, with message to confirm both actions.")
    print("\nRequest delivery")
    print("Details shown below.")

    print("\n- Delivery Menu -\n")
    print("The delivery menu displays different delivery reports, and can be used to request a delivery.")
    print("Delivery reports can be viewed by selecting one of the options, all, delivered, scheduled and requested.")
    print("The report will be shown in a table format similar to shown above.")
    print("Only one deliveries sheet currently exists, so all deliveries will be shown.")
    print("This could be updated to create a new delivery sheet per month if required.")
    print("Note - Deliveries cannot yet be edited using this system (could be linked to a driver system).")
    print("\nRequest delivery")
    print("You can request an internal delivery of a car from one site to another.")
    print("This is for things such as test drives, stock distribution and sales.")
    print("When requesting a delivery, you must provide the ID number of the car and the destination.")
    print("The current location will be displayed in the cars information, and cannot be entered as a destination.")
    print("Only destinations on the sites list will be accepted.")
    print("Once a delivery request has been made, it will be added to the delivery sheet and marked with a")
    print("delivery request in the status on the stock sheet.")
    print("The current date will be used as the delivery request date, and an automatic schedule date will")
    print("be created 3 days ahead of the current date.")
    print("Note - Deliveries cannot be marked as delivered using this system yet (could be linked to a driver system).")
