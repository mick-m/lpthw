#1. accept user input range of type int and print incrementally

def count_my_nos(i, inc):
    """ Takes user-defined number range and outputs result. """
    while i < inc:
        print i
        i = i + 1

# Take user input
print "The program will count for you."
print "input your starting number:"
strt_no = int(raw_input(""))

print "input your ending number:"
fin_no = int(raw_input(""))

# Adds one so that final no is displayed
fin_no = fin_no + 1

# Skip a line
print "\n"

# Method call
count_my_nos(strt_no, fin_no)


# 2. Create a list. Accept user input range of type int and add to list.
#    Then print the list.

list = []
def count_again (start, end):
    """ Accepts user-defined number range and adds to a list."""
    for i in range (start, end):
        # tells you it's adding your no as loop iterates
        print "adding %d to the list" % i
        
        # Appends each number to list
        list.append(i)

# Output instructions to user
print "\nLet's create a new list:"
print "Please enter the first number in your list: > "
strt = int(raw_input())
print "Plesase enter the last number in your list: > "
fin = int(raw_input())

# Add one so the final no is displayed
fin = fin + 1

# Method call
print "\nPrinting your new list...\n"
count_again(strt, fin)

print "\n",list
