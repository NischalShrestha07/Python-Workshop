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


class Car(Vehicle):
    def __init__(self, name, model, year, color, price):
        super().__init__(name, model, year, color, price)
        