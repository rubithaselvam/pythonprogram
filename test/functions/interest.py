def interest(p,r,t):
    return(p * r * t) / 100
def amount(p,r,t):
    return p + ((p * r * t) / 100)
print(interest(10000,12,1))
print(amount(10000,12,1))
