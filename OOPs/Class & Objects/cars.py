from car import Car

car_1 = Car('Audi','A4','White')
car_2 = Car('Nissan','GT','Black')

car_1.start()
car_2.drive()
car_1.stop()

'--------------------Class & Instance Variables -----------------------'

print(car_1.wheels)
print(car_2.wheels)

Car.wheels = 2
print(car_1.wheels)
print(car_2.wheels)

car_2.wheels = 3
print(car_1.wheels)
print(car_2.wheels)
