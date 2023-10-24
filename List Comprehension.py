squares = [i*i for i in range(1,11)]
print(squares)

marks = [0,10,20,30,40,50,60,70,80,90,100]

pass_mark = [i for i in marks if i >= 50]

print(pass_mark)



marks_2 = [0,10,20,30,40,50,60,70,80,90,100]

pass_mark_2 = ['Pass' if i >= 50 else 'Fail' for i in marks ]

print(pass_mark_2)