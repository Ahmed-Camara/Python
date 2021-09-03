"""
(Binary to decimal) Write a function that parses a binary number as a string into a
decimal integer. Use the function header:
def binaryToDecimal(binaryString):
For example, binary string 10001 is 17 
So, binaryToDecimal("10001") returns 17.
Write a test program that prompts the user to enter a binary string and displays the
corresponding decimal integer value.
"""

import math


def binaryToDecimal(binaryString):
    length = len(binaryString) - 1
    num = 0

    for ch in binaryString:
        b = int(ch) * math.pow(2, length)
        num = num + b
        length -= 1
    return int(num)


if __name__ == "__main__":

    binary_number = input("Enter a binary string: ")
    num = binaryToDecimal(binary_number)
    print("{}".format(num))
