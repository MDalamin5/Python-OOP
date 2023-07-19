import random


class Person:
    def __init__(self, name) -> None:
        self.name = name
        

# ********************
class Teacher(Person):
    def __init__(self, name, subject) -> None:
        self.subject = subject
        super().__init__(name)

    def teach(self):
        pass

    def take_exam(self, subject, students):
        for student in students:
            marks = random.randint(0,100)
            # TODO set marks for the subject for each Student


# ********************
class Student(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.classroom = None
        self.__id = None
        self.subject = []
        self.marks = {}
        self.grade = None

    @property
    def id(self):
        return id
    
    @id.setter
    def id(self, value):
        self.__id = value