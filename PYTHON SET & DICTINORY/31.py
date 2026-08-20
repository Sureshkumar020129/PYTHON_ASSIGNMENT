print("31.	Create a dictionary and remove the last inserted item using popitem().")
student = {
    "name": "Alice",
    "age": 20,
    "course": "Computer Science",
    "marks": 85
}
last_item = student.popitem()
print("Removed item:", last_item)
print("Updated dictionary:")
for key, value in student.items():
    print(key + ":", value)