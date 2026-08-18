print("20.	Create a list of numbers and find the smallest number without using min().")
numbers = [1, 2, 3, 4, 5]
smallest = numbers[0]
for n in numbers:
    if n < smallest:
        smallest = n
print(smallest)