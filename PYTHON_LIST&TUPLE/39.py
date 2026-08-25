print("39.	Create a nested list containing student names and three subject marks. Calculate the total and average marks of every student.")
students = [
    ["Alice", 85, 90, 78],
    ["Bob", 70, 80, 65],
    ["Charlie", 90, 85, 88],
    ["David", 65, 70, 60],
    ["Eve", 80, 85, 75]
]

for student in students:
    name = student[0]
    marks = student[1:4]
    total = sum(marks)
    average = total / len(marks)
    print(f"{name}: Total = {total}, Average = {average:.2f}")