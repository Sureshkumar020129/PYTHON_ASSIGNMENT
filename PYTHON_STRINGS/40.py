print("40.	Write a program to count uppercase and lowercase characters separately.")
string = input("Enter a string: ")
upper_count = 0
lower_count = 0
for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Number of uppercase characters:", upper_count)
print("Number of lowercase characters:", lower_count)