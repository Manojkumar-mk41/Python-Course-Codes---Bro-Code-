store = [('Shirt',20),('Pant',30),('TShirt',10),('Shoe',40)]

discount_50 = lambda data:(data[0], data[1] / 2)

discounted_price = list(map(discount_50,store))

print(discounted_price)