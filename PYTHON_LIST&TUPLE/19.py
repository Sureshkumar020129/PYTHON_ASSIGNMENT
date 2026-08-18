print("19.	Create a list of numbers and find the largest number without using max().")
numbers = [1, 2, 3, 4, 5]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print(largest)