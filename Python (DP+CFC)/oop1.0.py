    
    
 # those functions which are inside the class are called METHODS
# class calculation:
#     def add(self,a,b):
#         return 1+1 

# calculator=calculation()
# result=calculator.add(2,2)
# print(result)



# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):    
#         print("I can Eat")
        
#     def sleep(self):    
#         print("I can Sleep")
# class Dog(Animal):
#     def bark(self):
#         print("I can Bark.")
 

# dog1=Dog("BullDog")       
# dog1.eat()
   
   
class Vehicle:
    def __init__(self,carName,carBrand,carPrice,carColor):
        self.carName=carName
        self.carBrand=carBrand
        self.carPrice=carPrice
        self.carColor=carColor
    def move(self):
        print("Car is Moving.")    
    def stop(self):
        print("Car has Stopped.")    
    def fuel(self):
        print("Car needs Fuels.")    

    def printCarDetails(self):
        # print(self.carName,self.carBrand,self.carPrice,self.carColor)
        print(f"CarName:{self.carName}")
        print(f"CarBrand:{self.carBrand}")
        print(f"CarPrice:{self.carPrice}")
        print(f"CarColor:{self.carColor}")

class Car(Vehicle):
    def slowSpeed(self):
        print("Car is Slow.")        
        
car1=Car("Scorpio","Ford","2500000","Red")        
car1.slowSpeed()
car1.move()
car1.stop()
car1.fuel()
data=Vehicle("Lamborgani","Lambo","2500000","Red")
print("\n")

data.printCarDetails()