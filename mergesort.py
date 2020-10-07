# Merge sort
# ----------
# Phase 1: calling down the recursion:

#           [5 9 3 7 2 8 1 6]
#      [5 9 3 7]         [2 8 1 6]
#     [5 9] [3 7]       [2 8] [1 6]
#   [5] [9] [3] [7]   [2] [8] [1] [6]

# Phase 2: merge! returning from recursion:

#   [5] [9] [3] [7]   [2] [8] [1] [6]
#     [5 9] [3 7]       [2 8] [1 6]
#      [3 5 7 9]         [1 2 6 8]
#             ^                   ^
#          [1 2 3 5 6 7 8 9]
