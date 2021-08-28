string1 = str("Welcome to string learning in python")
print(string1)

string2 = str("Welcome to string learning in python")
print(string2)

print("string 1 id is : {},\nstring 2 id is : {}".format(id(string1), id(string2)))

# functions for strings

st = "Welcome"
print(st)
print(len(st))
print(max(st))
print(min(st))
print('Last character : ', st[len(st) - 1])
print('Last character : ', st[-2])
# slicing
print(st[1:4])
print(st[:6])
print(st[4:])
print(st[1:-1])

# concatenation,repetition

s1 = "Welcome"
s2 = "Python"

s3 = s1 + ' ' + s2
print(s3)

s4 = 3 * s1
print(s4)

s5 = s1 * 3
print(s5)


# in and not in operator

s1 = "Welcome"
print("come" not in s1)

"""
s = input("Enter a string: ")

if "python" in s or "Python" in s:
    print("Python is in ", s)
else:
    print("Python is not in ", s)

"""
for ch in string2:
    print(ch, end='')
print()
print(string2.endswith("on"))

st = "Welcome to python"
print(st.isalpha())


# SEARCHING FOR SUBSTRINGS


s = "Welcome to python come"
print("Ends with 'thon' : ", s.endswith("thon"))
print("Ends with 'good' : ", s.startswith("good"))
print("find 'come' : ", s.find("come"))
print("rfind 'come' : ", s.rfind("come"))
print("count '0' : ", s.count("o"))


# CONVERTING STRING

s = str(s)
s = s[0:(len(s)-4)]

print('Capitalize() : ', s.capitalize())
print('Title() : ', s.title())
print('Lower() : ', s.lower())
print('Upper() : ', s.upper())
print('Swapcase() : ', s.swapcase())
print('Replace() : ', s.replace("python", "c++"))

s = "Welcome"
s = s.replace("come", "COME")
print(s)


s = "Welcome"

print(s.center(11))
print(s.ljust(11))
print(s.rjust(11))
