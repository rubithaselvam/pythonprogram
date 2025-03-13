tuple = (10, 32, 4, 78,67)
print("tuple:", tuple)

# creating a mixed tuple
mixed_tuple = (5, "rubi", 265.54, "false")
print("mixed_tuple:", mixed_tuple)
print(type(mixed_tuple))

# creating a single element
single_element = ("dhiya",) # the comma(,) is important
print("single_element:", single_element)

numbers = (22, 65, 5289, 5578, 55) # creating a new set for find a index & slicing

# index of the element
print("first element:",numbers[0])
print("last element:", numbers[-1])

# slicing a numbers using index value
print("first 3 numbers:", numbers[:3])
print("last 2 numbers:", numbers[-2:])
print("centre number:", numbers[2:3])

# creating a 2 set for combining into 1 set
tuple1 = (1, 5, 68, 527, 65)
tuple2 = (65, 57, 574, 78, 447)
combine = tuple1 + tuple2
print("combine:", combine)

# repeating a tuple
repeat = tuple2
print("repeat:", tuple2*2)

value = (56, 65, 98, 54, 56, 58,556,56)

# finding a index and count of value
print("index of value:", value.index(556))
print("count of value:", value.count(56))

# unpacking tuples
person = ("rubitha", 21, "makeup artist")
name, age, profession = person
print("name:", name, "age:", age, "profession:", profession)


nested_tuple = (1, (2, 3, 4), (5, 6))
print("Nested Tuple:", nested_tuple)
print("Access Nested Element:", nested_tuple[1][2])  # 4

# list muttable
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list[6] = 19
print("update list:", list)

# tuple immutable
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#tuple[6] = 19
print("update tuple:", tuple) # it cannot be updated because it is immutable

