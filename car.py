from prettytable import PrettyTable


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
            profit = int(self.sold_price) - (int(self.cost) + int(self.repairs))
            return profit
        except ValueError as e:
            print(f"Error converting to int: {e}")

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
