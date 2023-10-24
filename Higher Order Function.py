#Accepts functon as an argument
def big(text):
    return text.upper()

def small(text):
    return text.lower()

def hello(func):
    text = func('Hello World')
    print(text)

hello(big)
hello(small)

#return a function

def divider(x):
    def divident(y):
        return y / x
    return divident

divide = divider(2)
print(divide(10))