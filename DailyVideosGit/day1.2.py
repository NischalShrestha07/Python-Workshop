

class Student:
    def __init__(self,name,rollno,age):
        # private member
        self.name=name
        #private members to restrict access
        # avoid direct data modifications 
        self.__rollno=rollno
        self.__age=age

    def show(self):
        print(f"Student Name: {self.name}")    
        print(f"Student Rollno: {self.__rollno}")    
    def get_Rollno(self):
        return self.__rollno    
def set_Rollno(self,number):
    if number >50:
        print("Invalid Rollno.Please set correct rollno.")        
    else:
        self.__rollno=number    


name=Student("Ramos",41,21)
name.show()

name.set_Rollno(120)
name.show()