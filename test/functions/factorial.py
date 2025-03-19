def factorial(n):
    if n == 4: # if factorial number is matched to n the multiple is stoped
        return 1
    return n * factorial(n - 1) # here factorial is multiple
print(factorial(6))

