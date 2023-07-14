#  base class , parent class, common attribute + functiionality class
# drive class , parent class, uncommon attribut class

class Gadget:
    def __init__(self, brand, price, color, orgin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.orgin = orgin
    
    def run(self):
        return f'Running Laptop{self.brand}'




class Laptop:
    def __init__(self,brand, price, color, memory) -> None:
        self.memory = memory

    def codding(self):
        return f'learning python and practicing'
    
class Phone(Gadget):
    def __init__(self,brand, price, color, orgin,dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,orgin)
    
    def phone_Call(self,number, text):
        return f'Sending SMS to {number} with : {text}'
    
    def __repr__(self) -> str:
       return f'Phone Brand: {self.brand}, Price: {self.price}, Color: {self.color}, Duel sim: {self.dual_sim}'
    
    

class Camera:
    def __init__(self,brand, price, color, pixel) -> None:
        self.pixel = pixel
        

    def change_lens(self):
        pass

# inharitance

my_phone = Phone('iPhone', '3454', 'Black', 'Canada',True)
print(my_phone.brand)
print(my_phone)
