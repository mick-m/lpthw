print "What height are you (in inches)?",

# Cast input as an int to avoid calculation errors, such as:
# e.g. TypeError: can't multiply sequence by non-int of type 'float'
# Unless done - it thinks input is a String.

inches = int(raw_input())
cm = inches * 2.54
print "%r inches = %r cm." % (inches, cm)

print "How much do you weight in pounds?",
pounds = int(raw_input())
kilos = pounds * 0.45359237
print "%r pounds = %r kilos." %  (pounds, kilos)
