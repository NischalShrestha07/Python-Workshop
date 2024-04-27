class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        # this is lower-level method as this is hidden and another getter is setted.  
    def calcualte_perimeter(self):
        return 2*(self.length+self.width)    
    
    # this is higher-level method as this methods helps to abstract the actual data in calcualte_perimeter() method.  .  
    # So "calcualte_perimeter()" is not accessed by the user and "get_perimeter()" can be accessed.
    def get_perimeter(self):
        return self.calcualte_perimeter()    
    
rectangle=Rectangle(4,2)    
# here "calcualte_perimeter()" is not taken as its the main data which shouldn't be access or changed 
# So "get_perimeter()" is made a getter which helps to abstract the data from users.

perimeter=rectangle.get_perimeter()