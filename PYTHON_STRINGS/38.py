print("38.	Write a program to count the number of digits in a string.")
string = input("Enter a string: ")
count = 0
for char in string:
    if char.isdigit():
        count += 1
print("Number of digits in the string:", count)