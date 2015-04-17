from sys import argv

script, filename = argv

print "We're going to ersae %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for 3 x lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# change to ex16 to allow writing to file with one write statement
writeLine = "%s\n%s\n%s\n" % (line1, line2, line3)

print "I'm going to write these to the file."

# one line of code vs. six in previous example
target.write(writeLine)

print "And finally, we close it."
target.close()

