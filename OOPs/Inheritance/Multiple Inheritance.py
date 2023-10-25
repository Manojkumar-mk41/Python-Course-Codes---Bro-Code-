class Prey:

    def flee(self):
        print('It will flee')

class Predator:

    def hunt(self):
        print('It will hunt')        

class Frog(Prey):
    pass

class Snake(Prey,Predator):
    pass

class Eagle(Predator):
    pass

frog = Frog()
snake = Snake()
eagle = Eagle()

frog.flee()
eagle.hunt()
snake.flee()
snake.hunt()