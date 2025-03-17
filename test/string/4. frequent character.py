from collections import Counter

def most_frequent_char(s):
    count = Counter(s)
    return max(count, key=count.get)

s = "I am sathiyavathi"
print("the frequent letter is:", most_frequent_char(s))
