class Family:
    def __init__(self,address) -> None:
        self.address = address

    def __repr__(self) -> str:
        return f'Address: {self.address}'


class School:
    def __init__(self,id, lavel) -> None:
        self.id = id
        self.lavel = lavel

class Sports:
    def __init__(self,game_name) -> None:
        self.game_name = game_name


class Student (Family, School, Sports):
    def __init__(self, address, id, lavel, game_name) -> None:
        School.__init__(self, id, lavel)
        Sports.__init__(self, game_name)
        Family.__init__(self, address)

    def __repr__(self) -> str:
        print(f'ID: {self.id}, Lavel: {self.lavel}, Fevo. Game: {self.game_name}')
        return super().__repr__()



Alamin = Student('Bashundhara RA', 18111904, 'UG-3rd Year', 'Cricket')
print(Alamin)
        