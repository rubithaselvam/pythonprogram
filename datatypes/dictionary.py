# Creating a dictionary
student = {
    "name": "Alice",
    "age": 25,
    "course": "Python"
}
print("Student Dictionary:", student)

print("----------------------")


# Creating an empty dictionary
empty_dict = {}
print("Empty Dictionary:", empty_dict)

print("-----------------------")


# Using dict() constructor
person = dict(name="John", age=30, city="New York")
print("Person Dictionary:", person)

print("-----------------------")


# Accessing Dictionary Values

print("Name:", person["name"])  # Accessing value using key

print("------------------")


# Using get() method (avoids KeyError)
#print("Age:", student["age1"])
print("Age:", student.get("age1"))
print("Marks:", student.get("marks", "Not available"))# Default value if key doesn't exist

print("---------------------")


# Adding & Updating Key-Value Pairs


student["age"] = 26  # Updating value
student["marks"] = 90  # Adding new key-value pair
print("Updated Dictionary:", student)

print("---------------------")


# Removing Elements

del student["marks"]  # Remove a key
print("After deletion:", student)

marks = student.pop("age")  # Remove and return the value
print("Removed Age:", marks)

student.clear()  # Clears entire dictionary
print("Cleared Dictionary:", student)


# Dictionary Operations

student = {"name": "Alice", "age": 25, "course": "Python"}

# Keys, Values, and Items
print("Keys:", student.keys())       # Returns all keys
print("Values:", student.values())   # Returns all values
print("Items:", student.items())     # Returns all key-value pairs

# Checking if a key exists
print("Is 'age' in dictionary?", "age" in student)  # True
print("Is 'marks' in dictionary?", "marks" in student)  # False


# Looping Through a Dictionary

for key, value in student.items():
    print(f"{key}: {value}")


# Nested Dictionary

students = {
    "Alice": {"age": 25, "course": "Python"},
    "Bob": {"age": 22, "course": "Java"}
}

print("Alice's Course:", students["Alice"]["course"])



# Dictionary Comprehension

squares = {x: x**2 for x in range(1, 6)}
print("Squares Dictionary:", squares)


# Comparing Sizes of Multiple Dictionaries

import sys

dicts = {
    "Small Dict": {"a": 1, "b": 2},
    "Medium Dict": {i: i*2 for i in range(50)},
    "Large Dict": {i: i**2 for i in range(1000)}
}


print(f"Large Dic value : " + str(dicts["Large Dict"]))

for name, d in dicts.items():
    print(f"{name} Size: {sys.getsizeof(d)} bytes")

print("=" * 35)
print("++++++++++++++++++++++++++++++++++++++++++++++++")

