class Person:
    def __init__(self, name, age) -> None:  # double underscore is Dunder Method
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}---Age: {self.age}")
    
    def __del__(self):
        print('Person object Deleted successfully')
        


alamin = Person('Md Al Amin', 24)
alamin.display()
