

class Employee:
    def __init__(self,name,salary,project):
        self.name=name
        self.salary=salary
        self.project=project


    def show(self):
        print(f"Name: {self.name}")   
        print(f"Salary: {self.salary}")   
        # print(f"Name: {self.name}")   

    def work(self):
        print(f"{self.name} is wprking on {self.project}" )    
        
emp=Employee('Nischal',45000,"Ecommerce")        

emp.show()
emp.work()
