class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_age(self):
        return self.age
    
stu1 = Student("Haseeb", "19")
stu2 = Student("Danyal", "19")
stu3 = Student("Ahmed", "19")

print(stu1.age)
print(stu2.name)
print(stu3.name, stu3.age)

print(stu1.get_age())

