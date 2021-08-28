
def hexCharToDecimal(ch):
    if 'A' <= ch <= 'F':
        return 10 + ord(ch) - ord('A')
    else:
        return ord(ch) - ord('0')


def hexToDecimal(hex):
    decimalValue = 0
    for i in range(len(hex)):
        ch = hex[i]
        if 'A' <= ch <= 'F' or '0' <= ch <= '9':
            decimalValue = decimalValue * 16 + hexCharToDecimal(ch)
        else:
            return None

    return decimalValue


if __name__ == "__main__":
    hex = input("Enter a hex number : ")
    decimal = hexToDecimal(hex.upper())

    if decimal == None:
        print("Incorrect hex number.")
    else:
        print("The decimal value for hex number {} is {}".format(hex, decimal))
