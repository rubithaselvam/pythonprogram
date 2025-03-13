# Integer and Float

num1 = int(input("Enter an integer: "))     # Taking integer input
num2 = float(input("Enter a float: "))      # Taking float input

print(f"Integer: {num1}, float:{num2}")
print(f"sum: {num1 + num2}, Multiplication: {num1 * num2}")

# String
text = input ("Enter a string: ")
print(f"uppercase: {text.upper()}, length: {len(text)}")

# list
num_list = [10, 20, 30, 40, 50]
print(f"Original list: {num_list}")
num_list.append(60)     # adding an element
print(f"updated list; {num_list}")

# tuple
num_tuple = (1, 2, 3, 4, 5)
print(f"tuple: {num_tuple}, second element: {num_tuple[1]}")

# set (removes duplicates)
num_set = {1, 2, 3, 4, 5}
print(f"set (no duplicates): {num_set}")
num_set.add(6)
print(f"updated set: {num_set}")

# dictionary (key-value paris)
student = {"name": "mani", "age": 45, "course": "python"}
print(f"student dictionary: {student}")
print(f"student namel: {student['name']}")

# boolean
is_adult = num1 >= 18   # boolean condition
print(f"is adult? {is_adult}")