name = "Gautam"
age = 22
print("%s is %d years old" % (name, age))

languages = ['Hindi', 'Punjabi', 'English']

print("Known Languages are %s" % languages)
print(', '.join(languages))

pi = 3.14159
print("value of pi at 2 digits is: %.2f" % pi)
print("age in hex is: %x" % age)

MultilineString = '''This is
multiline 
string
'''

print(MultilineString)
print("This" in MultilineString)
print(MultilineString.index("multi"))
print(MultilineString.find("multi"))

pi = "3.14"
print(pi.isdigit())
print(f"{pi}")

number = 123
print("{number}".format(number = number))

print(MultilineString[2:10:2])
print(name.upper())
print(MultilineString.startswith("This"))
print(MultilineString.split())