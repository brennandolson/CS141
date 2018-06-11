# The following program outputs a simple times tables.
# The output is automatically sent to terminal via 
# the print command.

# Modify the code so that it instead outputs to a file 
# named output.txt via the write command.




print("X |", end='')

for i in range(1, 10):
  print (str(i).rjust(3), end="")

print('\n'+'-'*31)


for i in range(1, 10):
  print (str(i)+" |", end="")
  for j in range(1, 10):
    print (str(i * j).rjust(3), end="")
  print ()