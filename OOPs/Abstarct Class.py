from abc import ABC, abstractclassmethod

class Vehicle(ABC):

    @abstractclassmethod
    def go(self):
        print('Vehicle is Going')

class Car(Vehicle):

    def go(self):
        print('Car is Going')

    def name(self):
        print('This is car')

class Bike(Vehicle):

    def go(self):
        print('Bike is Going')

    def name(self):
        print('This is Bike')

car = Car()
bike = Bike()

car.go()
bike.go()

car.name()
bike.name()


