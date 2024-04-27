class Vehicle:
    def __init__(self,name,model,year,color,price):
        self.name=name
        self.model=model
        self.year=year
        self.color=color
        self.price=price
    def display_Info(self):
        print(f"Name: {self.name}")    
        print(f"Model: {self.model}")    
        print(f"Year: {self.year}")    
        print(f"Color: {self.color}")    
        print(f"Price: {self.price}")    

# super() is keyword which is used when we are inheriting the data from the parent class.
# super() aslo means as parent class(Vehicle)

class Car(Vehicle):
    def __init__(self, name, model, year, color, price,num_doors):
        super().__init__(name, model, year, color, price) 
        # pushing the data to above __init__
        self.num_doors=num_doors
        
    def display_Info(self):
         super().display_Info()    
         print(f"Numbers of Doors: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self,name,model,year,color,price,engine_size):
        super().__init__(name,model,year,color,price)
        self.engine_size=engine_size
        
    def display_Info(self):
         super().display_Info()
         print(f"Engine Size: {self.engine_size}")

# this data are passed in Parent class (Car) which has different attributes on it.
# And according to those attributes below the data are passed.
car=Car('Toyota','Model2806',2024,'Red',500000,4)
print("The Details of Car is listed below:")
car.display_Info()


print("\n")
print("The Details of Bike is listed below:")
bike=Bike("Kawasaki","M25GH",2024,"Green",1500000,"24HP")
bike.display_Info()