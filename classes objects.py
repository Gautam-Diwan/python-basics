from abc import ABC, abstractmethod

class Person:
    name = "Gautam Diwan"
    age = 22

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @abstractmethod
    def show(self):
        pass

class Employee(Person):
    id = 719

    def __init__(self, name="Gautam Diwan", age = 22, id = 0):
        super().__init__(name, age)
        self.id = id

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def __setId(self, id):
        self.id = id
    
class Book: pass
    
employee = Employee()
print(employee.getName())
newEmployee = Employee("Raj", 25, 111)
print(newEmployee.getName())
newEmployee.show()

print(Person.add(10, 20))

