
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
        return 3014*self.radius**2    
