

class Student:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
     
    def printName(self):
         print(f"FIRSTNAME:- {self.firstName}")   
         print(f"LASTNAME:- {self.lastName}")   
       
       
class studentInfo(Student):
    def age(self):
        print(F"AGE: {self.age}")        

        




details=Student("Nischal","Shrestha")
details.printName()
