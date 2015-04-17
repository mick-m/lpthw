# importing argv from the sys module (aka as libraries)
from sys import argv

# unpacking argv
# argv = "argument variable" - holds arguments you pass to script when you run
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "your third variable is:", third

# to run this you must pass 3 x arguments
# e.g. python ex13.py first 2nd 3rd
