


class Vehicle:
    def __init__(self,engine):
        print("Inside Vechicle Constructor")
        self.engine=engine


class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine,max_speed):
        super().__init__(engine)
        print("Inside Car Constructor.")
        self.max_speed=max_speed


class Electric_Car(Car):
# Constructor of ethe Electric Car
    def __init__(self,engine,max_speed,km_range):
        super().__init__(engine,max_speed)
        print("Inside Electric Car Constructor. ")
        self.km_range=km_range


elctricVehicle=Electric_Car('1500cc', 240, 750 )
print(f"Engine: {elctricVehicle.engine}")
print(f"Max_Speed: {elctricVehicle.max_speed}")
print(f"Km_Range: {elctricVehicle.km_range}")
