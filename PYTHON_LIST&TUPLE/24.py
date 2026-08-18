print("24.	Create a list containing duplicate values and create a new list without duplicates. Do not use set()")
numbers = [1, 2, 3, 2, 4, 1, 5, 4]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)
print(unique_numbers)