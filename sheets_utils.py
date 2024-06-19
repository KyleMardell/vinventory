import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from datetime import datetime, timedelta
from input_validation import get_integer_input, get_site_input
from input_validation import *
import os
import platform

# function to clear the terminal


def clear_terminal():
    """ 
    Checks the operating system and clears the terminal
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Car class and functions


class Car:

    # define minimum values to create a car, values match google sheets columns in order,
    # with the optional values added when a car is sold.
    def __init__(self, id, make, model, year, milage, engine, colour, status, price, cost, repairs, sold_price=None, buyer_name=None, buyer_contact=None, sale_date=None):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.milage = milage
        self.engine = engine
        self.colour = colour
        self.status = status
        self.price = price
        self.cost = cost
        self.repairs = repairs
        self.sold_price = sold_price if sold_price is not None else "N/A"
        self.buyer_name = buyer_name if buyer_name is not None else "N/A"
        self.buyer_contact = buyer_contact if buyer_contact is not None else "N/A"
        self.sale_date = sale_date if sale_date is not None else "N/A"

    # function to return the cars properties as a list in the same order as the google sheet.
    def car_as_list(self):
        """ 
        Returns car object data values as a list
        """
        return [self.id, self.make, self.model, self.year, self.milage, self.engine, self.colour,
                self.status, self.price, self.cost, self.repairs, self.sold_price, self.buyer_name, self.buyer_contact, self.sale_date]

    # function to display the cars properties in a table
    def display_info(self, fields=15):
        """ 
        Prints a table containing all car data
        """
        table_fields = ["ID", "Make", "Model", "Year", "Milage", "Engine",
                        "Colour", "Status", "Price", "Cost", "Repairs", "Sold Price", "Buyer Name", "Buyer Contact", "Sale Date"]
        table = PrettyTable()
        table.field_names = table_fields[:fields]
        table.add_row(self.car_as_list()[:fields])
        print(table)

    # function to calculate the cars profit when sold
    def calculate_profit(self):
        """ 
        Calculates profit if car has been sold
        """
        try:
            profit = int(self.sold_price) - \
                (int(self.cost) + int(self.repairs))
            return profit
        except ValueError as e:
            print("Error: Cannot convert to int.")
            print(f"Details: {e}\n")

    # function to create a delivery request for the car
    def request_delivery(self):
        print(f"Creating delivery request for car ID: {
            self.id} ({self.colour} {self.make} {self.model})")
        print(f"Current site: {self.status}")
        print("What is the destination site?")
        destination = get_site_input(self.status)
        create_delivery_request(
            self.id, self.make, self.model, self.year, self.milage, self.status, destination)
        update_delivery_status_in_stock_sheet(
            self.id, self.status, delivery=True)

# function to create a list of car instances from a given list of cars
# uses the spread operator to create either cars in stock or
# sold cars with additional sales information


def create_car_instances(car_data):
    """ 
    Create a list of cars from input data
    """
    cars = []
    for data in car_data:
        car = Car(*data)
        cars.append(car)
    return cars

# Sheets functions

# function to open the connection to the 'VinVentory' google sheet
# Could be made to accept any creds file and sheet name by adding parameters.
# Not used here as I am only connecting to 1 sheet.
# returns the full sheet (all worksheets) if found


def open_google_sheet():
    """
    Connects to google sheet via api, using gspread.
    Returns SHEET, open sheet data.
    """
    # the scope defines which google drive and sheets api functions are needed
    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    try:
        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('vinventory')
        return SHEET
    except Exception as e:
        print("Error: Cannot connect to the Google Sheets API")
        print(f"Details: {e}\n")

# function that connects to a worksheet within the 'VinVentory' google sheet


def connect_to_sheet(sheet_name):
    """ 
    Connect to worksheet within Google Sheets using provided name,
    for editing sheet.
    """
    print("\nRetrieving Worksheet Information...\n")
    SHEET = open_google_sheet()
    try:
        current_sheet = SHEET.worksheet(sheet_name)
        return current_sheet
    except Exception as e:
        print("Error, sheet not found:")
        print(f"Details: {e}\n")

# function to get all the sheet data from a worksheet
# returns as a list of lists (a list of cars, each car listing its information)


def get_sheet_data(sheet_name):
    """ 
    Connect to worksheet within Google Sheets using provided sheet name
    get all sheet data values and return sheet data
    """
    SHEET = open_google_sheet()
    try:
        current_sheet = SHEET.worksheet(sheet_name)
        sheet_data = current_sheet.get_all_values()
        return sheet_data
    except Exception as e:
        print(f"Error, sheet not found.")
        print(f"Details: {e}\n")

# function to create a table from a worksheet
# creates a table with the provided number of columns to account
# for sold and unsold cars


def display_sheet_table(sheet_name, columns):
    """
    Displays a worksheet as a table.
    Requires worksheet name and amount of columns.
    """
    sheet_data = get_sheet_data(sheet_name)
    if sheet_data:
        try:
            headers = sheet_data[0]
            data_rows = sheet_data[1:]

            table = PrettyTable()
            table.field_names = headers[:columns]

            cars_in_stock = create_car_instances(data_rows)
            for car in cars_in_stock:
                car_to_add = car.car_as_list()[:columns]
                table.add_row(car_to_add)

            print(table)
            return True
        except Exception as e:
            print("Error: Cannot display table.")
            print(f"Details: {e}\n")
            return False

# function to find a car within a worksheet
# creates a list of cars using create_car_instances and loops through to
# check for a provided ID number
# if found, returns car.display_info to show the user the cars information


def find_car_by_id(sheet_name):
    """ 
    Displays a single cars info.
    Loops through all cars in the sheet to check for ID and
    prints an error message if ID does not exist.
    """
    try:
        sheet_data = get_sheet_data(sheet_name)
        cars_in_stock = create_car_instances(sheet_data[1:])
        car_found = False
        while not car_found:
            input_id = get_integer_input(
                "Please enter a cars valid internal ID number: ")
            for car in cars_in_stock:
                if int(car.id) == input_id:
                    car.display_info(11)
                    car_found = True
                    return car
            print(f"Car ID: {input_id} not found.")

    except Exception as e:
        print("Error: Cannot find car.")
        print(f"Details: {e}\n")

    print("ID not found.")
    return False

# function to get all worksheet names within the 'VinVentory' google sheet
# returns a list of all the worksheet names


def get_worksheet_names():
    """ 
    Returns a list of all worksheet names in the Google Sheet
    """
    try:
        SHEET = open_google_sheet()
        worksheets = SHEET.worksheets()
        worksheet_names = [worksheet.title for worksheet in worksheets]
        return worksheet_names
    except Exception as e:
        print("Error: Cannot retrieve worksheet name data")
        print(f"Details: {e}\n")

# function to generate a unique ID number by createing a list of
# cars called current_cars and looping through each worksheet and adding them to the list
# once the list of all cars in all worksheets is complete, all ID numbers are checked
# the highest found ID is incremented by 1 to create and return a unique ID


def generate_unique_id():
    """ 
    Checks all current stock and sold cars and generates
    a new unique ID number
    """
    print("Generating unique ID...")
    unique_id = 1
    cars = []
    try:
        worksheet_names = get_worksheet_names()
        for name in worksheet_names:
            if name != "deliveries":
                car_data = get_sheet_data(name)
                current_cars = create_car_instances(car_data[1:])
                cars.extend(current_cars)

        for car in cars:
            if int(car.id) >= unique_id:
                unique_id = int(car.id) + 1

        return unique_id

    except Exception as e:
        print("Error: Cannot generate unique ID number.")
        print(f"Details: {e}\n")

# function to add a delivery request to the delivery worksheet
# creates a request date using the current date and a scheduled date
# 3 days ahead of the current date.


def create_delivery_request(id, make, model, year, milage, site_from, site_to):
    """ 
    Creates a delivery request in the deliveries sheet
    Requires car data as parameters, auto generates
    """
    delivery_sheet = connect_to_sheet("deliveries")
    current_date = datetime.now()
    request_date = str(current_date)[:10]
    schedule_date = current_date + timedelta(days=3)
    schedule_date = str(schedule_date)[:10]
    delivery_request = [id, make, model, year, milage, site_from,
                        site_to, "requested", request_date, schedule_date]
    try:
        delivery_sheet.append_row(delivery_request)
        print("Request added to deliveries sheet")
        print(f"Expected delivery date (upon approval): {schedule_date}")
    except Exception as e:
        print("Error: could not add delivery to sheet.")
        print(f"Details: {e}\n")

# function to update the status of a car in stock when a delivery is requested
# can be used to remove a delivery status from a car in stock


def update_delivery_status_in_stock_sheet(id, status, delivery=False):
    """ 
    Updates the delivery status of a car in the stock Google Sheet
    Requires input of ID, status and delivery(boolean)
    """
    stock_sheet = connect_to_sheet("stock")
    id_cell = stock_sheet.find(id)
    status_cell = f"H{id_cell.row}"

    suffix = " - Delivery requested"

    if delivery:
        new_status = f"{status}{suffix}"
    else:
        new_status = status.removesuffix(suffix)

    stock_sheet.update_acell(status_cell, new_status)
    print(f"\nStock sheet information for car ID: {id} has been updated.")

# function to add a car to a sheet using provided sheet name and car as a list


def add_car_to_sheet(car_as_list, sheet_name):
    """ 
    Adds a car to the stock list.
    Requires a list of car details in correct order as per stock sheet.
    [ID, Make, Model, Year, Milage, Engine, Colour, Status, Price, Cost, Repairs]
    """
    try:
        stock_sheet = connect_to_sheet(sheet_name)
        stock_sheet.append_row(car_as_list)
        print(f"Vehicle ({car_as_list[1]} {
            car_as_list[2]}) successfully added to {sheet_name} sheet.")
    except Exception as e:
        print("Error: Could not add vehicle to sheet.")
        print(f"Details: {e}\n")




def delete_car_from_sheet(sheet_name, car_id=None):
    # function to delete a car from a sheet
    # uses the find function to check if a car with provided ID exists
    # optional car id parameter deleted the car with provided ID number
    # if no ID is provided, the user is asked to provide one
    """ 
    Deletes a car from the stock list.
    Asks user for a valid car id number and to confirm before deleting.
    """
    current_sheet = connect_to_sheet(sheet_name)
    if car_id == None:
        car_to_delete = find_car_by_id(sheet_name)
        car_id = car_to_delete.id
        cell = current_sheet.find(car_id)
        while True:
            answer = input(
                f"Would you would like to delete the car (ID:{car_id}) from the {sheet_name} sheet? (y/n): \n").lower()
            if answer == "y":
                clear_terminal()
                try:
                    current_sheet.delete_rows(cell.row)
                    print(f"Car ID: {car_id} successfully deleted from {
                          sheet_name}.\n")
                except Exception as e:
                    print("Error: Cannot delete car from sheet.")
                    print(f"Details: {e}")
                return
            elif answer == "n":
                print("Cancelled\n")
                return
            else:
                print("Invalid input, please try again.\n")
                continue
    else:
        cell = current_sheet.find(car_id)
        try:
            current_sheet.delete_rows(cell.row)
            print(f"Car ID: {car_id} successfully deleted from {
                  sheet_name}.\n")
        except Exception as e:
            print("Error: Cannot delete car from sheet.")
            print(f"Details: {e}\n")

def edit_car_in_stock():
    # function to edit a car currently in stock
    # asks the user to enter a cars ID to edit, thens asks which attribute
    # they would like to edit, until they enter 0 to save and exit
    # this functions contains an inner function to get the changes made to a car for better readability
    """ 
    Edits a car in stocks information.
    Asks the user to enter a car ID, once confirmed then asks the user to
    enter which attribute they would like to edit. Changes are submitted 
    by entering 0.
    """

    # function to get the user input changes to the selected car.
    def get_changes():
        """ 
        edit_car_in_stock inner function only.
        Gets the user input changes and validates each input.
        """
        changes = None
        while True:
            changes = input(
                "Enter the name of the attribute you would like to edit (Make, Model, Year, Milage, Engine, Colour, Status, Price, Cost, Repairs) or enter 0 to finish editing.: \n").lower()
            match (changes):
                case "make":
                    car_to_edit.make = get_string_input(
                        "Enter new make details: ").capitalize()
                    print("Confirmed.\n")
                    continue
                case "model":
                    car_to_edit.model = input(
                        "Enter new model details: \n").capitalize()
                    print("Confirmed.\n")
                    continue
                case "year":
                    car_to_edit.year = get_year_input(
                        "Enter new year details: ")
                    print("Confirmed.\n")
                    continue
                case "milage":
                    car_to_edit.milage = get_integer_input(
                        "Enter new milage details: ")
                    print("Confirmed.\n")
                    continue
                case "engine":
                    car_to_edit.engine = get_engine_input(
                        "Enter new engine details: ")
                    print("Confirmed.\n")
                    continue
                case "colour":
                    car_to_edit.colour = get_colour_input(
                        "Enter new colour details: ")
                    print("Confirmed.\n")
                    continue
                case "status":
                    print("Status, cannot be manually updated.")
                    print(
                        "To change location, please request a delivery. To mark as reserved or sold, please user previous menu options.\n")
                    continue
                case "price":
                    car_to_edit.price = get_price_input(
                        "Enter new vehicle price details: ")
                    print("Confirmed.\n")
                    continue
                case "cost":
                    car_to_edit.cost = get_integer_input(
                        "Enter new vehicle cost details: ")
                    print("Confirmed.\n")
                    continue
                case "repairs":
                    car_to_edit.repairs = get_integer_input(
                        "Enter new repair cost details: ")
                    print("Confirmed.\n")
                    continue
                case "0":
                    return
                case _:
                    print("Invalid input, please try again.\n")

    # Connect to the sheet and get the car to edit.
    # Get the cell of the car ID from the sheet to use when editing.
    stock_sheet = connect_to_sheet("stock")
    car_to_edit = find_car_by_id("stock")
    car_id = car_to_edit.id
    cell = stock_sheet.find(car_id)

    while True:
        answer = input(f"Are you sure you would like to edit the car, ID: {
                       car_to_edit.id}? (y/n): \n").lower()
        if answer == "y":
            # Get the changes to the car
            get_changes()
            car_to_edit.display_info(11)
            while True:
                # Ask the user to confirm the changes and save if yes.
                confirm = input(
                    "Do you want to save these changes? (y/n): \n").lower()
                if confirm == "y":
                    clear_terminal()
                    print("Confirmed...")
                    try:
                        # Get the car as a list and update the Google Sheet
                        car_as_list = car_to_edit.car_as_list()
                        stock_sheet.update(
                            f"A{cell.row}:Q{cell.row}", [car_as_list])
                        print(f"Changes to car ID: {
                              car_to_edit.id} have been saved to the worksheet.\n")
                    except Exception as e:
                        print("Error, changes not saved.")
                        print(f"Details: {e}\n")
                        continue
                    return
                elif confirm == "n":
                    print("Cancelled.\n")
                    break
                else:
                    print("Invalid input, please try again.\n")
                    continue

        elif answer == "n":
            print("Cancelled.\n")
            return
        else:
            print("Invalid input, please try again.\n")
            continue

def create_new_sales_sheet(sheet_name):
    # function to create a new sales sheet using consistent headings for all sales sheets.
    """ 
    Creates a new sales sheet.
    """
    headings = ["ID", "Make", "Model", "Year", "Milage", "Engine", "Colour", "Status",
                "Price", "Cost", "Repairs", "Sold Price", "Buyer Name", "Buyer Contact", "Sale Date"]

    try:
        vinv_sheet = open_google_sheet()
        new_sheet = vinv_sheet.add_worksheet(title=sheet_name, rows=0, cols=15)
        new_sheet.append_row(headings)
        print(f"New sales sheet created named '{sheet_name}'")
    except Exception as e:
        print("Error: Sheet could not be created.")
        print(f"Details: {e}\n")

def sell_car(current_sales_sheet):
    # function to mark a car as sold, adding to the current sales sheet and
    # deleting from the stock sheet.
    # contains an inner function to get the sale details for readability
    """ 
    Gets sale details from user and moves car from stock sheet to sales sheet.
    """
    print("- Sell Car Menu -\n")

    sold_car = find_car_by_id("stock")

    def get_sales_details():
        """ 
        Gets the sales details from the user and adds them to the current car.
        """
        current_date = datetime.now()
        sale_date = str(current_date)[:10]
        while True:
            sold_price = get_integer_input(
                "Enter the vehicle's sold price (i.e. 15000, 22500): £ ")
            buyer_name = get_string_input("Enter the buyers name: ")
            buyer_contact = get_integer_input(
                "Enter the buyers phone number: ")

            while True:
                confirm = input(
                    "Confirm and save new sale details (y/n, enter 0 to exit): \n").lower()
                if confirm == "y":
                    clear_terminal()
                    sold_car.sold_price = sold_price
                    sold_car.buyer_name = buyer_name
                    sold_car.buyer_contact = buyer_contact
                    sold_car.sale_date = sale_date
                    sold_car.status = "Sold"
                    return sold_car
                elif confirm == "n":
                    print("Cancelled.")
                    break
                elif confirm == "0":
                    print("Exiting.")
                    return False
                else:
                    print("Invalid input, please try again.\n")
                    continue

    while True:
        answer = input(
            "Would you like to continue selling this car? (y/n): \n").lower()
        if answer == "y":
            new_sale = get_sales_details()
            if new_sale:
                car_as_list = new_sale.car_as_list()
                add_car_to_sheet(car_as_list, current_sales_sheet)
                delete_car_from_sheet("stock", new_sale.id)
            return
        elif answer == "n":
            print("Cancelled.")
            break
        else:
            print("Invalid input, please try again.\n")
            continue
