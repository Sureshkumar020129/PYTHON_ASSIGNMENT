print("36.	Create a list containing 5 tuples, where each tuple contains a student's name and marks. Display all students who scored above 75.")
students = [
    ("Alice", 85),
    ("Bob", 70),
    ("Charlie", 90),
    ("David", 65),
    ("Eve", 80)
]

for name, marks in students:
    if marks > 75:
        print(f"{name}: {marks}")