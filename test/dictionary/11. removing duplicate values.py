people = {"name" : "kavitha",
          "age" : 30,
          "year" : 30,
          "place" : "chennai",
          "hobby" : "playing games"}
print(people)
h = {}
for key, value in people.items():
    if value not in h.values():
        h[key] = value

print(h)
