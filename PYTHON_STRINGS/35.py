print("35.	Ask the user to enter an email address and check whether it contains '@' and '.' to validate it.")
email = input("Enter an email address: ")
if "@" in email and "." in email:
    print("The email address is valid.")
else:
    print("The email address is invalid.")