def greetings(name, age):
    print("Name is " + name + " and age is " + str(age))

greetings("Gautam", 22)
greetings(name="Gautam Diwan", age=22)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("5! = " + str(factorial(5)))

values = [1,2,3]

multiples = list(map(lambda x: x * 2, values))
print(multiples)

def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Hello", " ", "World!"))

def printItems(**kwargs):
    for key, item in kwargs.items():
        if isinstance(item, dict):
            printItems(**item)
        else:
            print(key, item)

printItems(name = "Gautam", age = "22", language = "Python")