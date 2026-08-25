print("35.	Create a dictionary of student marks and check whether a particular student exists.")
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 95
}
student_name = input("Enter the name of the student to check: ")
if student_name in student_marks:
    print(student_name,"exists in the dictionary with marks:")
else:
    print("student not found in the dictionary.")