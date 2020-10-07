# Recursion -

# We take a value, perform some function on it, and then call the function again with a modification to the initial input

def foo(x, y):
    if x >= y:  # Base case - Our "Stopping point"
        return
    print(x)
    foo(x + 1, y)


foo(1, 3)  # Will  print 1, 2
foo(1, 8)  # Will  print 1, 2, 3, 4, 5, 6, 7


# Can we define this problem in the terms of identical sub problems?

# Goal: print the numbers from x to y - 1
# A if x >= y: return <-- Base case
# print x
# print numbers from x+1 to y-1

# def print_nums(x, y - 1):
#   if x >= y:
#     return

#   print(x)
#   print_nums(x+1, y-1)

# The recursive call has to drive the data to the base case in some way
