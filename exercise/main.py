# Exercise with classes
# 1 - Create the class Car (Name)
# 2 - Create the class Engine (Name)
# 3 - Create the clas Manufacturer (Name)
# 4 - Create a connection where the Car has an Engine
# P.S: An Engine can be of many cars
# 5 -  Create a connection between Car and a Manufacturer
# P.S: A Manufacturer can build many cars
# Display the car's name, and its respective engine and manufacture

class Car:
    def __init__(self, name, engine):
        self.name = name
        self._engine = engine
        self.__manufacturer = None

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

    @classmethod
    def list_all_cars(cls, all_cars):
        for car in all_cars:
            print(f"*******\nCar: {car.name}\nEngine: {car.engine}\nManufacturer: {car.manufacturer}")


class Engine:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        

class Manufacture:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.__company_cars = []

    def list_company_cars(self):
        for car in self.__company_cars:
            print(f"***\nCar: {car.name}\nEngine:{car.engine.name}\nManufacturer:{self.name}")

    def build_car(self, car_name, car_engine):
        new_car = Car(car_name, car_engine)
        new_car.manufacturer = self.name
        self.__company_cars.append(new_car)
        all_cars.append(new_car)


all_cars = []
engine_1 = Engine(" Default Honda Engine", 5000)
manufacture1 = Manufacture("Honda", "Japan")
manufacture1.build_car(car_name="Honda Civic", car_engine=engine_1.name)
manufacture1.build_car(car_name="Honda City", car_engine=engine_1.name)
Car.list_all_cars(all_cars)
