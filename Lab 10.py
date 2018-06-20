# CS141 - Summer 2018
# Lab 10 - classes

# This file contains two class definitions
# 1. A Point class, which is complete and correct, and 
# 2. A LineSegment class, whose methods you must fill in

import math

class Point():
	def __init__(self, x, y):
		'''initialize a point with coordinates (x, y)'''
		self.x = x
		self.y = y
		
	def get_x(self):
		'''return the x-coordinate'''
		return self.x
	
	def get_y(self):
		'''return the y-coordinate'''
		return self.y

	def is_origin(self):
		'''return True if this point is the origin, False otherwise'''
		if self.x == 0 and self.y == 0:
			return True
		else:
			return False

	def magnitude(self):
		'''returns the magnitude of the point, AKA its distance from 
		   the origin'''
		return math.sqrt(self.x**2 + self.y**2)
	

	def __str__(self):
		'''gives the string representation of a Point object. This method
		   is called behind the scenes when a Point is given to a print
		   command'''
		return "(" + str(self.x) + ", " + str(self.y) + ")"




class LineSegment():
	def __init__(self, point_a, point_b):
		'''initialize a line segment spanning the space between two Point
		   objects, point_a and point_b'''
		self.point_a = point_a
		self.point_b = point_b
		

	def is_degenerate(self):
		'''returns True if point_a and point_b are the same point in space, 
		   False otherwise'''
		pass
	
	def is_vertical(self):
		'''returns True if the line segment is vertical, False if it is 
		   either degenerate or not vertical'''
		pass
	
	def is_horizontal(self):
		'''returns True if the line segment is horizontal, False if it is 
		   either degenerate or not horizontal'''
		pass
	
	def slope(self):
		'''returns the slope of the line segment, or returns False if the 
		   line segment is vertical or degenerate'''
		pass
	
	def length(self):
		'''returns the length of the line segment. Note that even a degenerate
		   line segment has a length, it is just a length of 0.'''
		return 1 # This return 1 is a placeholder like "pass", but it needs
		         # to return a number to give to the format function
	



point_a = Point(1, 2)
point_b = Point(3, -4)
point_c = Point(1, 2)
point_d = Point(3, 4)
line_a = LineSegment(point_a, point_b)
line_b = LineSegment(point_a, point_c)
line_c = LineSegment(point_b, point_d)

# These commands all execute correctly already
print (point_a)
print (point_b)
print (point_a.get_y())
print (point_a.is_origin())
print (point_b.magnitude())

# These commands will only return correct results once you've filled
# out the methods for the LineSegment class.
# The expected output of each line is commented out to the right.
print (line_a.is_degenerate())           # False
print (line_b.is_degenerate())           # True
print (line_a.is_horizontal())           # False
print (line_c.is_vertical())             # True
print (line_c.slope())                   # False
print (line_a.slope())                   # -3.0
print ("{:.6f}".format(line_a.length())) # 6.324555