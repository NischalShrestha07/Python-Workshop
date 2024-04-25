    
    
 # those functions which are inside the class are called METHODS
# class calculation:
#     def add(self,a,b):
#         return 1+1 

# calculator=calculation()
# result=calculator.add(2,2)
# print(result)



class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):    
        print("I can Eat")
        
    def sleep(self):    
        print("I can Sleep")
class Dog(Animal):
    def bark(self):
        print("I can Bark.")
 
 
dog1=Dog("BullDog")       
dog1.eat()
   