"""
(Occurrences of a specified character) Write a function that finds the number of
occurrences of a specified character in a string using the following header:
def count(s, ch):
The str class has the count method. Implement your method without using the
count method. For example, count("Welcome", 'e') returns 2. Write a test
program that prompts the user to enter a string followed by a character and displays the number of occurrences of the character in the string.
"""


def counts(s, str):

    count = 0

    for c in str:
        if s == c:
            count += 1
    return count


if __name__ == '__main__':

    strs = input("Enter a string string : ")
    char = input("Enter a character : ")

    if (strs.isupper() or strs.capitalize()) or (char.isupper()):
        strs = strs.lower()
        strs = strs.strip()
        char = char.strip()
        char = char.lower()

    count = counts(char, strs)

    print("{} occurs {} times in {}.".format(char, count, strs))
