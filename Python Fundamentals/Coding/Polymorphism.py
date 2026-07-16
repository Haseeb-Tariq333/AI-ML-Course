class Employee:
    def get_designation(self):
        print("Designation = ?")

class Teacher(Employee):
    def get_designation(self):  ## Function Overriding
        print("Designation = Teacher")
        
t1 = Teacher()
t1.get_designation()