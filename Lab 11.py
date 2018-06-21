# CS141 - Summer 2018
# Lab 11 - more classes

# The following code contains a class Fraction
# for storing fractional numbers. It currently
# only has constructor and string methods.

# Add the following methods to this class:
# 1. getNum  - returns numerator
# 2. getDen  - returns denominator
# 3. __add__ - returns the sum of two Fractions. Note: by 
#              naming this function __add__, we are 
#              overriding the "+" sign.
# 4. __mul__ - returns the product of two Fractions. Note: by 
#              naming this function __mul__, we are 
#              overriding the "*" sign.
# 5. __neg__ - returns -1 times a Fraction. Note, by naming 
#              this function __neg__, we are overriding the 
#              unary "-" sign.
# 6. __sub__ - returns the difference of two Fractions. Note:
#              by naming this function __sub__, we are overriding
#              the "-" sign.
# 7. __eq__  - returns True if two Fractions are equal, False
#              otherwise. Note: by naming this function __eq__,
#              we are overriding the "==" operator.

# You do not need to include any input or output in your code,
# although I do recommend writing some tests to ensure your 
# methods are functioning as intended. Just make sure to comment
# out the test code submitting the final assignment.

def gcd(a,b):
  '''Euclidean algorithm to return the greatest
     common divisor of integers a and b'''
  while b:
    a, b = b, a % b
  return a

class Fraction():
  '''A class for storing fractions in canonical form:
     - gcd(numerator, denominator) = 1
     - positive denominator
  '''
  def __init__(self, num, den):
    g = gcd(abs(num), abs(den))
    self.num = num // g
    self.den = den // g
    if self.den < 0:
      self.num *= -1
      self.den *= -1

  def __str__(self):
    return "({:d}/{:d})".format(self.num, self.den)