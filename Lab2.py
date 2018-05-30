# CS141 - Summer 2018
# Lab 2
from math import sqrt, pi

# Examples:
# You can prompt a user for input with the "input" function
a_string = input("Input a value for a:")
b_string = input("Input a value for b:")

# Input comes in as strings, so numbers must be converted
#   to ints or floats as needed
a = float(a_string)
b = float(b_string)

print ("The sum of a and b is", sqrt(a + b) + pi)

# Question 1 (length of a line segment):
# Prompt the user for four values: x0, y0, x1, y1.
# Output the length of the line segment connecting points
#   (x0, y0) and (x1, y1). 
# Recall the formula for this is 
#   length = sqrt((y0 - y1)**2 + (x0 - x1)**2).




# Question 2 (slope of a line segment):
# Prompt the user for four values: x0, y0, x1, y1.
# Output the slope of the line segment connecting points
#   (x0, y0) and (x1, y1). 
# Recall the formula for this is 
#   slope = (y0 - y1) / (x0 - x1).




# Question 3 (cylinder statistics):
# Prompt the user for two vaues: height and radius
# Output the volume and surface area of a cylinder with 
#   this height and radius.
# Recall the formulas for these are
#   volume = pi * radius**2 * height
#   area   = 2 * pi * radius * height + 2 * pi * radius**2