print("Welcome to the programming")
x = 5
y = 6
z = x + y
print(z)
print("The sum = ", z)
print("The sum of", x, "and", y, "is", z)


person = "Mani", 25, "Fashion designing", "ruby5243@gmail.com"
print(type(person))


person = ("ruby", 21, "Fashion designing", "ruby9768@gmail.com")

name, age, department, email = person  # Unpacking tuple into variables
print(f"Name: {name}, Age: {age}, Department: {department}, email: {email}")

print("++++++++++++++++++++++++++++++++++++++++++++++")
name = input ("enter the name: ")
for i in range(12) :
    print(str(i+1) + " " + name)
