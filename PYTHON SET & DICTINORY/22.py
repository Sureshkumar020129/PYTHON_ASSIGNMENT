print("22.	Create a set of numbers and find the smallest number without using min().")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
smallest_number = None
for n in numbers:
    if smallest_number is None or n < smallest_number:
        smallest_number = n
print("Smallest number:", smallest_number)