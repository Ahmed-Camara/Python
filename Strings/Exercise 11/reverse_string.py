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
