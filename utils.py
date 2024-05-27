from sheets_utils import *
from input_validation import *
from prettytable import PrettyTable
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

def find_car_by_id():
    """ 
    Search for a car by ID number
    """
    found_id = False
    while not found_id:
        input_id = get_integer_input("Please enter a valid ID number: ")
        found_id = display_car_by_id("stock", input_id)
        
def search_car_by_criteria():
    """ 
    Search for a car by criteria.
    Gets the list of cars in stock and asks the user to input a list of desired criteria. 
    Creates a table of cars with matching criteria.
    """
    data = connect_to_sheet("stock")
    stock_cars = create_car_instances(data[1:])
    matching_cars = []
    
    while matching_cars == []:
        
        search_terms = get_list_input("Enter search terms / desired features separated by comma's. (E.g. 'Red, Ford,' or '2020, white, volvo') ")

        for car in stock_cars:
            term_found = False
            for term in search_terms:
                if term in [str(value).lower() for value in car.car_as_list()] and car.status.lower() != "reserved":
                    term_found = True
                    break
            if term_found:
                matching_cars.append(car)
            
        if matching_cars == []:
            print("No matches found.")
            continue
        else:
            table = PrettyTable()
            table.field_names = table.field_names = ["ID", "Make", "Model", "Year", "Milage", "Engine", "Colour", "Status", "Price", "Cost", "Repairs"]
            for car in matching_cars:
                table.add_row(car.car_as_list()[:11])
            print(table)