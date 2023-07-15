class Person:
    def __init__(self,name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('Alu vorta dal and rute')

    def excersise(self):
        raise NotImplementedError

 # '+' sign operator Overload
    
    def __add__(self, other):
        return self.age+other.age

    def __gt__(self, other):
        return self.age > other.age


class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # overriding
    def eat(self):
        print('Vagitable frutes, aslkdfj')

    # overriding
    def excersise(self):
        print('Reguler going to Gym and proper exercise')

alamin = Cricketer('Al Amin', 25, '6f', 64, 'BD')
alamin.eat()
alamin.excersise()

niloy = Cricketer('Niloy', 23, '5.4f', 70, 'Bd')

print(alamin+niloy)
print(alamin > niloy)
        