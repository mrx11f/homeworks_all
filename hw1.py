# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married
    
#     def introduce_myself(self):
#         print(f"My name is {self.fullname}. I'm {self.age} years old. I'm {'married' if self.is_married else 'not married'}.")
        

# class Student(Person):
#     def __init__(self, fullname, age, is_married, marks):
#         super().__init__(fullname, age, is_married)
#         self.marks = marks
    
#     def average_grade(self):
#         total = sum(self.marks.values())
#         count = len(self.marks)
#         return total / count

# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience, salary):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary

#     def introduce(self):
#         print(f"Hello, my name is {self.fullname} and {self.is_married}")
#         print(f"I am {self.age} years old and have {self.experience} years of experience.")
    
#     def calculate_salary(self):
#         bonus_years = max(self.experience - 3, 0)
#         bonus_percent = bonus_years * 0.05
#         salary = self.salary + (self.salary * bonus_percent)
#         return salary


# teacher = Teacher("Maria", 35, "I`m not married", 6, 50000)

# teacher.introduce()
# print(f"My salary is {teacher.calculate_salary()} dollars per year.")

# def create_students():
#     students = []
#     students.append({'name': 'John', 'math': 90, 'english': 85, 'history': 95})
#     students.append({'name': 'Mary', 'math': 80, 'english': 90, 'history': 92})
#     students.append({'name': 'Peter', 'math': 95, 'english': 87, 'history': 89})
#     return students

# students = create_students()

# for student in students:
#     print(f"Student name: {student['name']}")
#     print(f"Math grade: {student['math']}")
#     print(f"English grade: {student['english']}")
#     print(f"History grade: {student['history']}")
#     avg_grade = (student['math'] + student['english'] + student['history']) / 3
#     print(f"Average grade: {avg_grade:.2f}")
#     print()