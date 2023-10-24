import functools

letter = ['H','E','L','L','O']

word = functools.reduce(lambda x, y:x + y, letter)
print(word)

nums = [1,2,3,4,5,6,7,8,9,10]

sum = functools.reduce(lambda x, y:x + y, nums)
print(sum)