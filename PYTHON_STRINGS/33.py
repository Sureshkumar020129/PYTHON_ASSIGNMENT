print
("33.	Ask the user to enter a password and check whether it contains at least one digit.")
password = input("Enter a password: ")
if any(char.isdigit() for char in password):
    print("The password contains at least one digit.")  