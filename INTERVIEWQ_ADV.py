# Print the sum of integers less than 100 which are divisible by two.

def even_sum(start, end):
    
    # Brackets and quotes uses to split lines the exceed 80 characters 
    print ("The following number is the sum of all even numbers between %d "
            "and %d") % (start, end)
    y = 0
    
    # Added 1 to end, because last number in a range is not inclusive.
    # e.g. "between 1 and 100" only goes as far as 99.
    
    for x in range (start, end + 1):
        if x % 2 == 0:
            y = y + x
    print y

print ("\nThis program will compute the sum of all even integers between x "
        "and y:")
print "Please enter the starting point (x): "
strt = int(raw_input(""))

print "Please enter the end point (y): "
nd = int(raw_input(""))

even_sum(strt, nd)
