print(n := 5)
print(name := 'Mano')



""" foods = list()
while True:
    food = input('Enter your Favourite food : ')
    if food.lower() == 'quit':
        break
    foods.append(food)
print(foods)
 """
foods = list()
while food := input('Enter your Favourite food : ') != 'quit':
    foods.append(food)
print(foods)

#Not expected Output