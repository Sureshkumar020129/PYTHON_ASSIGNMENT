print("8.	Create a set of numbers and check whether a particular number exists.")
numbers = {1, 2, 3, 4, 5}
print(numbers)
number_to_check = 3
if number_to_check in numbers:
    print(f"{number_to_check} exists in the set.")
else:
    print(f"{number_to_check} does not exist in the set.")