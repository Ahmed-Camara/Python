def isPalindrome(string):

    low = 0
    high = len(string) - 1

    while low < high:

        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


if __name__ == "__main__":

    string = input("Enter a string : ")

    if isPalindrome(string):
        print("{} is a palindrome.".format(string))
    else:
        print("{} is not a palindrome.".format(string))
