class Car:

    def start(self):
        print('Car Started')
        return self
    
    def drive(self):
        print('Car is Driving')
        return self
    
    def brake(self):
        print('Applying Brake')
        return self
    
    def stop(self):
        print('Car is Stopped')
        return self
    
car = Car()

car.start().drive().brake().stop()
