class Person:
    def __init__(self,firstName,middleName,lastName):
        self.firstName=firstName
        self.middleName=middleName
        self.lastName=lastName

    def printName(self):
        print(self.firstName,self.middleName,self.lastName)

data=Person("Nischal","Narayan","Shrestha")  
data.printName()
        