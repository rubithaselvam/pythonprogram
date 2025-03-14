def count(s,c):
    c1 = 0
    for i in s:
        if i == c:
            c1 += 1
    return c1
string =input("Enter a string:")
ch =input("Enter a character to be searched:")
cnt = count(string, ch)
print("the given character {} occurs {} times in the given string".format(ch,cnt))

