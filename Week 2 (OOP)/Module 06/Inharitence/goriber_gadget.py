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
    
class Phone:
    def __init__(self, brand , price, color, dual_sim) -> None:

        self.dual_sim = dual_sim
        pass
    
    def phone_Call(self,number, text):
        return f'Sending SMS to {number} with : {text}'
    

class Camera:
    def __init__(self,brand, price, color, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass