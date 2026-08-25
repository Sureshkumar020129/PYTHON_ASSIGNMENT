print("34.	Create a dictionary and print all key-value pairs using items().")
student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}
print("Key-value pairs in the dictionary:")
for key, value in student.items():
    print(key + ":", value)