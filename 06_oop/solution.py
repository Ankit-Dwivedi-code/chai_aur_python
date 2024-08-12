class Car:

    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1

    def full_name(self):
        return self.__brand + " " + self.__model
    
    def get_brand(self):
        return self.__brand + "!"
    
    def fuel_type(self):
        return "Petrol or deisel"
    
    @staticmethod
    def car_desc():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

my_car = Car('Toyota', 'Camry')
# print(my_car.__brand)
# print(my_car.full_name())
# my_car.model = "bmw" //Can not be changed

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Battery"

my_new_car = ElectricCar("Tata", "Tiago ev", "70kwh")
# print(my_new_car.battery_size)
# print(my_car.fuel_type())
# print(Car.total_cars)
# print(Car.car_desc())

# print(my_car.model()) 
# print(my_car.model)

print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))
print(isinstance(my_new_car, ElectricCar))
print(isinstance(my_new_car, Car))

# Multiple inheritance

class Battery:
    def battery_info(self):
        return "Battery health is good"

class Engine:
    def engine_info(self):
        return "Engine health is good"
    
class Tesla(Car, Battery, Engine):
    pass

new_tesla = Tesla("Tesla", "Model S")
print(new_tesla.engine_info())
print(new_tesla.battery_info())