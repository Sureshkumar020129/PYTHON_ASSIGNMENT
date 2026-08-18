print("23.	Create a list of numbers and create separate lists for even and odd numbers.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)

print( even_numbers)
print(odd_numbers)