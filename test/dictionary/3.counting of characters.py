def count_characters(s): # s refers to the string
    count = {}
    for c in s: # c is refers to the character
        count[c] = count.get(c, 0) + 1
    return count

# Example usage
s = input("Enter a string: ")
result = count_characters(s)
print("Character count:", result)