# CS141 - Summer 2018
# Lab 8 - lists

# Problem 2 - sieve of Eratosthenes

# The sieve of eratosthenes is a fast way of producing all prime numbers
# up to some number.

# One implementation goes as follows:

# Given a number N, we wish to produce all primes less than or equal to N

# 1. create a list all_nums of 0's of length N + 1
# 2. create an empty list prime_nums in which to store primes as we encounter them
# 3. iterate i from 2 to N
# 4. if all_nums[i] is 0, then we know i is prime
# 4a. add i to prime_nums
# 4b. iterate j from i to N with an increment of i. Set all_nums[j] = 1
#     This has the effect of ruling out all multiples of i from being
#     counted as prime later.
# 5. return prime_nums



# Create a function sieve(N) which takes a number N >= 2 and returns
# the list of primes less than or equal to N


