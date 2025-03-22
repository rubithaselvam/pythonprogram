# Arithemetic operators
m = 10
n = 31

print("Addition of m and n:", m + n)
print("Subtraction of m and n:", m - n)
print("Multiplication of m and n:", m * n)
print("Division of m and n:", m / n)
print("Exponentiation of m and n:", m ** n)
print("modulo of m and n:", m % n)
print("Floor division of m and n:", m // n)     # floor division always takes a whole number

# Relational operators or comparison
s = 89
t = 45

print("less than of s and t:", s < t)
print("greater than of s and t:", s > t)
print("less than or equal to s and t:", s <= t)
print("greater than or equal to s and t:", s >= t)
print("equal to s and t:", s == t)
print("not equal to s and t:", s != t)

# assignment operator ---> when the operations are done the value of the variable is changed
                            # the changed value is done follow the operations
k = 27
k += 3

print("After += :", k)
k -= 8
print("After -= :", k)
k *= 3
print("After *= :", k)
k /= 2
print("After /= :", k)
k %= 5
print("After %= :", k)

# Logical operators ---> true or false are do not given in the string eg: "true"
r = False
u = True

print("logical and:", r and u)
print("logical or:", r or u)
print("logical not:", not u)

# identity operator
a = [101, 111, 121]
b = a # the two variables refers the same the value
c = [101, 111, 121] # the values are same but variables are different

print("a is b:", a is b)
print("a is not b:", a is not b)
print("a is equal to c:", a == c)

# membership operators
objects = ["ShuttleBat", "Crock", "Net"]

print("Is 'ShuttleBat' in the list:", "ShuttleBat" in  objects)
print("Is 'Crock' in the list:", "Crock" not in objects)

# bitwise operator
h = 81 # 1010001
t = 67 # 1000011

""" # Binary convert formula
binary_representation = bin(67)
print(binary_representation)"""

print("bitwise of or:", h | t)
print("bitwise of xor:", h ^ t)
print("bitwise of and:", h & t)
print("bitwise of left shift:", h << t)
print("bitwise of right shift:", h >> t)
print("bitwise of one's complement:", ~ t)

