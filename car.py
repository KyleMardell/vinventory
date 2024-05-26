from prettytable import PrettyTable

class Car:
    
    def __init__(self, id, make, model, year, milage, engine, colour, status, price, cost, repairs):
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
        
    def car_as_list(self):
        return [self.id, self.make, self.model, self.year, self.milage, self.engine, self.colour, self.status, self.price, self.cost, self.repairs]
        
    def display_info(self):
        table = PrettyTable()
        table.field_names = ["ID", "Make", "Model", "Year", "Milage", "Engine", "Colour", "Status", "Price", "Cost", "Repairs"]
        table.add_row(self.car_as_list())
        print(table)
        
def create_car_instances(car_data):
    cars = []
    for data in car_data:
        car = Car(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        cars.append(car)
    return cars