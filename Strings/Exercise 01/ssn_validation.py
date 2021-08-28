"""
(Check SSN) Write a program that prompts the user to enter a Social Security
number in the format ddd-dd-dddd, where d is a digit. The program displays
Valid SSN for a correct Social Security number or Invalid SSN otherwise.

"""


def validate_SSN(ssn):

    validator = False
    if "-" in ssn:

        ssn_split = ssn.split("-")
        if (len(ssn_split[0]) == 3 and ssn_split[0].isdigit()) and (len(ssn_split[1]) == 2 and ssn_split[1].isdigit()) and (len(ssn_split[2]) == 4 and ssn_split[2].isdigit()):
            validator = True

    return validator


if __name__ == '__main__':

    ssn = input("Enter SSN number : ")

    if validate_SSN(ssn):
        print("{} is a valid ssn number ".format(ssn))
    else:
        print("{} is not a valid ssn number ".format(ssn))
