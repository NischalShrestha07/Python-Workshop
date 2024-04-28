
class Company:
    def __init__(self):
        self._project="NLP"

class Employee(Company):
    def __init__(self,name):
        self.name=name
        Company.__init__(self)
    
    
    def show(self):
        print("Employee Name:",self.name)
        print("Working on project:",self._project)
print('')

c=Employee("Jeesaa")
c.show()
print('')

print('Project',c._project)