# Defining constants
PI = 3.14159
GRAVITY = 9.81 # earth's gravity in m/s²

# calculate the area of a circle
def area_of_circle(radius):
    return PI * radius**2

# calculate the time of free fall
def time_of_free_fall(height):
    return (2 * height / GRAVITY)**0.5

# Usage
radius = 5
print("area of circle:", area_of_circle(radius))

height = 20
print("time of free fall:", time_of_free_fall(height))
