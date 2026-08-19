print("45.	Create a list of student tuples and search for a student by name.")
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("Diana", 92)]
student_name = "Charlie"
found = False
for name, grade in students:
    if name == student_name:
        print(f"Student found: {name}, Grade: {grade}")
        found = True
        break
if not found:
    print("Student not found.")