
class Laptop:
    def __init__(self,brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running Laptop{self.brand}'
    
    def codding(self):
        return f'learning python and practicing'
    
class Phone:
    def __init__(self, brand , price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim
        pass
    
    def run(self):
        return f'Phone running but {self.brand} Brand'
    
    def phone_Call(self,number, text):
        return f'Sending SMS to {number} with : {text}'
    

class Camera:
    def __init__(self,brand, price, color, pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel
    
    def run(self):
        pass

    def change_lens(self):
        pass