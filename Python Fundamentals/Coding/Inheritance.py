class Employee:
    start_time = "10 am"
    end_time = "8pm"

class Teacher(Employee):
    def __init__(self, name):
        self.name = name
        
teacher_1 = Teacher("Haseeb")    
print(teacher_1.name, teacher_1.start_time, teacher_1.end_time)


## Multi level Inheritance