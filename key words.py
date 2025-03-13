import keyword

print("The list of keywords is : ")

print(keyword.kwlist)



# Value Keyword
print("---------------")

print("---- Value keyword ------------")
print(False == 0)
print(True == 2)

# True + True + True + True is  8
print(True + True + True + True)

# True + False + False + True is  4
print(True + False + False + True)

# None isn't equal to  0  or an empty list []
print(None == 0)
print(None == [])


# DELETE
print("---------------")

s = "GeeksForGeeks"
print(s)

del s
# Print(s)

# AND OR and NOT

print("---- LOGICAL Operator-----")
a = True
b = False

# Logical operators
print(a and b)  # AND: True if both a and b are true
print(a or b)   # OR: True if at least one of a or b is true
print(not a)    # NOT: Inverts the value of a


# in heyword

print("----- In keyword --------")

 # example 1
print(3 in [1,2,3])

# example 2
if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not a part of geeksforgeeks")


# is keyword

print("-------- is keyword ----------")

# example 1
print(2 is 2)
print(id(2) is id(2))

x = 2

print("------ x int reference ----------")
print(x is x)
print(id(x) is id(x))

print(id(2))
print(id(2))

print("-- is object reference ---")
# example 2
a = [1, 2, 3]
b =a
c = [1, 2, 3]

# True: a and b refer to the same object
print(a is b)

# False; a and c have a same value but are different objects
print(a is c)