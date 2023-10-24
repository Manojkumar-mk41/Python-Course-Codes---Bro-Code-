city_temp_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

city_temp_C = {key: round((value-32)*(5/9)) for (key,value) in city_temp_F.items()}
print(city_temp_C)


names = {'Luffy': 17, 'Zoro': 19, 'Sanji': 19}

voters = {key: value for (key, value) in names.items() if value >= 18}
print(voters)


names = {'Luffy': 17, 'Zoro': 19, 'Sanji': 19}

voters = {key: ('Voter' if value >= 18  else 'Non voter') for (key, value) in names.items()}
print(voters)



def age(value):
    if value >= 18:
        return 'Voter'
    
    else:
        return 'Non Voter'

names = {'Luffy': 17, 'Zoro': 19, 'Sanji': 19}

voters = {key: age(value) for (key, value) in names.items()}
print(voters)