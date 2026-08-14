print("36.	Write a program to count the number of vowels in a string.")
user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in user_string:
    if char in vowels:
        count += 1
print(f"The number of vowels in the string is: {count}")