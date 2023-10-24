double = lambda x: x*2
multi = lambda x, y:x * y
add = lambda a, b, c:a + b + c
name = lambda fname, lname:fname + " " + lname
age_check = lambda x:True if x>=18 else False

print(double(5))
print(multi(5,4))
print(add(1,2,3))
print(name('God','Usopp'))
print(age_check(19))