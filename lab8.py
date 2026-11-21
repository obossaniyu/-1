
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def Info(self):
        pass

    @abstractmethod
    def FuelConsumption(self):
        pass

class Car(Vehicle):
    def Info(self):
        print("Легковой автомобиль:", self.brand)

    def FuelConsumption(self):
        return 8.0

class Truck(Vehicle):
    def Info(self):
        print("Грузовой автомобиль:", self.brand)

    def FuelConsumption(self):
        return 25.0


class Motorcycle(Vehicle):
    def Info(self):
        print("Мотоцикл:", self.brand)

    def FuelConsumption(self):
        return 4.0


car = Car(input("Введите марку автомобиля: "))
truck = Truck(input("Введите марку грузовика: "))
motorcycle = Motorcycle(input("Введите марку мотоцикла: "))

vehicles = [car, truck, motorcycle]

distance = float(input("Введите расстояние (км): "))

for vehicle in vehicles:
    print()
    vehicle.Info()

    consumption = vehicle.FuelConsumption()
    fuel = consumption * distance / 100

    print(f"Расход топлива: {consumption} л/100 км")
    print(f"Необходимо топлива: {fuel:.2f} л")
