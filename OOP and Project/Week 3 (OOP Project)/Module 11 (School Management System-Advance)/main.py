from School import School, ClassRoom, Subject
from Persons import Student, Teacher



def main():
    school = School('North South School', 'Bashundhara')
    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add students
    abul = Student('Abul Khan', eight)
    school.student_admission(abul)

    babul = Student('Babul Khan', eight)
    school.student_admission(babul)

    Ubul = Student('Ubul Khan', eight)
    school.student_admission(Ubul)

    # subject
    physics_teacher = Teacher('Md Al Amin')
    physics = Subject('Physics', physics_teacher)
    eight.add_subject(physics)

    chemistry_teacher = Teacher('Kaysarul Anas')
    chemistry = Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)

    math_teacher = Teacher('Jahid hasan')
    math = Subject('math', math_teacher)
    eight.add_subject(math)

    biology_teacher = Teacher('Rofiqul Alam')
    biology = Subject('biology', biology_teacher)
    eight.add_subject(biology)

    
    # Taking exam 
    eight.take_semester_final()


    print(school)





if __name__ == '__main__':
    main()