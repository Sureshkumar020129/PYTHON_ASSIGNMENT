print("46.	Write a program to check whether a string is a palindrome.")
s = "dad"
cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
is_palindrome = cleaned_s == cleaned_s[::-1]
print(f"'{s}' is a palindrome: {is_palindrome}")