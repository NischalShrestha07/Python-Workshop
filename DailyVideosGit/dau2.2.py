


# CONSTRUCTOR OVERLOADING

class Student:
    # One Arguments Constructor
    def __init__(self,name):
        print(" One Arguments Constructor")
        self.name=name


    # Two Arguments Constructor
    def __init__(self,name,age):
        print("Two Arguments Constructor")
        self.name=name
        self.age=age

        
std=Student("Nischal",21)        

std2=Student("Harry",30)



