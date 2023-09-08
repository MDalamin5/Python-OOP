# inharitace is a relationship
# composition has a relationship

class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        print('Engine Start....')
    

class Driver:
    def __init__(self) -> None:
        pass



class Car:
    def __init__(self) -> None:
        self.engine = Engine()


    def start(self):
        self.engine.start()


tata = Car()
tata.start()