numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None

numbers.append(1)
numbers.append(2)
numbers.append(3)

names.append('hello')
names.append('world')

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print(numbers[-1])

from random import shuffle
print(names)
shuffle(names)
print(names)