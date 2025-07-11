from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("the car has four wheels")
    
class Bike(Vehicle):
    def start(self):
        print("The bike as two wheels")


car=Car()

bike=Bike()

car.start()

bike.start()