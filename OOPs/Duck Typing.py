class Duck:

    def walk(self):
        print("The Duck is walking")


    def talk(self):
        print("The Duck is quaking")

class Chicken:

    def walk(self):
        print("The Chicken is walking")


    def talk(self):
        print("The Chicken is clucking")

class Person:

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("You caught the bird")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)