# finding a minimum value in python
m = [45,56,50]
x = min(m)
print("the minimum number in m:",x)

# finding greater value of 40 using loop method
k = [78,98,45,36,27]
value = 40
highvalue = []
for values in k:
    if values > value :
        highvalue.append(values)

print("the highest value of :",highvalue)

# how to get a reverse string
# in strings question is one type and here is another type
text = "hello"  # Given string
reversed_text = ""  # Empty string to store the reversed version
print(text)
for i in text:
    reversed_text = i + reversed_text  # Add each character at the beginning

print("the reverse of given string is ", reversed_text)

# checked the program
def my_function():
    return
print("Hello")

my_function()

# LCM and GCD
import math
a,b = map(int,input("enter a value: ").split())
gcd = math.gcd(a,b) # input number of both can be divided by same number 6,8 both number can divide by 2
lcm = (a * b) // gcd # it multiply the given number and the multiple number is divided by gcd number 48 divided by 2
print(f"GCD: {gcd}, LCM: {lcm}")


