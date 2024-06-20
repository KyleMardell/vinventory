import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from datetime import datetime, timedelta
from input_validation import get_integer_input, get_site_input
from input_validation import *
import os
import platform


def clear_terminal():
    """
    Checks the operating system and clears the terminal
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


class Car:
    """
    Car class and functions
    Define minimum values to create a car,
    values match google sheets columns in order,
    with the optional values added when a car is sold.
    """
    def __init__(self, id, make, model, year, colour,
                 status, price, cost, repairs, sold_price=None,
                 sale_date=None):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.status = status
        self.price = price
        self.cost = cost
        self.repairs = repairs
        self.sold_price = sold_price if sold_price is not None else "N/A"
        self.sale_date = sale_date if sale_date is not None else "N/A"

    def car_as_list(self):
        """
        Returns car object data values as a list
        """
        return [self.id, self.make, self.model, self.year, self.colour,
                self.status, self.price, self.cost, self.repairs,
                self.sold_price, self.sale_date]

    def display_info(self, fields=11):
        """
        Prints a table containing all car data
        """
        table_fields = ["ID", "Make", "Model", "Year",
                        "Colour", "Status", "Price", "Cost",
                        "Repair", "Sold Price", "Sale Date"]
        table = PrettyTable()
        table.field_names = table_fields[:fields]
        table.add_row(self.car_as_list()[:fields])
        print(table)

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

    def request_delivery(self):
        print(f"Creating delivery request for car ID: " +
              f"{self.id} ({self.colour} {self.make} {self.model})")
        print(f"Current site: {self.status}")
        print("What is the destination site?")
        destination = get_site_input(self.status)
        create_delivery_request(
            self.id, self.make, self.model, self.year,
            self.status, destination)
        update_delivery_status_in_stock_sheet(
            self.id, self.status, delivery=True)


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

            cars_in_stock = create_car_instances(data_rows)

            # Create table
            table = PrettyTable()

            # Check if the sheet is a sales sheet
            if "sold" in sheet_name:
                sales_headers = ["ID", "Make", "Model", "Cost",
                                 "Repair", "Sold", "Profit",
                                 "Sale Date"]
                table.field_names = sales_headers
            else:
                table.field_names = headers[:columns]

            for car in cars_in_stock:
                # check if the sheet is a sales sheet
                if "sold" in sheet_name:
                    id = car.id
                    make = car.make
                    model = car.model
                    cost = car.cost
                    repairs = car.repairs
                    sold_price = car.sold_price
                    profit = car.calculate_profit()
                    sale_date = car.sale_date
                    car_to_add = [id, make, model, cost, repairs,
                                  sold_price, profit, sale_date]
                else:
                    car_to_add = car.car_as_list()[:columns]

                table.add_row(car_to_add)

            print(table)
            return True
        except Exception as e:
            print("Error: Cannot display table.")
            print(f"Details: {e}\n")
            return False


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
                    car.display_info(9)
                    car_found = True
                    return car
            print(f"Car ID: {input_id} not found.")

    except Exception as e:
        print("Error: Cannot find car.")
        print(f"Details: {e}\n")

    print("ID not found.")
    return False


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


def create_delivery_request(id, make, model, year, site_from, site_to):
    """
    Creates a delivery request in the deliveries sheet
    Requires car data as parameters, auto generates
    """
    delivery_sheet = connect_to_sheet("deliveries")
    current_date = datetime.now()
    request_date = str(current_date)[:10]
    schedule_date = current_date + timedelta(days=3)
    schedule_date = str(schedule_date)[:10]
    delivery_request = [id, make, model, year, site_from,
                        site_to, "requested", request_date, schedule_date]
    try:
        delivery_sheet.append_row(delivery_request)
        print("Request added to deliveries sheet")
        print(f"Expected delivery date (upon approval): {schedule_date}")
    except Exception as e:
        print("Error: could not add delivery to sheet.")
        print(f"Details: {e}\n")


def update_delivery_status_in_stock_sheet(id, status, delivery=False):
    """
    Updates the delivery status of a car in the stock Google Sheet
    Requires input of ID, status and delivery(boolean)
    """
    stock_sheet = connect_to_sheet("stock")
    id_cell = stock_sheet.find(id)
    status_cell = f"F{id_cell.row}"

    suffix = "-D"

    if delivery:
        new_status = f"{status}{suffix}"
    else:
        new_status = status.removesuffix(suffix)

    stock_sheet.update_acell(status_cell, new_status)
    print(f"\nStock sheet information for car ID: {id} has been updated.")


def add_car_to_sheet(car_as_list, sheet_name):
    """
    Adds a car to the stock list.
    Requires a list of car details in correct order as per stock sheet.
    [ID, Make, Model, Year, Colour, Status, Price, Cost, Repairs]
    """
    try:
        stock_sheet = connect_to_sheet(sheet_name)
        stock_sheet.append_row(car_as_list)
        print(f"Car ID: {car_as_list[0]} successfully added to " +
              f"{sheet_name} sheet.")
    except Exception as e:
        print("Error: Could not add vehicle to sheet.")
        print(f"Details: {e}\n")


def delete_car_from_sheet(sheet_name, car_id=None):
    """
    Deletes a car from the stock list.
    Asks user for a valid car id number and to confirm before deleting.
    """
    current_sheet = connect_to_sheet(sheet_name)
    if car_id is None:
        car_to_delete = find_car_by_id(sheet_name)
        car_id = car_to_delete.id
        cell = current_sheet.find(car_id)
        while True:
            answer = input(f"Do you want to delete the car (ID:{car_id})" +
                           f" from the {sheet_name} sheet? (y/n): \n").lower()
            if answer == "y":
                clear_terminal()
                try:
                    current_sheet.delete_rows(cell.row)
                    print(f"Car ID: {car_id} successfully deleted from " +
                          f"{sheet_name}.\n")
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
            print(f"Car ID: {car_id} successfully deleted from " +
                  f"{sheet_name}.\n")
        except Exception as e:
            print("Error: Cannot delete car from sheet.")
            print(f"Details: {e}\n")


def edit_car_in_stock():
    """
    Edits a car in stocks information.
    Asks the user to enter a car ID, once confirmed then asks the user to
    enter which attribute they would like to edit. Changes are submitted
    by entering 0.
    """

    def get_changes():
        """
        edit_car_in_stock inner function only.
        Gets the user input changes and validates each input.
        """
        car_details = "(Make, Model, Year, Colour, "
        car_details += "Status, Price, Cost, Repairs)"
        changes_message = "Enter the name of the attribute you would like to "
        changes_message += f"edit {car_details} or 0 to finish editing.: \n"

        changes = None
        while True:
            changes = input(changes_message).lower()
            match (changes):
                case "make":
                    message = "Enter new details: "
                    car_to_edit.make = get_string_input(message).capitalize()
                    print("Confirmed.\n")
                    continue
                case "model":
                    message = "Enter new model details: \n"
                    car_to_edit.model = input(message).capitalize()
                    print("Confirmed.\n")
                    continue
                case "year":
                    message = "Enter new year details: "
                    car_to_edit.year = get_year_input(message)
                    print("Confirmed.\n")
                    continue
                case "colour":
                    message = "Enter new colour details: "
                    car_to_edit.colour = get_colour_input(message)
                    print("Confirmed.\n")
                    continue
                case "status":
                    print("Status, cannot be manually updated.")
                    print("To change location, request a delivery. " +
                          "To mark as reserved or sold, " +
                          "use previous options.\n")
                    continue
                case "price":
                    message = "Enter new vehicle price details: "
                    cost = int(car_to_edit.cost)
                    repairs = int(car_to_edit.repairs)
                    car_to_edit.price = get_price_input(message, cost, repairs)
                    print("Confirmed.\n")
                    continue
                case "cost":
                    message = "Enter new vehicle cost details: "
                    car_to_edit.cost = get_integer_input(message)
                    print("Confirmed.\n")
                    continue
                case "repairs":
                    message = "Enter new repair cost details: "
                    car_to_edit.repairs = get_integer_input(message)
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
        answer = input("Are you sure you would like to edit the car, " +
                       f"ID: {car_to_edit.id}? (y/n): \n").lower()
        if answer == "y":
            # Get the changes to the car
            get_changes()
            car_to_edit.display_info(9)
            while True:
                # Ask the user to confirm the changes and save if yes.
                confirm = input("Do you want to save " +
                                "these changes? (y/n): \n").lower()
                if confirm == "y":
                    clear_terminal()
                    print("Confirmed...")
                    try:
                        # Get the car as a list and update the Google Sheet
                        car_as_list = car_to_edit.car_as_list()
                        stock_sheet.update(f"A{cell.row}:Q{cell.row}",
                                           [car_as_list])
                        print(f"Changes to car ID: {car_to_edit.id} " +
                              "have been saved to the worksheet.\n")
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
    """
    Creates a new sales sheet.
    """
    headings = ["ID", "Make", "Model", "Year", "Colour", "Status",
                "Price", "Cost", "Repairs", "Sold Price",
                "Sale Date"]

    try:
        vinv_sheet = open_google_sheet()
        new_sheet = vinv_sheet.add_worksheet(title=sheet_name, rows=0, cols=11)
        new_sheet.append_row(headings)
        print(f"New sales sheet created named '{sheet_name}'")
    except Exception as e:
        print("Error: Sheet could not be created.")
        print(f"Details: {e}\n")


def sell_car(current_sales_sheet):
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
        sale_date = str(current_date)[:9]
        while True:
            sold_price = get_integer_input("Enter the vehicle's sold " +
                                           "price (i.e. 15000, 22500): £ ")

            while True:
                confirm = input("Confirm and save new sale details " +
                                "(y/n, enter 0 to exit): \n").lower()
                if confirm == "y":
                    clear_terminal()
                    sold_car.sold_price = sold_price
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
