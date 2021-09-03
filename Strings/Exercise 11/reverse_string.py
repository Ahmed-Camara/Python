"""
(Reverse a string) Write a function that reverses a string. The header of the function is:
def reverse(s):
Write a test program that prompts the user to enter a string, invokes the reverse
function, and displays the reversed string
"""


def reverse(str):

    c = -1
    result = ""
    for s in range(len(str)):
        result = result + str[c]
        c -= 1
    return result


if __name__ == "__main__":

    s = input("Enter a string : ")
    print("The reversed version of the string '{}' is : '{}'".format(s, reverse(s)))
