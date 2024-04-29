


class Person:
    def __init__(self,name,gender,profession):
        self.name=name
        self.gender=gender
        self.profession=profession
        
        # Behaviour (Instance Methods)
    def show(self):
        print(f"Name: {self.name}")    
        print(f"Gender: {self.gender}")    
        print(f"Profession: {self.profession}")    
        # Behaviour (Instance Methods)

    def work(self):
        print(f"{self.name} working as a {self.profession}")


name1=Person('Nischal','Male','Hello')
print("\n")
name1.show()
name1.work()




   


    