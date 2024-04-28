class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

emp=Employee("Nischal","4000")

print(f"Name: {emp.name}")
print(f"Salary: ${emp.salary}")
print("")
emp.show()       