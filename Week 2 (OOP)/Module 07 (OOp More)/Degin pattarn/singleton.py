# singleton --> one single onstance
# if you want a new instance, you will get the old one (alrady created ) instace


class Singleton:
    __intance = None
    def __init__(self) -> None:
        if Singleton.__intance is None:
            Singleton.__intance = self
        else:
            raise Exception('This is Singleton. Already have an instance, use that one by calling get instance method')

    def get_instance():
        if Singleton.__intance is None:
            Singleton()
        return Singleton.__intance
    

first  = Singleton.get_instance()
secend = Singleton.get_instance()
third = Singleton.get_instance()
print(first)
print(secend)
print(third)
# last = Singleton()