# Print the sum of integers less than 100 which are divisible by two.

# x counts the numbers (from 2-100)
x = 0

# y stores output
y = 0

print "The following number is the sum of all even numbers between 2 and 100: "

# End number (101) is not inclusive
for x in range (0, 101):
    if x % 2 == 0:
        
        # y stores each number that is divisble by 2;
        # adds the new value for x to it on each iteration
        y = y + x

# Adding the comma after x ensures the numbers are printed on same line
print y,
