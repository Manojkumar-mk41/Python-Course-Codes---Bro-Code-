friends = [('Luffy',17),
           ('Zoro',19),
           ('Nami',18),
           ('Usopp',17),
           ('Sanji',19),
           ('Chopper',15)]

age = lambda data:data[1] >= 18

voters = list(filter(age,friends))
print(voters)