 # Example
name = "Alice"  # A string variable
age = 25         # A integer variable
is_student = True # A boolean variable

print(type(name))
print(id(name))

#Vaild variable names
user_name = ("kavi")
_score = 100
age2 = 30

# Invalid variable names
#2name = "Alice"    # Starts with a number
#user-name = "Bob"  # Contains a hyphen
#class = "Math"     # uses a reserved keyboard


x = 10  # x is an integer
x = "Hello"     # Now x is a string
x = 3.14    # Now X is a float


a = b = c = 5
print(a, b, c)  # Output: 5 5 5


x, y, z = 1, 2, 3
print(x, y, z)  #Output: 1 2 3


# Examples
integer_var = 10    # Integer
float_var = 3.14    # Float
string_var = "Python"   # String
list_var = [1, 2, 3]    # List
dict_var = {"a": 1, "b": 2}     # Dictionary -----> keys are always in double quotes


# Checking Variable Types

x = "42"
print(type(x))  # Output: <class 'int'>



x = 10
print(x)    # Output: 10
del x
# print(x)  # This will raise a NameError



# Best practices for variables

count = 5   # Clear
c = 5   # Unclear



user_name = "Alice"     # Preferred
UserName = "Alice"  # Not recommened (used for classes)


# Complex Data Type

# Examples
z1 = 3 + 4j     # Complex number with real=3, imaginery=4
z2 = 5 - 2j     # Complex number with real=5, imaginery=2


z = 3 + 4j
print(z.real)   # Output: 3.0 (real part)
print(z.imag)   # OUTPUT: 4.0 (imaginary part)

z1 = 2 + 3j
z2 = 1 - 1j

print(z1 + z2)  # Output: (3+2j)
print(z1 - z2)  # Output: (1+4j)
print(z1 * z2)  # Output: (5+1j)
print(z1 / z2)  # Output: (0.5+2.5j)


# Casting variables


s = "10"    # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)   # Cast integer to string

# Display results
print(n)
print(cnt)
print(s2)


x = [1, 2, 3]   # x refers to a list object in memory
y = x   # y is now same reference to the same object


# Object reference

x = [1, 2, 3]
y = x

print(id(x))    # Example: 140273645891520
print(id(y))    # Same as x: 140273645891520

# Immutable

a = 10
b = a
a = 20  # Create a new object for a
print(a)    # Output: 20
print(b)    # Output; 10 (b still points to the original object)


# is vs ==

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)    # True (values are equal)
print(x is y)   # False (different objects )


# Garbage Collection

x = [1, 2, 3]
y = None    # The list is no longer referenced, and memory is freed


a = "I am global"

def f():
    global a
    a = "Modified globally"
    print(a)

f()
print(a)



# Assigning value to variable
x = 10
print(x)

# Removing the variable using del
del(x)


