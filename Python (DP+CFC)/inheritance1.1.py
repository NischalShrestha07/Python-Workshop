

class Vehicle:
    def __init__(self,name,brand,color,price):
        self.name=name
        self.brand=brand
        self.color=color
        self.price=price

    def move(self):
        print("The car is moving")   

    def stop(self):
        print("The car has stopped")   
    def display(self):
        print(f"name: {self.name}".capitalize())    
        print(f"brand: {self.brand}".capitalize())    
        print(f"color: {self.color}".capitalize())    
        print(f"price: {self.price}".capitalize())    
        # print(f"name: {self.name}")    
class Car(Vehicle):
     def __init__(self,name,brand,color,price,doors,wheels):
        super().__init__(name,brand,color,price)
        self.wheels=wheels
        self.doors=doors

     def display(self):
         super().display()       
         print(f"Numbers of Doors: {self.doors}")
         print(f"Numbers of Wheels: {self.wheels}")
         

class Safari(Vehicle):
    def __init__(self, name, brand, color, price,windows,wheels):
        super().__init__(name, brand, color, price)
        self.windows=windows
        self.wheels=wheels
     
    def display(self):
         super().display()   
         print(f"Numbers of Windows: {self.windows}")
         print(f"Numbers of Wheels: {self.wheels}")


car1=Car('Lamborgani','LAMBO','Red','250000','4 Windows','4 Wheels')         
car1.display()
print("\n")

Safari1=Safari("Toyata","Nischal",'Blue',"500000","No Windows","3 Wheels")
Safari1.display()
# def check(n):
#     if(n>18):
#         print('You are adult')
#     else:
#         print("You are child")    
  
# check(25)        
        
