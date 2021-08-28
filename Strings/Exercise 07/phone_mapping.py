"""
(Phone keypads) The international standard letter/number mapping for telephones is:
Write a function that returns a number, given an uppercase letter, as follows:
def getNumber(uppercaseLetter):
Write a test program that prompts the user to enter a phone number as a string. The
input number may contain letters. The program translates a letter (uppercase or
lowercase) to a digit and leaves all other characters intact.
"""


def getNumber(ch):

    val = 0

    if ch >= 'W':
        val = 9
    elif ch >= 'T':
        val = 8
    elif ch >= 'P':
        val = 7
    elif ch >= 'M':
        val = 6
    elif ch >= 'J':
        val = 5
    elif ch >= 'G':
        val = 4
    elif ch >= 'D':
        val = 3
    else:
        val = 2
    return val


def processNumber(phone):

    for s in phone:
        if s.isalpha():
            ch = s
            s = s.upper()
            phone = phone.replace(ch, str(getNumber(s)))
    return phone


if __name__ == '__main__':

    phone = input("Enter phone number : ")

    print(processNumber(phone.strip()))
