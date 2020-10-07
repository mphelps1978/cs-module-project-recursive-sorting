# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    pass
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # first, set some defaults. We have 2 arrays, so we need to track their indexes,
    # starting from the first element. We also need to track a general index for our new
    # array
    indexA = 0
    indexB = 0
    i = 0

    while indexA < len(arrA) and indexB < len(arrB):  # while we're in the bounds of both arrays
        if arrA[indexA] < arrB[indexB]:  # if a is smaller than b
            merged_arr[i] = arrA[indexA]  # add a into the new array
            indexA += 1  # move to the next item in a
        else:
            merged_arr[i] = arrB[indexB]  # otherwise b is smaller, so we put it into the new array
            indexB += 1  # move to the next item in b

        i += 1  # get ready to insert a new item into the new array

    # now, let's say that for some reason, a and b are different lengths, or we have some leftovers after we
    # merge the arrays We need to account for that as well. they should already be sorted, so we should be ok

    while indexA < len(arrA):  # we'll start with A, and just toss them in the new array, incrementing the indexes as we go
        merged_arr[i] = arrA[indexA]
        indexA += 1
        i += 1

    while indexB < len(arrB):  # Now let's check B and do the same
        merged_arr[i] = arrB[indexB]
        indexB += 1
        i += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # our edge case for an empty array, or an array wiith 1 (it's already sorted, duh)
    # but not only that, this is our base case to get single length arrays to sort out
    if len(arr) <= 1:
        return arr

    # Now we're going to get the middle of the array
    middle = len(arr) // 2  # once again using floor to round down

    # now we're going to split the array into sub-list until the lengths are one lengths are 1
    # and assign them left/right values (splitting them into halves)

    left = merge_sort(arr[:middle])  # split it to the middle
    right = merge_sort(arr[middle:])  # split it after the middle

    return merge(left, right)  # and lastly, using the sorting method in merge, we put it all back together

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here
