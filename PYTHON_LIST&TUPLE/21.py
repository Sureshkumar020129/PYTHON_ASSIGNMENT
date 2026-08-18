print("21.	Create a list of numbers and calculate the average.")
numbers = [1, 2, 3, 4, 5]
total = 0       
for n in numbers:
    total += n
average = total / len(numbers)
print(average)