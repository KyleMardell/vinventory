import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from datetime import datetime, timedelta
from input_validation import get_integer_input


class Car:

    def __init__(self, id, make, model, year, milage, engine, colour, status, price, cost, repairs,
                 sold_price=None, deposit=None, payment_method=None, buyer_name=None, buyer_contact=None, sale_date=None):
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
        self.deposit = deposit if deposit is not None else "N/A"
        self.payment_method = payment_method if payment_method is not None else "N/A"
        self.buyer_name = buyer_name if buyer_name is not None else "N/A"
        self.buyer_contact = buyer_contact if buyer_contact is not None else "N/A"
        self.sale_date = sale_date if sale_date is not None else "N/A"

    def car_as_list(self):
        """ 
        Returns car object data values as a list
        """
        return [self.id, self.make, self.model, self.year, self.milage, self.engine, self.colour,
                self.status, self.price, self.cost, self.repairs, self.sold_price, self.deposit, self.payment_method,
                self.buyer_name, self.buyer_contact, self.sale_date]

    def display_info(self, fields):
        """ 
        Prints a table containing all car data
        """
        table_fields = ["ID", "Make", "Model", "Year", "Milage", "Engine",
                        "Colour", "Status", "Price", "Cost", "Repairs", "Sold Price", "Deposit Paid", "Payment Method", "Buyer Name", "Buyer Contact", "Sale Date"]
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
            print(f"Error converting to int: {e}")

    def request_delivery(self):
        print(f"Creating delivery request for car ID: {
              self.id} ({self.colour} {self.make} {self.model})")
        print(f"Current site: {self.status}")


def create_car_instances(car_data):
    """ 
    Create a list of cars from input data
    """
    cars = []
    for data in car_data:
        car = Car(data[0], data[1], data[2], data[3], data[4],
                  data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16])
        cars.append(car)
    return cars


def open_google_sheet():
    """
    Connects to google sheet via api, using gspread.
    Could be made to accept any creds file and sheet name by adding parameters.
    Not used here as I am only connecting to 1 sheet.
    Returns SHEET, open sheet data.
    """
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
        print(
            f"An error occurred while connecting to the Google Sheets API: {e}")


def connect_to_sheet(sheet_name):
    """ 
    Connect to sheet within Google Sheets using provided name,
    for editing sheet.
    """
    SHEET = open_google_sheet()
    try:
        current_sheet = SHEET.worksheet(sheet_name)
        return current_sheet
    except Exception as e:
        print(f"Error, sheet not found: {e}")


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
        print(f"Error, sheet not found: {e}")


def display_sheet_table(sheet_name, columns):
    """
    Displays a worksheet as a table.
    Requires worksheet name.
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
        except Exception as e:
            print("An error has occurred: {e}")


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
            input_id = get_integer_input("Please enter a valid ID number: ")
            for car in cars_in_stock:
                if int(car.id) == input_id:
                    car.display_info(9)
                    return car

    except Exception as e:
        print("An error occurred: {e}")

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
        print(f"An error occurred retrieving worksheet name data: {e}")


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
        print(f"An error has occurred: {e}")


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

    delivery_sheet.append_row(delivery_request)
    print("Request added to deliveries sheet")
    print(f"Expected delivery date (upon approval): {schedule_date}")
