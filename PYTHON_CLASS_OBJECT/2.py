print("2.	Create a class called Car and create three objects with different values.")

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)
print(f"Car 1: {car1.year} {car1.brand} {car1.model}")
print(f"Car 2: {car2.year} {car2.brand} {car2.model}")
print(f"Car 3: {car3.year} {car3.brand} {car3.model}")