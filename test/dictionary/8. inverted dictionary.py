x = {"m": 45, "u": 86}
y = {v:k for k,v in x.items()} # in x m = key, 45 = value
                               # v:k means the value changed as key
                               # the key changed as value and the output is inversed of x

print(y)
