order = {'a': 87, 'b': 575, 'c': 487, 'd': 776}

print("Ascending Order:", dict(sorted(order.items(), key=lambda x: x[1])))
print("Descending Order:", dict(sorted(order.items(), key=lambda x: x[1], reverse=True)))
