class Employee:
    def __init__(self,name):
        self.name=name
    def calculateSalary(self):
        pass    
class FullTimeEmployee(Employee):
    def calculateSalary(self):
        return 50000    

class PartTimeEmployee(Employee):
    def calculateSalary(self):
        return 25000
employees=[FullTimeEmployee('Nischal'),PartTimeEmployee('Prinka')]        
for employee in employees:
    print(f"{employee.name}'s salary:",employee.calculateSalary())
