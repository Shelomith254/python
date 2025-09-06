class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum(self.grades.values())
        return total_grades /len(self.grades)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"
student = Student("Alice", 15)
student.add_grade("Math", 80)
student.add_grade("English", 90)
student.add_grade("Science", 85)

print(student)
print(f"Average grade: {student.get_average_grade()}")

