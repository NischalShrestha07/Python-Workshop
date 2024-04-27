
#POLYMORPHISM DETAILS:
# when the same name methods are used in more than one class then its called method overriding.
# METHOD OVERRIDING OCCURS in polymorphism

# Example: pani lai maila Everest ma lage tyo freeze hunx tei pani maila tatooo thauma lage bafff auxa thats called polymorphism. Environment change garera tesko behaviours ma change lyaune


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def  __init__(self,radius):
        self.radius=radius
        # super().__init__()        
    def area(self):
        return 3.14*self.radius**2    
class Rectangle(Shape):
    def __init__(self,length,width):
        # super().__init__()
        self.length=length
        self.width=width

    
    def area(self):
        return self.length*self.width

def printArea(shape):
    print(f"Area: {shape.area()}")


# rectangle=Rectangle(5,2)    
# circle=Circle(4)

# printArea(rectangle)
# printArea(circle)
shapes=[Rectangle(5,2),Circle(4)]

for i in shapes:
    result=shapes[0]
    result2=shapes[1]
printArea(result)   
printArea(result2)   