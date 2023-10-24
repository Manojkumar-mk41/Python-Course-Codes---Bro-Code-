 #Sort Method

my_list = ['Luffy','Zoro','Sanji']
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

#Sort Function

my_tuple = ('Nami','Usopp','Chopper')
print(my_tuple)
sorted_list = sorted(my_tuple)
print(sorted_list)
sorted_list = sorted(my_tuple,reverse=True)
print(sorted_list) 

#list of tuples - Sort Method

list_2 = [('Luffy',19,'Pirate'),('Zoro',21,'Swordman'),('Sanji',21,'Cook')]
attr = lambda attr:attr[0]
list_2.sort(key=attr)
print(list_2)

attr = lambda attr:attr[1]
list_2.sort(key=attr)
print(list_2)

attr = lambda attr:attr[2]
list_2.sort(key=attr,reverse=True)
print(list_2)

#Tuple of tuples - Sorted Function

tuple_2 = (('Nami',20,'Navigator'),('Usoop',20,'Sniper'),('Chopper',17,'Doctor'))
attr = lambda attr:attr[0]
sorted_tuple = sorted(tuple_2,key=attr)
print(sorted_tuple)

tuple_2 = (('Nami',20,'Navigator'),('Usoop',20,'Sniper'),('Chopper',17,'Doctor'))
attr = lambda attr:attr[1]
sorted_tuple = sorted(tuple_2,key=attr)
print(sorted_tuple)

tuple_2 = (('Nami',20,'Navigator'),('Usoop',20,'Sniper'),('Chopper',17,'Doctor'))
attr = lambda attr:attr[2]
sorted_tuple = sorted(tuple_2,key=attr,reverse=True)
print(sorted_tuple)