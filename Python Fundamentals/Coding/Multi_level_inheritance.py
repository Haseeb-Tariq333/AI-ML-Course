class Employee:
    start_time = "10 am"
    end_time = "8 pm"
    
class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role
        
class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

a1 = Accountant(11_000, "CA")
print(a1.role, a1.salary, a1.start_time)
        