from math import pi

class Shape:
    def __init__(self) -> None:
        pass

    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self,height, length, width) -> None:
        self.height = height
        self.length = length
        self.width = width

    def getArea(self):
        return self.height*self.length*self.width
    

class Triangle(Shape):
    def __init__(self,height, length) -> None:
        self.height = height
        self.length = length
    
    def getArea(self):
        return 0.5 * self.height * self.length
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def getArea(self):
        return pi * self.radius * self.radius
    

rec_obj = Rectangle(2,3,5)
print(rec_obj.getArea())

tri_obj = Triangle(3,2)
print(tri_obj.getArea())

cir_obj = Circle(5)
print(cir_obj.getArea())
        
        