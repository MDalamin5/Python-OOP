from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, ) -> None:
        self.name = name


# *******
class Customer(User):
    def __init__(self, name, money) -> None:
        self.wallet = money
        self.__order = None
        super().__init__(name)

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(sefl, order):
        sefl.__order = order 

    def place_order(self, order):
        self.order=order
        print(f"{self.name} Place an Order {order.items}")

    def eat_food(self, order):
        print(f"{self.name} item food {order.items}")

    def pay_for_order(self, amount):
        # TODO: submit the moner to the manager
        pass

    def give_tips(self, tips_amount):
        pass

    def write_review(self, stars):
        pass