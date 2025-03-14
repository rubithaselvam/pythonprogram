def remove_duplicates(r):
    return "".join(sorted(set(r), key = r.index))

r = "malayalam"
print(r)
m = remove_duplicates(r)
print(f"string without duplicates:{m}")
