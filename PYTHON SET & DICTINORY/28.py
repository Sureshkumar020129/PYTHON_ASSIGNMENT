print("28.	Create a dictionary and add a new key-value pair.")
student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}
student["email"] = "alice@example.com"
print("Updated dictionary:")
for key, value in student.items():
    print(key + ":", value)