print("32.	Ask the user to enter a username and check whether it contains only alphabets and numbers.")
username = input("Enter a username: ")
if username.isalnum():
    print("The username contains only alphabets and numbers.")
else:
    print("The username contains other characters.")