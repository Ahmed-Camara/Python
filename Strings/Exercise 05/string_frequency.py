"""
(Occurrences of a specified string) Write a function that counts the occurrences of a
specified non-overlapping string s2 in another string s1 using the following header:
def count(s1, s2):
For example, count("system error, syntax error", "error") returns
2. Write a test program that prompts the user to enter two strings and displays the
number of occurrences of the second string in the first string.
"""


def count(s1, s2):

    s1_split = s1.split(",") if "," in s1 else s1.split(" ")
    count = 0
    for s in s1_split:

        if s2 in s:
            count += 1
    return count


if __name__ == '__main__':

    str1 = input("Enter string 1 : ").lower()
    str2 = input("Enter string 2 : ").lower()

    str1 = str1.strip()
    str2 = str2.strip()

    count = count(str1, str2)

    print(count)
