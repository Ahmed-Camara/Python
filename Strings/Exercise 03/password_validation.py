"""
(Check password) Some Web sites impose certain rules for passwords. Write a
function that checks whether a string is a valid password. Suppose the password
rules are as follows:
■ A password must have at least eight characters.
■ A password must consist of only letters and digits.
■ A password must contain at least two digits.
Write a program that prompts the user to enter a password and displays valid
password if the rules are followed or invalid password otherwise.
"""


def validate_password(password):

    digits = 0
    chars = 0

    # iterate through the password string

    for ch in password:

        if ch.isalpha():
            chars += 1
        elif ch.isdigit():
            chars += 1
            digits += 1

    if chars >= 8:
        if digits >= 2:
            return True

    return False


if __name__ == '__main__':

    password = input("Enter a password : ")

    if validate_password(password):
        print("{} is a valide password".format(password))
    else:
        print("{} is not a valide password".format(password))
