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
