from math import factorial
class Phitron:
    def __init__(self,a, b, c) -> None:
        self.a = a
        self.b = b
        self.c =c
        
    def sum(self):
        return self.a + self.b+ self.c
    
    def factorial(self):
        return factorial(self.b)
    

obj = Phitron(2,5,7)
print(obj.sum())
print(obj.factorial())
    
