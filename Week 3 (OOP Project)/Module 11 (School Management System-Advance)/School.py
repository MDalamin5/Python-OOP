class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        # composition
        self.classrooms = {}
        
    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        className = student.classroom.name
        if className in self.classrooms:
            # TODO: set student id (rool number) at the time of adding the student
            self.classrooms[className].add_student(student)
        else:
            print(f"No classroom as named {className}")


    @staticmethod
    def calculate_grade(marks):
        if 80<= marks <= 100:
            return 'A+'
        elif 70 <= marks <= 80:
            return 'A'
        elif 60 <= marks <= 70:
            return 'A-'
        elif 50 <= marks <= 60:
            return 'B'
        elif 40 <= marks <= 50:
            return 'C'
        elif 33 <= marks <= 40:
            return 'D'
        else:
            return 'F'
    

    @staticmethod
    def grade_to_value(grade):
        grade_map = {'A+' : 5.00,
                     'A' : 4.00,
                     'A-': 3.50,
                     'B' : 3.00,
                     'C' : 2.00,
                     'D' : 1.00,
                     'F' : 0.00
                     }
        return grade_map[grade]
    

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <=5.00:
            return 'A+'
        elif 3.5 <= value <= 4.5:
            return 'A'
        elif 3.0 <= value <= 3.5:
            return 'A-'
        elif 2.5 <= value <= 3.0:
            return 'B'
        elif 2.0 <= value <= 2.5:
            return 'C'
        elif 1.0 <= value <= 2.0:
            return 'D'
        else:
            return 'F'

    def __repr__(self) -> str:
        print('=============All Classrooms============')
        for key, value in self.classrooms.items():
            print(key)

        print('------------Student Info------------')
        eight = self.classrooms['eight']
        print('Total student in Class Eight: ', len(eight.students))

        for student in eight.students:
            print('Name: ',student.name)

        print('****************SUBJECT INFO*****************')
        for subject in eight.subjects:
            print(f'Subject Name: {subject.name} :: Teacher Name: {subject.teacher.name}')
            print('-'*55)

        print('-----------------STUDENT EXAM MARKS--------------')
        print()
        for student in eight.students:
            
            for key, value in student.marks.items():
                print(f'Student name: {student.name} : {key} ---> {value} ---> {student.subject_grade[key]}')
            print('='*45)


        return ''



# ****************
class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        # composition
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students)+1}'
        student.id = serial_id
        # student.classroom = self.name
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    #TODO: sort students by grade
    def get_top_student(self):
        pass



# ****************
class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_mark = 30

        
    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark) 
