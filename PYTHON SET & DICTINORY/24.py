print("24.	Create two sets representing students enrolled in Python and Java. Find students enrolled in both courses.")
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Charlie", "David", "Eve", "Frank"}
both_courses = python_students & java_students
print("Students enrolled in both courses:", both_courses)