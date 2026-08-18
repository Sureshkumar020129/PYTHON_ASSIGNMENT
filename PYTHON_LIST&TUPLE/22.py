print("22.	Create a list of numbers and count how many numbers are greater than 50.")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
count = 0
for n in numbers:
    if n > 50:
        count += 1
print(count)