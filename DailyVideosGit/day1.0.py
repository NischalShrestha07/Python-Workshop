class Student:
    def __init__(self,name,age):
        self.name=name
        # private member
        self.__age=age
    def get_age(self):
        return self.__age    

    def set_age(self,age):
        self.__age=age
   
print("")     
std=Student('Nischal',150)        
print(f'Name: {std.name}')
print(f'Age: {std.get_age()}')


std.set_age(153)

