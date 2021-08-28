"""
(Count the letters in a string) Write a function that counts the number of letters in
a string using the following header:
def countLetters(s):

"""


def countLetters(s):

    count = 0

    for c in s:
        if c.isalpha():
            count += 1
    return count


if __name__ == '__main__':

    strs = input("Enter a string : ").lower()

    count = countLetters(strs)

    print("The string : '{}' contains {} letters.".format(strs, count))
