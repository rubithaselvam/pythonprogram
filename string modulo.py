# String modulo operator(%)

print("geeks : %2d, portal : %5.2f" %  (1, 05.333))

print("Total students : %3d, boys : %3d" % (240, 120))  # Print integer value

print("%15.3o" % (12))  # Print octal value

print("%10.3E" % (356.08977))   # Print exponental value




# Positional formation with format() method

# Using indexed placeholders for string formation
print("I Love {0} for \"{1}!\"".format("mahil", "Techlab"))

# {0} is replaced by the first argument 'Geeks'
print("{0} and portal".format("Geeks"))

# Formating with placeholders, {0} replaced by 'Geeks'
print("portal and {0}".format("Geeks"))




cstr = "Electrity Bill"

# Printing the center aligned string with fillchr
print("Center aligned: ")
print(cstr.center(40,'='))

# Printing the left aligned string with "-" padding
print("left aligned: ")
print(cstr.ljust(40, '-'))

# Printing the right aligned string with "-" padding
print("right aligned: ")
print(cstr.rjust(40, '-'))