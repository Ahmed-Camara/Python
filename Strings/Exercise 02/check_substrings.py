"""
(Check substrings) You can check whether a string is a substring of another string
by using the find method in the str class. Write your own function to implement
find. Write a program that prompts the user to enter two strings and then checks
whether the first string is a substring of the second string.

"""


def find(str1, str2):

    if str1 in str2:
        return True

    return False


if __name__ == '__main__':

    str1 = input("Enter first string : ")
    str2 = input("Enter second string : ")

    if find(str1, str2):
        print("{} is a substring of {} ".format(str1, str2))
    else:
        print("{} is not a substring of {} ".format(str1, str2))
