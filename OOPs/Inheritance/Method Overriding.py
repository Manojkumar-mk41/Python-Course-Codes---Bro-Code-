class Animal:

    def eat(self):
        print('It will eat')

class Rabbit(Animal):

    def eat(self):
        print('It will eat carrots')

rabbit = Rabbit()

rabbit.eat()