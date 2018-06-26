# CS141 - Summer 2018
# Lab 12 - the command line

# Up until now, our Python programs have interacted with
# the world around them by prompting the user for input.
# This technique assumes that there is a human there to provide
# the input in the first place. But, there is another method
# of interacting with other programs that makes our code much
# easier to integrate into our computers' execution environments.
# That method is through command line arguments.


# Consider the following command line argument
#
# cd assignments
#
# You know that this opens the folder named assignments, 
# or returns an error if no such folder exists.
# "cd" is a function, and "assignments" is an argument,
# so you can think of this as the command line version of
# Python's cd("assignments"). Command line functions are
# flexible in the number of arguments that they accept.
# For instance, try running the following lines
#
# ls
# ls -l
# ls -l -a
#
#
# Each has slightly different output, and you see that ls
# is willing to accept a variety of amounts of inputs.


# When you run a Pyton script from the command line with 
#
# python3 Lab12.py
#
# the function python3 calls a program which interprets
# Python files and points it at your code Lab12.py
# We can give further arguments to this program, which
# in turn are accessible to your code, e.g.
#
# python3 Lab12.py 1 "abc" data.txt 2.4
#
# Inside your code, the list sys.argv contains the 
# command line arguments called alongside your script.


# The following code computes the length of a hypotenuse 
# of a right triangle with given leg lengths. Notice how
# it handles command line arguments

import sys
import math

if len(sys.argv) != 3:
	print ("Incorrect number of inputs. Expected two numbers.")
	quit()

try:
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	hypotenuse = math.sqrt(a**2 + b**2)
except:
	print ("Incorrect type of inputs. Expected two positive numbers.")
else:
	print ("Hypotenuse is {:.2f}".format(hypotenuse))
	
# You can run this program with the command
# 
# python3 Lab12example.py 3 4
#
# to test it. Two things to note:
# 1. sys.argv[0] is always the name of the program being run.
# 2. all values in sys.argv are strings by default.