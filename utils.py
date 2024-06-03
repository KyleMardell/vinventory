from sheets_utils import *
from input_validation import *
from prettytable import PrettyTable
import os
import platform
from datetime import datetime


def clear_terminal():
    """ 
    Checks the operating system and clears the terminal
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def search_car_by_criteria():
    """ 
    Search for a car by criteria.
    Gets the list of cars in stock and asks the user to input a list of desired criteria. 
    Creates a table of cars with matching criteria.
    """
    data = get_sheet_data("stock")
    stock_cars = create_car_instances(data[1:])
    matching_cars = []

    while matching_cars == []:
        search_terms = get_list_input(
            "Enter search terms separated by comma's (E.g. 'Red, Ford,' or '2020, white, volvo'): ")

        for car in stock_cars:
            term_found = False
            for term in search_terms:
                if term in [str(value).lower() for value in car.car_as_list()]:
                    term_found = True
                    break
            if term_found:
                matching_cars.append(car)

        if matching_cars == []:
            print(f"No Matches found for: {search_terms}")
            continue
        else:
            table = PrettyTable()
            table.field_names = table.field_names = [
                "ID", "Make", "Model", "Year", "Milage", "Engine", "Colour", "Status", "Price", "Cost", "Repairs"]
            for car in matching_cars:
                table.add_row(car.car_as_list()[:11])
            print(table)
        

def generate_sales_report(sheet_name):
    """ 
    Calculates all relevant sales data and
    displays in a report.
    """
    try:
        data = get_sheet_data(sheet_name)
        sold_cars = create_car_instances(data[1:])

        number_of_car_sold = len(sold_cars)
        total_profit = 0
        total_repairs = 0
        total_takings = 0
        total_purchase_costs = 0
        highest_profit = (0, 0)
        lowest_profit = (sold_cars[0].id, sold_cars[0].calculate_profit())

        for car in sold_cars:
            total_profit += car.calculate_profit()
            total_repairs += int(car.repairs)
            total_purchase_costs += int(car.cost)
            total_takings += int(car.sold_price)

            if int(car.calculate_profit()) > highest_profit[1]:
                highest_profit = (car.id, int(car.calculate_profit()))
            if int(car.calculate_profit()) < lowest_profit[1]:
                lowest_profit = (car.id, int(car.calculate_profit()))

        average_profit = int(total_profit / number_of_car_sold)
        gross_profit = total_takings - total_purchase_costs
        net_profit = total_takings - (total_purchase_costs + total_repairs)

        print(f"Sales Report for {sheet_name}")
        print("----------")
        print(f"Number of car sold: {number_of_car_sold}")
        print(f"Total Months Profit: £{total_profit}")
        print("")
        print(f"Average Profit: £{average_profit} per car")
        print(
            f"Highest Profit Car: ID - {highest_profit[0]}, Profit - £{highest_profit[1]}")
        print(
            f"Lowest Profit Car: ID - {lowest_profit[0]}, Profit - £{lowest_profit[1]}")
        print("")
        print(f"Total Takings: £{total_takings}")
        print(f"Total car purchase costs: £{total_purchase_costs}")
        print(f"Total Repair Costs: £{total_repairs}")
        print("")
        print(f"Gross Profit: £{gross_profit}")
        print(f"Net Profit (gross minus repairs): £{net_profit}")
    except:
        # Return None, as missing sheet error handled inside get_sheet_data function.
        # This stops the full error details being displayed to the user.
        return None


def get_current_sales_sheet_name():
    """ 
    Returns the current months sales sheet name
    """
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month
    sheet_name = f"sold-{current_month}-{current_year}"
    return sheet_name


def create_sheet_name():
    while True:
        current_year = datetime.now().year
        user_year = get_integer_input("Enter the year number (e.g. 2024): ")

        if not (2022 < user_year <= current_year):
            print("Invalid year.")
            continue

        user_month = get_integer_input(
            "Enter the month number (e.g. '2' for feb): ")
        if not (1 <= user_month <= 12):
            print("Invalid month.")
            continue
        break

    return f"sold-{user_month}-{user_year}"


def display_deliveries_table(delivery_status=["scheduled", "requested", "delivered"]):
    """ 
    Displays deliveries sheet as a table with provided delivery status,
    requires list of delivery status (can contain only 1 element).
    """
    sheet_data = get_sheet_data("deliveries")
    table = PrettyTable()
    table.field_names = sheet_data[0]
    for data in sheet_data[1:]:
        for status in delivery_status:
            if status in data:
                table.add_row(data)

    print(table)

def get_new_car_details():
    id = generate_unique_id()
    make = get_string_input("Enter the vehicle's Make (e.g. Ford, Volvo): ")
    # Model may contain letters, numbers and special characters. No validation required.
    model = input("Enter the vehicle's Model (e.g. focus, C40): ")
    year = get_year_input("Enter the vehicle's Year of production (e.g. 2017, 1999): ")
    
    
    print(id, make, model, year)
    return [id, make, model, year]