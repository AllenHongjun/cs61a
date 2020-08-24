# Tree recursion

def fib(n):
    """Compute the nth Fibonacci number.

    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


#Knapsack

def knap(n, k):
    if n == 0:
        return k == 0
    with_last = knap(n // 10, k - n % 10)
    without_last = knap(n // 10, k)
    return with_last or without_last


#Count Partitions

def count_partitions(n, m):
    """Count the partitions of n using parts up to size m.

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

def knap(n, k):
    if n == 0:
        return k == 0
    with_last = knap(n // 10, k - n % 10)
    without_last = knap(n // 10, k)
    return with_last or without_last


#Binary Print

def all_nums(k):
    def h(k, prefix):
        if k == 0:
            print(prefix)
            return
        h(k - 1, prefix * 10)
        h(k - 1, prefix * 10 + 1)
    h(k, 0)

