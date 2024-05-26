import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from car import Car, create_car_instances

def connect_to_sheet(sheet_name):
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

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('vinventory')
    current_sheet = SHEET.worksheet(sheet_name)
    sheet_data = current_sheet.get_all_values()
    return sheet_data

def display_sheet_as_table(sheet_name):
    """
    Displays a worksheet as a table.
    Requires sheet data from connect_to_sheet method and
    worksheet name.
    """
    sheet_data = connect_to_sheet(sheet_name)

    table = PrettyTable()
    table.field_names = sheet_data[0]

    cars_in_stock = create_car_instances(sheet_data[1:])
    for car in cars_in_stock:
        table.add_row(car.car_as_list())

    print(table)
    
def display_car_info(sheet_name, id):
    """ 
    Displays a single cars info.
    Loops through all cars in the sheet to check for ID and
    prints an error message if ID does not exist.
    """
    sheet_data = connect_to_sheet(sheet_name)
    cars_in_stock = create_car_instances(sheet_data[1:])
    
    for car in cars_in_stock:
        
        if int(car.id) == id:
            car.display_info()
            return True

    print(f"ID number {id} not found.")
    return False
        