print("45.	Write a program to reverse a string without using slicing or reversed().")
s = "Hello, World!"
reversed_s = ""
for char in s:
    reversed_s = char + reversed_s
print(reversed_s)