my_set = {"rubi", "udhaya", "ramya", "sree"} # me the mistake is ("ruby, udhaya, ramya, sree")
print("set:", my_set) # set is key word dont give in coding name eg: set = ("....")its worng; myset = ("...")its correct

empty_set = set()
print("empty_set = ", empty_set)

# adding a name in a set
my_set.add("pavi")
print("after adding pavi:", my_set)

# removing a name in a set
my_set.remove("ramya")
print("after removeing ramya:", my_set)

# dicard a set
my_set.discard("jaya")
print("after dicarding jaya:", my_set)

# updating a set
my_set.update(["mahil","tech"])
print("after update a set:", my_set)

# remove a random element
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("set after pop:", my_set)


# clearing a entire set
my_set.clear()
print("after clearing a set:", my_set)


print("+++++++++++++++++++++++++++++++++++++")
set1 = {3,4,1,2,}
set2 = {1,2,5,}

print("union:", set1 | set2)
print("intersection:", set1 & set2)
print("difference:", set1 - set2)
print("symmetric:", set1 ^ set2)











