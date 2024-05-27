from sheets_utils import *
from input_validation import *
from car import *
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
    car_found = False
    while not car_found:
        input_id = get_integer_input("Please enter a valid ID number: ")
        car_found = display_car_by_id("stock", input_id)
    return car_found
        
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
            
def generate_sales_report(sheet_name):
    data = connect_to_sheet(sheet_name)
    sold_cars = create_car_instances(data[1:])
    
    number_of_car_sold = len(sold_cars)
    total_profit = 0
    total_repairs = 0
    total_takings = 0
    purchase_costs = 0
    highest_profit = (0,0)
    lowest_profit = (sold_cars[0].id, sold_cars[0].calculate_profit())
    
    for car in sold_cars:
        total_profit += car.calculate_profit()
        total_repairs += int(car.repairs)
        purchase_costs += int(car.cost)
        total_takings += int(car.sold_price)
        
        if int(car.calculate_profit()) > highest_profit[1]:
            highest_profit = (car.id, int(car.calculate_profit()))
        if int(car.calculate_profit()) < lowest_profit[1]:
            lowest_profit = (car.id, int(car.calculate_profit()))
            
    average_profit = int(total_profit / number_of_car_sold)
    gross_profit = total_takings - purchase_costs
    net_profit = total_takings - (purchase_costs + total_repairs)
    
    print(f"Sales Report for {sheet_name}")
    print("----------")
    print(f"Number of car sold: {number_of_car_sold}")
    print(f"Total Months Profit to date: £{total_profit}")
    print("")
    print(f"Average Profit: £{average_profit} per car")
    print(f"Highest Profit Car: ID - {highest_profit[0]}, Profit - £{highest_profit[1]}")
    print(f"Lowest Profit Car: ID - {lowest_profit[0]}, Profit - £{lowest_profit[1]}")
    print("")
    print(f"Total Takings: £{total_takings}")
    print(f"Total car purchase costs: £{purchase_costs}")
    print(f"Total Repair Costs: £{total_repairs}")
    print("")
    print(f"Gross Profit: £{gross_profit}")
    print(f"Net Profit (after repairs): £{net_profit}")