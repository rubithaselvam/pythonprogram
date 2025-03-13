list = ["ramya","udhaya","rubitha"]
counter = 1
for name in list:
    print( str(counter) + " -- " + name)
    counter = counter + 1


list = (1, 3, 6, 10, 21.8, "kavi")
for item in list:
    print(type(item))
    print(str(item))
    print(id(item))
