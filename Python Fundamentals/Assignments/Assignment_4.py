          ##################
          ### Question:1 ###
          ##################

class BankAccount:
    def __init__(self, acc_num, owner_name, balance):
        self.owner_name = owner_name
        self.acc_num = acc_num
        self.balance = balance
        
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"New balance is {self.balance}") 
        
    def withdraw(self, withdraw_amount):
        if self.balance > withdraw_amount:
            self.balance -= withdraw_amount
        else:
            print("Insufficnet balance") 
            
    def check_balance(self,):
        print(f"Your current balance is {self.balance}")
        
a1 = BankAccount(1234, "Haseeb", 5000)
a1.deposit(2000)
a1.withdraw(1000)
a1.check_balance()



          ##################
          ### Question:2 ###
          ##################
          
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []
    
    def add_review(self):
        new_review = input("Add a new review: ")
        self.reviews.append(new_review)
        print(f"New list of reviews is {self.reviews}")
        
    def count_reviews(self):
        print(f"The number of reviews are {len(self.reviews)}")
        
    def display_reviews(self):
        print(f"All reviews are {self.reviews}")
        
        
Book1 = Book("The Town of Dead", "Haseeb Gilbert")
Book1.add_review()
Book1.count_reviews()
Book1.display_reviews()


          ##################
          ### Question:3 ###
          ##################
          

class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
        
    def get_name(self):
        return self.__name
    def set_name(self, name):
        if not name or name.strip() == "":
            print("No name found")
        self.__name = name
    
    def get_roll_no(self):
        return self.__roll_no
    def set_roll_no(self, roll_no):
        if roll_no < 0 and roll_no > 100:
            print("Enter a roll no betweeen 1 and 100")
        else:
            self.__roll_no = roll_no
            
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        if marks < 0:
            print("Marks cannot be negative")
        else:
            self.__marks = marks
    
stu1 = Student("Haseeb",12,34)
print(stu1.get_marks())
stu1.set_marks(67)
print(stu1.get_name())
stu1.set_name("Habiib")
print(stu1.get_roll_no())
stu1.set_roll_no(99)



          ##################
          ### Question:4 ###
          ##################
          
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width       
    def area(self):
        return self.length*self.width
    
sq1 = Square(5)
print(sq1.area())



          ##################
          ### Question:5 ###
          ##################
          
class Vehicle:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price

class Car(Vehicle):
    def __init__(self,brand, model, price, no_of_seats, car_type):
        super().__init__(model,brand,price)
        self.no_of_seats = no_of_seats
        self.car_type = car_type

class Bike(Vehicle):
    def __init__(self,brand, model, price, engine_cc):
        super().__init__(brand, model, price)
        self.engine_cc = engine_cc
    
    
    
          ##################
          ### Question:6 ###
          ##################
          

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name  = name
    
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend
        
    def calculate_salary(self):
        return self.stipend 

class FullTimeEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary 
        self.bonus = bonus
        
    def calculate_salary(self):
        return self.salary+self.bonus
    
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate 
        self.hours_worked = hours_worked
        
    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked 
    
Intern1 = Intern("Haseeb",25000000000)
print(Intern1.calculate_salary())


      
      
          ##################
          ### Question:8 ###
          ##################

class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name 
        self.level = level
        Player.player_count += 1
        
    def display_num_of_players(self):
        print(f"total number of plaeyers are {Player.player_count}")
        
          
          
             
          ##################
          ### Question:9 ###
          ##################
          


class Herbivore:
    def __init__(self):
        self.has_flat_teeth = True
        
    def eat_plants(self):
        return "eating berries and plants..."
class Carnivore:
    def __init__(self):
        self.has_claws = True
    def hunt(self):
        return "Going to hunt and eat and meat"
class Omnivore:
    def eat_anything(self):
        return "Can eat both plants and meat"
    
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        Carnivore.__init__(self)
        Herbivore.__init__(self)
        self.name = name
        
yogi = Bear("Yogi")
print(yogi.eat_plants())   
print(yogi.has_claws)
print(yogi.eat_anything())
    
    
    