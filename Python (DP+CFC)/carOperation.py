   
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


class Car(Vehicle):
    def slowSpeed(self):
        print("Car is Slow.")        
        
car1=Car("Scorpio","Ford","2500000","Red")        
car1.slowSpeed()
car1.move()
car1.stop()
car1.fuel()