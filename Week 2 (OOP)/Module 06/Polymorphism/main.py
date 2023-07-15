# poly ---> many
# morph ---> shape

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('Animal make sound')
    
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('mawwwwww mawwww meowwww')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('Gawww gawwww')


class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    




don = Cat('Real Don')
don.make_sound()

jarman_saferd = Dog('Kalu')
jarman_saferd.make_sound()

jon = Goat('Lamu')
jon.make_sound()

animals = [don, jarman_saferd, jon]

for animal in animals:
    animal.make_sound()
    