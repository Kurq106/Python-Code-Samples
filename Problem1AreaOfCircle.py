# Kimberly Urquiza
# Date
# Problem 1: Write a function areaOfCircle(r) which returns the area of a circle with radius r.

import math

def areaOfCircle(r):
    # Returns the area of a circle based on radius r
    return math.pi * (r ** 2)

# Test
r = 5
print("The area of a circle with radius", r, "is:", areaOfCircle(r))
