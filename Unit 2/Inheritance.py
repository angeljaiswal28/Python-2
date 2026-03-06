#Multiple Inheritance program , with User input 
class person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age
    
    def display_p(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age} years")

class employee:
    def __init__(self, id, sal):
        self.id = id      
        self.sal = sal 

    def display_e(self):
        print(f"Employee ID = {self.id}")
        print(f"Salary = {self.sal}")

class manager(person, employee):
    def __init__(self, name, age, id, sal, department):
        # Call parent constructors
        person.__init__(self, name, age)
        employee.__init__(self, id, sal)
        self.department = department 
        
    def display(self):
        print("\nManager Details:")
        self.display_p()
        self.display_e() 
        print(f"Department = {self.department}")

# Input section
n = input("Enter name: ")
a = int(input("Enter age in years: "))
i = input("Enter Employee ID: ")
s = int(input("Enter salary: "))
d = input("Enter department: ")

# Object creation
m = manager(n, a, i, s, d)
m.display() 
