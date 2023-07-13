class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self) -> str:
        return f'Student name: {self.name} class: {self.current_class} ID: {self.id}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, Subject: {self.subject}, ID: {self.id}'


class School:
    def __init__(self, name):
        self.name = name
        self.teacher = []
        self.student = []

    def add_teacher(self, name, subject):
        id = len(self.teacher)+1001
        teacher = Teacher(name,subject,id)
        self.teacher.append(teacher)

    def enroll(self, name, fee):
        if fee<6500:
            return 'Not enough fee'
        else:
            id = len(self.student)+1
            student = Student(name,'UG',id)
            self.student.append(student)
            return f'{name} is enrolled with id : {id}, extra money {fee-6500}'
    
    def __repr__(self) -> str:
        print('Welcome to ',self.name)
        print('===========Our Teachers==========')
        for teacher in self.teacher:
            print(teacher)
        print('===========Our Student==========')
        for student in self.student:
            print(student)
        return 'All Done for Now'
# alamin = Student('Md Al Amin', 'UG-3rd Year',1811904)
# print(alamin)

# Kaysar = Teacher('Kaysar', 'CSE', 18112344)
# print(Kaysar)

phitron = School('Phitron')
phitron.enroll('Md Al Amin',5000)
phitron.enroll('Kaysar', 7000)
phitron.enroll('Shihab', 8000)
phitron.enroll('Jahid', 4000)

phitron.add_teacher('Md Shahin','Accountig')
phitron.add_teacher('Murad Ahmed','Bangla')
phitron.add_teacher('AZk', 'ML')

print(phitron)