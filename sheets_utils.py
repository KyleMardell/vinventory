import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from car import Car, create_car_instances

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
    Connect to worksheet within Google Sheets using provided sheet name
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
    sheet_data = connect_to_sheet(sheet_name)
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
    else:
        print("Error: No worksheet data found.")

def display_car_by_id(sheet_name, id):
    """ 
    Displays a single cars info.
    Loops through all cars in the sheet to check for ID and
    prints an error message if ID does not exist.
    """
    try:
        sheet_data = connect_to_sheet(sheet_name)
        cars_in_stock = create_car_instances(sheet_data[1:])

        for car in cars_in_stock:
            if int(car.id) == id:
                car.display_info(9)
                return car

    except Exception as e:
        print("An error occurred: {e}")
        
    return False

def get_worksheet_names():
    """ 
    Returns a list of all worksheet names in the Google Sheet
    """
    try:
        SHEET = open_google_sheet()
        worksheets = SHEET.worksheets()
        worksheet_names = [worksheet.title for worksheet in worksheets]
        print(worksheet_names)
        return worksheet_names
    except Exception as e:
        print(f"An error occurred retrieving worksheet name data: {e}")
        
def generate_unique_id():
    unique_id = 1
    cars = []
    worksheet_names = get_worksheet_names()
    for name in worksheet_names:
        if name != "deliveries":
            car_data = connect_to_sheet(name)
            current_cars = create_car_instances(car_data[1:])
            cars.extend(current_cars)
    
    for car in cars:
        if int(car.id) >= unique_id:
            unique_id = int(car.id) + 1
    print(unique_id)