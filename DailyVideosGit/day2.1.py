# class Employee:
#     count=0
#     def __init__(self):
#         Employee.count=Employee.count+1


# # Creatiing Objects
# c1=Employee()
# c2=Employee()
# c3=Employee()
# print("")
# print("The number of Employee:",Employee.count)


class Student:
    # one argument Constructor
    def __init__(self,name):
        print("\nOne Arguments Constructors.")
        self.name=name

    # one argument Constructor
    def __init__(self,name,age):
        print("\nTwo Arguments Constructor.")
        self.name=name
        self.age=age

# First Object Created
std=Student("Nischal",21)



# First Object Created
std2=Student("Manish",22)

