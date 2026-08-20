print("30.	Create a dictionary and remove a key-value pair using pop().")
student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}
email = student.pop("email", None)
print("Removed email:", email)
print("Updated dictionary:")
for key, value in student.items():
    print(key + ":", value)