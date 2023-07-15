class Book:
    def __init__(self,name) -> None:
        self.name = name

    def read(self):
        # pass
        raise NotImplemented

class Physics(Book):
    def __init__(self, name, lab) -> None:
        self.lab = lab
        super().__init__(name)

    def read(self):
        return f'I read the book every day'


topon = Physics('Topon Sir', True)
print(topon.read())
print(issubclass(Physics, Book))
print(isinstance(topon, Physics))
print(isinstance(topon, Book))

        