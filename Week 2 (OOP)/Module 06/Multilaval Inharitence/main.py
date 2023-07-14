class Veacle:
    def __init__(self,name, price) -> None:
        self.name = name
        self.price = price
    
    def move():
        pass
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.price}'

class Bus(Veacle):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Veacle):
    def __init__(self, name, price,weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'Name: {self.name}, Price of the bus: {self.price}, No of seat have: {self.seat}, Temputure: {self.temperature}')
        return super().__repr__()


green_line = ACBus('Volvo', 50000000, 24, '20 degree')
print(green_line)
