# CS141 - Summer 2018
# Lab 9 - dictionaries


# A concordance is a list of words in a document,
# along with the lines in which those words appear.
# Write a program which:
#   1. Prompts the user for a filename, and 
#   2. Outputs a concordance for that file

# A sample text file "sample.txt" is provided for your testing.
# The expected output for this file would be

# a : 0 3
# as : 2
# document : 1 2
# intended : 2
# is : 0 2
# sample : 0 3
# the : 1
# this : 0

# Hints:
# 1. You can store the words of the document as keys to a dictionary,
#    and the lines on which they appear as the values of 
#    that dictionary (with all the line numbers in a single list).
# 1a. This means the first time you encounter a word, add it to the dictionary
#     and make its value a list with one item - the current line number.
# 1b. When you encounter a word already in the dictionary, you can add
#     the current line number to the list of line numbers associated to the
#     word.
#
# 2. Use 'for i, line in enumerate(file_object)' to iterate through a file.
#    'line' will store the contents of the current line and 'i' will store 
#    the current line number.
#
# 3. Use 'for word in line.split()' to iterate through the words in a line.
#
# 4. You can check if an object 'k' is already in a dictionary 'd' (as a key)
#    by checking 'if k in d'.
#
# 5. You can throw out periods, commas, etc. from a string by using '.replace()'