class Employee:
    def __init__(self,name,em_id,salary):
        # _name the underscore(_) is given before so that these data cannot be accessed outside this class/any person.
        self._name=name
        self._em_id=em_id
        self._salary=salary


    def calculate_bonus(self):
        return self._salary*0.1    

# below getters/setter are used to access the data from the class
    def display_info(self):
        print(f"Name: ${self._name}") 
        print(f"Employee ID: ${self._em_id}") 
        print(f"Salary: ${self._salary}") 
        
        
# employee._name By this the data cannot be accessed as _ is used which means its encapsulated.
# So to get those data we need getter() function as we have made display_info() method
employee=Employee("Naruto",1,5000)        
employee.display_info()
bonus=employee.calculate_bonus()
print(f"The bonus amount is: ${bonus}")