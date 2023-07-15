from abc import ABC, abstractmethod
# abstract base class


class Animal(ABC):
    @abstractmethod
    def eat(self):
        print(f'hello i eat only Brieaney')
        print('Hey nana!! i\'m eating Banana')

    @abstractmethod
    def move(self):
        pass


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name
        self.catagory = 'Monkey'
        super().__init__()

    def eat(self):
       print('Hey Na nana, i am eating Banana')
    
    def move(self):
        return super().move()



mirpur_banor = Monkey('Lika')

mirpur_banor.eat()