print("1.	Create a class called Student and create one object of the class.")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Alice", 20)
print(f"Student Name: {student1.name}, Age: {student1.age}")