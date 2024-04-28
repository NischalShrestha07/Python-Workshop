# class Student:
#     def __init__(slef,name):
#         print("Inside Constructor")
#         slef.name=name
#         print("All variable Initilized")

# # Instance Method
#     def show(self):
#         print("Hello,my name is",self.name)
# s1=Student('Ramesh')        
# s1.show()


# Number 2:
# class Company:
#     def __init__(self):
#         self.name="PYnative"
#         self.address="Rajatpur"

#     def show(self):
#         print(f"Name: {self.name}")    
#         print(f"Address: {self.address}")    


# print("")
# # Creating the object of the class
# cmp=Company()        
# cmp.show()


# Number 3
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def show(self):
        print(f"Name: {self.name}")    
        print(f"Age: {self.age}years old.")    
        print(f"Address: Rs{self.salary}")    
print("")
name1=Employee("Nishan",42,250000)
name1.show()

print("")
name2=Employee('Krishna',10,120)
name2.show()