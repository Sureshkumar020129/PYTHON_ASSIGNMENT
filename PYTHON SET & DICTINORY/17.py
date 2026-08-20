print("16.	Create a set of numbers and print only the even numbers.")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {n for n in numbers if n % 2 == 0}
print("Even numbers:", even_numbers)