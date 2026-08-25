print("38.	Create a list of tuples containing employee name, designation, and salary. Find the employee with the highest salary.")
employees = [
    ("Alice", "Manager", 50000),
    ("Bob", "Developer", 45000),
    ("Charlie", "Analyst", 40000),
    ("David", "Designer", 42000),
    ("Eve", "Tester", 38000)
]

highest_paid_employee = max(employees, key=lambda x: x[2])
print(f"The employee with the highest salary is {highest_paid_employee[0]} with a salary of ${highest_paid_employee[2]}.")