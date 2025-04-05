# add a integer
add_lambda = lambda x, y : x + y
print(add_lambda(7,5)) # here we can not give like this = print("jgf"(add_lambda(3,4)))

# sub a integer
sub_lambda = lambda f,g : f - g
print(sub_lambda(9,6))

#multiple of integer
multi_lambda = lambda r,e : r * e
print(multi_lambda(45,6))

# division of integer
division_lambda = lambda y,u : y / u
print(division_lambda(87,7)) # we can not give the .2f method to convert the float to whole num

# mapping a lambda for square
x = [3,5,8,9,7]
numbers = list(map(lambda y : y ** 2,x)) # here after the lambda y : y need same variable
print(numbers)

# modouls
integers = [78,53,26,75]
modouls = list(filter(lambda i : i % 3,integers)) # here which number is modouls by 3 is output
print(modouls)

# even number
even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even(7))

# odd number
odd = lambda f : "odd" if f % 5 == 0 else "even"
print(odd(8))







