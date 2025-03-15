x = {"a": 89, "b": 90, "c": 20, "d": 30}
threshold = 30
for k,v in x.items():
    if v > threshold:
        print("the above threshold values:",v)
