from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Lion(Animal):
    def make_sound(self):
        print("ROAR!")
        
lion = Lion()
lion.make_sound()