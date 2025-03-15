x = {"a": "ruby",
     "m": "ramya",
     "n": "udhaya"
     }
y = {"a": "pavi",
     "b": "jaya",
     "c": "shree"
     }
# the set operators (difference(-)) formula is used here
key = x.keys() - y.keys()
keys = y.keys() - x.keys()

print("remaining keys in x:", key)
print("remaining keys in y:", keys)
