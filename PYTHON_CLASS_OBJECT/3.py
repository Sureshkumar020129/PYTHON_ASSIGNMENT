print("3.	Create a class called Employee and create an object to represent an employee.")

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
employee1 = Employee("John", 30, 50000)
print(f"Employee Name: {employee1.name}, Age: {employee1.age}, Salary: {employee1.salary}")