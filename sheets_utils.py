import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable

def connect_to_sheet():
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
    return SHEET

def display_sheet_as_table(sheet_name):
    """
    Displays a worksheet as a table.
    Requires sheet data from connect_to_sheet method and
    worksheet name.
    """
    SHEET = connect_to_sheet()
    current_sheet = SHEET.worksheet(sheet_name)
    sheet_data = current_sheet.get_all_values()

    table = PrettyTable()
    table.field_names = sheet_data[0]

    for row in sheet_data[1:]:
        table.add_row(row)

    print(table)
    
def display_car_info(sheet_name, id):
    """ 
    Displays a single cars info.
    Loops through all cars in the sheet to check for ID and
    prints an error message if ID does not exist.
    """
    SHEET = connect_to_sheet()
    current_sheet = SHEET.worksheet(sheet_name)
    sheet_data = current_sheet.get_all_values()
    
    for row in sheet_data[1:]:
        table = PrettyTable()
        table.field_names = sheet_data[0]
        
        if int(row[0]) == id:
            table.add_row(row)
            print("Chosen car - ")
            print(table)
            return True

    print(f"ID number {id} not found.")
    return False
        