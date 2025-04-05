# find the longest word in sentence
def longest_word(s):
    words = s.split()
    return max(words, key=len)

sentence = "Find the longest word in this sentence"
print(longest_word(sentence))

# find the smallest word in sentence
def smallest_word(x):
    words = x.split()
    return min(words, key= len)
string = "what was that of a product ?"
print(smallest_word(string))

# remove the spaces in words
def remove_spaces(s):
    return s.replace(" ", "")

string = "Hello World"
print(remove_spaces(string))
