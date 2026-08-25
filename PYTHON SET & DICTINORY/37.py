print("37.	Create a dictionary of student names and marks. Find the student with the highest marks without using max().")
student_marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "Diana": 95
}
highest_student = None
highest_marks = 0
for student, marks in student_marks.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_student = student
print(f"The student with the highest marks is {highest_student} with {highest_marks} marks.")