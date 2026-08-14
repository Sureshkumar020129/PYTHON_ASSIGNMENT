print('44.	Write a program to remove all spaces from a string without using replace().')
string = input("Enter a string: ")
new_string = ""
for char in string:
    if char != " ":
        new_string += char
print("String without spaces:", new_string)