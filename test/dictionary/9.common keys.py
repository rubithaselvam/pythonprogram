x = {"a" :"ruby",
     "x" :"mani",
     "d" :"anu"}
y = {"x" :"yash",
     "b" :"ruby",
     "d" :"manya"}

z = set(x.keys()) & set(y.keys())
print("common keys:", z)
