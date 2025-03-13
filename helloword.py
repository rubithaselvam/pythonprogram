print("rubitha")

name = "Alice"  # A string variable

print(name)

print("--------------")


name = ("kavin, malathi", 5, 9, 35858.554, ("janu", 6, 244.753))
print(type(name))
print(id(name))
print(str(name))
for item in name:
    print(item)

print("--------------")


print("haritha")
name = "mani devi"
marks = 90
print(name)
print(marks)
print(id(90))

print("--------------")


# Explanation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
print("Sum:", sum_result)

print("--------------")


# Explanation
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
num3 = float(input("enter the third number: "))

largest = max(num1, num2, num3)
print("largest = ", largest)

print("-------------")



# Reverse codeing
a,b = 5, 6
a,b = b,a
print(a,b)