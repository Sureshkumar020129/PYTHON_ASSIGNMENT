print("42.	Write a program to print only the vowels from a string.")
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        print(char)