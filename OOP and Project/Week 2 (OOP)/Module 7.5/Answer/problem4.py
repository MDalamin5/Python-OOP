# gatter and setter method

class NSU:
    def __init__(self,name, id, dep) -> None:
        self.__name = name
        self.__id = id
        self.__dep = dep

    @property
    def name(self):
        return self.__name
    
    
    @name.setter
    def name(self, value):
        self.__name = value
    



    def display(self):
        print(f'Name: {self.__name}, ID: {self.__id}, Department: {self.__dep}')



Alamin = NSU('Al Amin', 1811904, 'ECE')
# Alamin.display()
print(Alamin.name)
Alamin.name = 'Md Al Amin'
print(Alamin.name)
