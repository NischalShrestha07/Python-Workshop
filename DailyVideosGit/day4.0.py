

class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    
    def show(self):
        print(f"Details:")    
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Price: Rs{self.price}")
    
    def max_speed(self):
        print("Vehicle max Speed is 150 MPH")

    def change_gear(self):
        print("Vehicle changed 6 gears.")   

            
class Car(Vehicle):
    def max_speed(self):
        print("Car max speed is 240 MPH")
    def change_gear(self):
        print("Car Changed 7 gears.")        

# /Car Object
car1=Car("Lambo","Red",2000000)        
car1.show()

# calls methods from Car class
car1.max_speed()
car1.change_gear()

# Vehicle Object:
print("")
vehicle=Vehicle("Truck204","Black",750000)
vehicle.show()

# calls method from a Vehicle Class
vehicle.max_speed()
vehicle.change_gear()



        