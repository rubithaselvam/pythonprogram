def first_non_repeating_char(s):# s refers to the string
    for c in s:# c refers to the character
        if s.count(c) == 1:
            return c
    return None

r = "kaviarasan"
print("First non-repeating character:", first_non_repeating_char(r))
