print("21.	Create a set of numbers and find the largest number without using max().")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
largest_number = None
for n in numbers:
    if largest_number is None or n > largest_number:
        largest_number = n
print("Largest number:", largest_number)