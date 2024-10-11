# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"{self.name}, Age: {self.age}"

# Student class inheriting Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        total_points = sum(self.grades.values())
        return total_points / len(self.grades) if self.grades else 0

    def get_details(self):
        return f"Student: {self.name}, ID: {self.student_id}, Age: {self.age}, Average Grade: {self.get_average_grade()}"

# Teacher class inheriting Person
class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_details(self):
        subjects_taught = ', '.join(self.subjects)
        return f"Teacher: {self.name}, ID: {self.teacher_id}, Age: {self.age}, Subjects: {subjects_taught}"

# Classroom class
class Classroom:
    def __init__(self, class_name, teacher):
        self.class_name = class_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_class_details(self):
        students_details = "\n".join([student.get_details() for student in self.students])
        return f"Class: {self.class_name}\nTeacher: {self.teacher.get_details()}\nStudents:\n{students_details}"

# School class
class School:
    def __init__(self, name):
        self.name = name
        self.classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def get_school_details(self):
        class_details = "\n".join([classroom.get_class_details() for classroom in self.classrooms])
        return f"School: {self.name}\nClassrooms:\n{class_details}"

# Exam class to handle exams and grades
class Exam:
    def __init__(self, subject, total_marks):
        self.subject = subject
        self.total_marks = total_marks
        self.results = {}

    def add_result(self, student, marks_obtained):
        self.results[student] = marks_obtained

    def get_results(self):
        result_details = "\n".join([f"{student.name}: {marks}" for student, marks in self.results.items()])
        return f"Exam Results for {self.subject}:\n{result_details}"

# Sample usage of the system

# Create teacher
teacher_1 = Teacher("Mr. Smith", 40, "T123")
teacher_1.add_subject("Math")
teacher_1.add_subject("Physics")

# Create students
student_1 = Student("Alice", 15, "S101")
student_2 = Student("Bob", 16, "S102")
student_1.add_grade("Math", 90)
student_2.add_grade("Math", 85)

# Create classroom and add students
classroom_1 = Classroom("Class 10-A", teacher_1)
classroom_1.add_student(student_1)
classroom_1.add_student(student_2)

# Create school and add classrooms
school = School("Greenwood High School")
school.add_classroom(classroom_1)

# Display school details
print(school.get_school_details())

# Create an exam and add results
math_exam = Exam("Math", 100)
math_exam.add_result(student_1, 90)
math_exam.add_result(student_2, 85)

# Show exam results
print(math_exam.get_results())
