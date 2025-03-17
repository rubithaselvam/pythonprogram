d = ("the python program is easy to learn and easy to write a coding of python coding")
x = d.split()

count = {}

for word in x:
    count[word] = count.get(word, 0) + 1

print("The number of words and their frequency:",count)
