class Car:

    wheels = 4 #class variable

    def __init__(self,brand,model,color):
        self.brand = brand #instance variable 
        self.model = model #instance variable
        self.color = color #instance variable
    
    def start(self):
        print(f'{self.brand} {self.model} is gonna start')

    def drive(self):
        print(f'{self.color} color {self.model} car is driving')

    def stop(self):
        print(f'{self.color} color {self.brand} car is gonna stop')
