
class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def displayInfo(self):
        print(f"Name:{self.name}")
        print(f"Emp ID:{self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id,department):
        super().__init__(name, emp_id)
        self.department=department

    def displayInfo(self):
        super().displayInfo()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, emp_id,programmingLang):
        super().__init__(name, emp_id)
        self.programmingLang=programmingLang

    def displayInfo(self):
        super().displayInfo()    
        print(f"Programming Language:{self.programmingLang}")


manager1=Manager("Nischal","145","Enginnering")        
manager1.displayInfo()
print("\n")
developer1=Developer("Narayan","41","Computer Enginnering")        
developer1.displayInfo()

