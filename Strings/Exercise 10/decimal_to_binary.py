
def decimalToBinary(decimal):

    binary = ""

    while decimal != 0:
        bit = decimal % 2
        binary = binary + str(bit)
        decimal = decimal // 2

    return binary


if __name__ == "__main__":

    decimal = int(input("Enter a decimal number: "))
    num = decimalToBinary(decimal)
    print("{}".format(num))
