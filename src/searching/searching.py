import math

# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):

    # Your code here
    if len(arr) <= 0:  # edge case for empty array
        return -1

    # get the middle of the dataset
    middle = math.floor((start + end) / 2)  # using the floor operator to round down

    if arr[middle] == target:  # first, if the middle IS the target, we're done - This is also our Base Case
        return middle

    elif arr[middle] < target:  # target is less than the middle
        # recursive call, moving the start point to 1 after the middle
        return binary_search(arr, target, middle + 1, end)

    elif arr[middle] > target:  # target is greater than the middle
        # recursive call, moving the end point to 1 before the middle
        return binary_search(arr, target, start, middle - 1)

    return -1  # Can't find it


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# # or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here
