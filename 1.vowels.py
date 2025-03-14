string1="The person you called is Anu"
string2="aAeEiIoOuU"
vowles = 0 # v using as vowles
for i in string1:
    if i in string2:
        vowles += 1
print("the string contains {} vowles".format(vowles))



