phonebook = {
    "Gautam" : 938477566,
    "Raj" : 938377264,
}
print(phonebook)

addresses = {}
addresses['abc'] = "Karnal"
addresses['def'] = "Delhi"

new_dict = {}
new_dict.update(phonebook)
new_dict.update(addresses)

print(new_dict)
print(phonebook | addresses)

for key in new_dict:
    print(key)

for key, value in new_dict.items():
    print(f'key: {key}, value: {value}')

print(new_dict.get("Rohit"))

new_dict.setdefault("Rohit", 9999)
print(new_dict['Rohit'])

new_dict['Rohit'] = 100
print(new_dict["Rohit"])

print(new_dict.pop('Rohit'))

new_dict.clear()
print(new_dict)

new_dict = dict(zip(phonebook, addresses))
print(new_dict)