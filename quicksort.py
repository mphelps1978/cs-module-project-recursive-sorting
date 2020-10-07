# quicksort a list of numbers (a):
#   ...
#   ...
#   quicksort() <-- recursively


# Get the first number in place
# Quicksort the rest


# partition = chose a number to be a "pivot"


# let's chose the first one in the list [5]
# split the list into 2 lists:
# left one with numbers less than pivot [3 2 1]
# right one with greater or equal to pivot [9 7 8 6]

# smaller numbers left of the pivot [3 2 1] [5]
# greater numbers right of the pivot [3 2 1] [5] [9 7 8 6]

# quicksort left
# quicksort right

"""
quicksort(a):
    ...
    ...
    quicksort(...)
​
[5 9 3 7 2 8 1 6]
​
[3 2 1] [5] [9 7 8 6]    Things sorted after this pass: 1
         ^
[2 1] [3] [5] [7 8 6] [9] Things sorted after this pass: 3
       ^   ^           ^
​
[1 2 3 4 5 6]
​
[1] [2 3 4 5 6]
​
[1] [2] [3 4 5 6]
​
[1] [2] [3] [4 5 6]
​
​
[5 3 2 4 1 8 7 6 9]
​
[3 2 4 1] [5] [8 7 6 9]
[2 1] [3] [4] [5] [7 6] [8] [9]
​
quicksort(a)
    if len(a) <= 1:
        return a
​
    Partitioning in quicksort:
​
    choose a number to be the _pivot_
       let's just choose the first number
​
    split the list into two lists:
        left one with the numbers less than the pivot
        right one with numbers greater than (or equal to) the pivot
​
    put the smaller numbers left of the pivot
    greater numbers right of the pivot
​
    return quicksort(left) + [pivot] + quicksort(right)
"""


# Out  of Place (returns a new array, not very space efficient)
def partition(a):
    left = []
    pivot = a[0]
    right = []

    for v in a[1:]:
        if v < pivot:
            left.append(v)
        else:
            right.append(v)


def quicksort(a):
    if len(a) <= 1:
        return a

    left, pivot, right = partition(a)

    return quicksort(left) + [pivot] + quicksort(right)


# in place quicksort

# moving things around in the passed-in array

#      p
# a = [5, 9, 3, 7, 2, 8, 1, 6]
#      i
#      ^                       ^
#     low                     high


def quicksort(a):

    def quicksort_recursive(a, low, high):
        if low >= high:
            return
        p = low  # pivot index

        # partition step
        for i in range(low, high):
            if a[i] < a[p]:
                # swap element i with item to right of pivot
                a[p + 1], a[i] = a[i], a[p + 1]

                # swap pivot with element on its right
                a[p + 1], a[p] = a[p], a[p + 1]

            # at this point the pivot is in it's final spot, and the left and right partitions need to be sorted

            quicksort_recursive(a, low, p)
            quicksort_recursive(a, p + 1, high)

    quicksort_recursive(a, 0, len(a))


a = [5, 9, 3, 7, 2, 8, 1, 6]

quicksort(a)
print(a)
