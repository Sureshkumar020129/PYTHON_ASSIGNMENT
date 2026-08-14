print("43.	Write a program to print only the consonants from a string.")
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in string:
    if char.isalpha() and char not in vowels:
        print(char)