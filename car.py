from prettytable import PrettyTable

class Car:
    id = 0
    
    def generate_id():
        Car.id += 1
        return Car.id
    
    def __init__(self, make, model, year, milage, engine, colour, status, price, cost, repairs):
        self.id = Car.generate_id()
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
        
    def display_info(self):
        table = PrettyTable()
        table.field_names = ["ID", "Make", "Model", "Year", "Milage", "Engine", "Colour", "Status", "Price", "Cost", "Repairs"]
        table.add_row([self.id, self.make, self.model, self.year, self.milage, self.engine, self.colour, self.status, self.price, self.cost, self.repairs])