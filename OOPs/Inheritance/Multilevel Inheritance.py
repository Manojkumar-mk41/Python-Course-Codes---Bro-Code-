class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print('It can eat')

class Dog(Animal):
    def bark(self):
        print("It can bark")

dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()