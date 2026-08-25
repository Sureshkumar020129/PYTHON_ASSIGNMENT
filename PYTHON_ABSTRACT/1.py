from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass;
class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"
class Cat(Animal):
    def sound(self):
        return "Meow! Meow!"
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    
    print(f"Dog says: {dog.sound()}")
    print(f"Cat says: {cat.sound()}")
    
