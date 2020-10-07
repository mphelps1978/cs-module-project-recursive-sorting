# Fibonacci Sequence
# Each number is the sum of the previous 2 numbers

# 0 1 2 3 4 5 6 7  8  9  10 <-- Index
# 0 1 1 2 3 5 8 13 21 34 55 <-- Value

# fib(6):
#   fib(5)+fib(4)

# fib(0): 0
# fib(1): 1
# fib(n): fib(n - 1) + fib(n - 2)

def fib(n):
    if n == 0:
        return 0  # these two statements can be considered base, since
    if n == 1:
        return 1  # 0 and 1 are given values in a fibonacci sequence
    return fib(n - 1) + fib(n - 2)

# Above solution is O(2^n)

# Bonus - Using Caching to improve performance of the above solution:


cache = {}


def fib(n):
    # Base:
    if n == 0:
        return
    if n == 1:
        return

    if n not in cache:
        # because of the way this is calculated, we can put all the values into a cache and save it for later when we need it
        cache[n] = fib(n - 1) + fib(n - 2)

    return cache[n]
