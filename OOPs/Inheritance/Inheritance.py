class Animal:
    alive = True

    def eat(self):
        print("It can eat")

    def sleep(self):
        print('It can sleep')

class Lion(Animal):
    def walk(self):
        print('It can walk')

class Shark(Animal):
    def swim(self):
        print('It can swim')

class Hawk(Animal):
    def fly(self):
        print('It can fly')

lion = Lion()
shark = Shark()
hawk = Hawk() 

print(lion.alive)
lion.eat()
lion.sleep()
lion.walk()

print(shark.alive)
shark.eat()
shark.sleep()
shark.swim()

print(hawk.alive)
hawk.eat()
hawk.sleep()
hawk.fly()