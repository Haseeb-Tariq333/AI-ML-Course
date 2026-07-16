class Teacher:
    def __init__(self, salary):
        self.salary = salary
        
class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta_1 = TA(20_000, 3.9, "Haseeb")
print(ta_1.name , ta_1.gpa, ta_1.salary)
        