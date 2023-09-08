# read only --> you can not set the value. value can not be change
# getter --> get the value of the poperty. Most of the time, you will get the value of a privet attribute
# setter --> you can set the value a privet value


class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    # gatter without any setter is readonly attribute
    @property
    def age(self):
        return self._age
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        if value < 0:
            return f'You can not add negative value'
        self.__money += value

    @age.setter
    def age(self,value):
        self._age += value




alamin = User('Al Amin', 23, 12000)
print(alamin.money)
print(alamin.age)
alamin.age = 34
alamin.money = 345
print(alamin.money)
        