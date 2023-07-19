import random


class Person:
    def __init__(self, name) -> None:
        self.name = name
        

# ********************
class Teacher(Person):
    def __init__(self, name) -> None:
        
        super().__init__(name)

    def teach(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name} '

    def evaluate_exam(self):
        
        marks = random.randint(0,100)
        return marks
     #  TODO set marks for the subject for each Student


# ********************
class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None


    def calculate_final_grade(self):
        pass


    @property
    def id(self):
        return id
    
    @id.setter
    def id(self, value):
        self.__id = value