# if statement
x = 44 # check the condition is true or not
if x + 44:
    print("it is yes")

# if else statement
number = [12,88,34,40]
for number in number:

    if number % 4 == 0:
        print("the even number",number)
    else:
        print("the odd number",number)

# if elif else statement
j = 12
if j == 12:
    print("you are my age people")
elif j > 23:
    print("you are elder than me")
else:
    print("you are younger tha me")

# for statement
for i in range(8): # if counting is 8 but the number executed for 7
    print("hii girl",i)
print("---------another type----------")
m = ("kavi", "harini", "gomathi")
for names in m:
    print(names)

#while statement with continue and break
w = 54
while w < 90:
    w += 1 # because of this condition it added of 54 + 1 = 55

    if w == 70:
        continue

    if w == 85:
        break
    print("numbers:",w)

print("==" * 20)

# nested loop
for i in range(1,10):
    for k in range(1,5):
        print(i * k, end = "") # end kudukula na each numbers are printed in new line, if end is give see the output
    print() # this print seperate the set of work, if not given this print the o/p is 12342468......2736
