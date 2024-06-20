from sheets_utils import *
from input_validation import *
from prettytable import PrettyTable
from datetime import datetime


def search_car_by_criteria():
    """
    Search for a car by criteria.
    Gets the list of cars in stock and asks
    the user to input a list of desired criteria.
    Creates a table of cars with matching criteria.
    """
    data = get_sheet_data("stock")
    stock_cars = create_car_instances(data[1:])
    matching_cars = []

    while matching_cars == []:
        search_terms = get_list_input("Enter search terms separated " +
                                      "by comma's (E.g. 'Red, Ford,' " +
                                      "or '2020, white, volvo'): ")

        # loops through cars and checks if they
        # contain the given criteria/terms
        for car in stock_cars:
            term_found = False
            for term in search_terms:
                if term in [str(value).lower() for value in car.car_as_list()]:
                    term_found = True
                    break
            if term_found:
                matching_cars.append(car)

        # if no cars are found, display a message
        # else create a table of cars and display to the terminal
        if matching_cars == []:
            print(f"No Matches found for: {search_terms}")
            continue
        else:
            table = PrettyTable()
            table.field_names = table.field_names = [
                "ID", "Make", "Model", "Year", "Colour", "Status", "Price"]
            for car in matching_cars:
                table.add_row(car.car_as_list()[:7])
            print(table)


def generate_sales_report(sheet_name):
    # function to create and display a sales report from a sheet
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

        # loops through all the cars in the sheet
        for car in sold_cars:
            # adds to profit to total profit
            total_profit += car.calculate_profit()
            # adds repairs to total repairs
            total_repairs += int(car.repairs)
            # adds cost to total cost
            total_purchase_costs += int(car.cost)
            # adds sales price to total takings
            total_takings += int(car.sold_price)

            # checks if the current car has the
            # highest or lowest profit in the sheet
            if int(car.calculate_profit()) > highest_profit[1]:
                highest_profit = (car.id, int(car.calculate_profit()))
            if int(car.calculate_profit()) < lowest_profit[1]:
                lowest_profit = (car.id, int(car.calculate_profit()))

        # calculates the average profit per car
        average_profit = int(total_profit / number_of_car_sold)
        # calculates the gross profit, before repair costs
        gross_profit = total_takings - total_purchase_costs
        # calculates net profit after repair costs
        net_profit = total_takings - (total_purchase_costs + total_repairs)

        # generates the reports and displays the information
        # in an easy to read format to the user
        print(f"Sales Report for {sheet_name}")
        print("----------")
        print(f"Number of car sold: {number_of_car_sold}")
        print(f"Total Months Profit: £{total_profit}")
        print("")
        print(f"Average Profit: £{average_profit} per car")
        print(f"Highest Profit Car: ID - {highest_profit[0]}, " +
              f"Profit - £{highest_profit[1]}")
        print(f"Lowest Profit Car: ID - {lowest_profit[0]}, " +
              f"Profit - £{lowest_profit[1]}")
        print("")
        print(f"Total Takings: £{total_takings}")
        print(f"Total car purchase costs: £{total_purchase_costs}")
        print(f"Total Repair Costs: £{total_repairs}")
        print("")
        print(f"Gross Profit: £{gross_profit}")
        print(f"Net Profit (gross minus repairs): £{net_profit}")
        return True
    except Exception as e:
        # False return is handled when the function is called.
        print("Error: Missing Data")
        print(f"Details: {e}\n")
        return False


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
    """
    Returns a new sheet name using the current month and year
    """
    while True:
        current_year = datetime.now().year
        user_year = get_integer_input("Enter the year number (e.g. 2024): ")

        if not (2022 < user_year <= current_year):
            print("Invalid year.")
            continue

        user_month = get_integer_input("Enter the month number " +
                                       "(e.g. '2' for feb): ")
        if not (1 <= user_month <= 12):
            print("Invalid month.")
            continue
        break

    return f"sold-{user_month}-{user_year}"


def display_deliveries_table(delivery_status=[
        "scheduled", "requested", "delivered"]):
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


def delivery_request():
    """
    Creates delivery request for a car, asks the user to enter
    the car ID and confirm delivery request
    """
    answer = "n"
    while True:
        if answer == "n":
            car_to_deliver = find_car_by_id("stock")

        answer = input("Would you like to continue? (y/n): \n")
        if answer == "y":
            car_to_deliver.request_delivery()
            return
        elif answer == "n":
            clear_terminal()
            print("Cancelled.")
            continue
        else:
            print("Not a valid entry, please try again.")


def get_new_car_details():
    """
    Returns car information as a list. In the same order as the Google Sheet.
    [id, make, model, year, colour, status, price, cost, repairs]
    Asks the user to enter all the required information to add a car to
    the stock sheet.
    """
    answer = "n"

    while True:

        if answer == "n":
            make = get_string_input("Enter the vehicle's make " +
                                    "(e.g. Ford, Volvo): ")
            # Vehicles models can contain letters,
            # numbers and special characters. No validation required.
            model = input("Enter the vehicle's model " +
                          "(e.g. focus, C40): \n").capitalize()
            year = get_year_input("Enter the vehicle's year of production " +
                                  "(e.g. 2017, 1999): ")
            colour = get_colour_input("Enter the vehicle's colour " +
                                      "(e.g. black, orange): ")
            status = get_location_input("Enter the vehicle's current " +
                                        "location (leeds, liverpool, " +
                                        "manchester, preston, york): ")
            cost = get_integer_input("Enter the vehicle's cost / price " +
                                     "paid (whole numbers only, " +
                                     "e.g. 15000, 7500): £ ")
            repairs = get_integer_input("Enter the vehicle's " +
                                        "cost of repairs, 0 if none " +
                                        "(whole numbers only, " +
                                        "e.g. 250, 400): £ ")
            price = get_price_input("Enter the vehicle's list " +
                                    "price (whole numbers only, " +
                                    "e.g. 22000, 12500): £ ", cost, repairs)
            id = generate_unique_id()

            car = [id, make, model, year,
                   colour, status, price, cost, repairs]

            clear_terminal()
            print("- Entered Details Summary -")
            table = PrettyTable()
            table.field_names = ["ID", "Make", "Model", "Year",
                                 "Colour", "Status", "Price",
                                 "Cost", "Repairs"]
            table.add_row(car)
            print(table)

        # Asks the user to confirm the input
        answer = input("Confirm details are correct (y/n): \n").lower()
        if answer == "y":
            return car
        elif answer == "n":
            clear_terminal()
            print("Cancelled.")
            continue
        else:
            print("Error: Invalid Entry.")
