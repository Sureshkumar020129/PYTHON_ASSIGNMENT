print("37.	Write a program to count the number of consonants in a string.")
user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in user_string:
    if char.isalpha() and char not in vowels:
        count += 1
print(f"The number of consonants in the string is: {count}")