# Print
-2
print(-2)
'Go Bears'
print('Go Bears')
print(1, 2, 3)
None
print(None)
x = -2
x
x = print(-2)
x
print(print(1), print(2))

# Addition/Multiplication
2 + 3 * 4 + 5
(2 + 3) * (4 + 5)

# Division
618 / 10
618 // 10
618 % 10
from operator import truediv, floordiv, mod
floordiv(618, 10)
truediv(618, 10)
mod(618, 10)

# Approximation
5 / 3
5 // 3
5 % 3

# Multiple return values
def divide_exact(n, d):
    return n // d, n % d
quotient, remainder = divide_exact(618, 10)

# Dostrings, doctests, & default arguments
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(618, 10)
    >>> quotient
    61
    >>> remainder
    8
    """
    return floordiv(n, d), mod(n, d)

# Conditional expressions
def absolute_value(x):
    """Return the absolute value of X.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

# Summation via while
i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i
total

# Return

def end(n, d):
    """Print the final digits of N in reverse order until D is found.

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

def search(f):
    """Return the smallest non-negative integer x for which f(x) is a true value."""
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def is_three(x):
    """Return whether x is three.

    >>> search(is_three)
    3
    """
    return x == 3

def square(x):
    return x * x

def positive(x):
    """A function that is 0 until square(x)-100 is positive.

    >>> search(positive)
    11
    """
    return max(0, square(x) - 100)

def invert(f):
    """Return a function g(y) that returns x such that f(x) == y.

    >>> sqrt = invert(square)
    >>> sqrt(16)
    4
    """
    return lambda y: search(lambda x: f(x) == y)

# Control

def if_(c, t, f):
    if c:
        t
    else:
        f

from math import sqrt

def real_sqrt(x):
    """Return the real part of the square root of x.

    >>> real_sqrt(4)
    2.0
    >>> real_sqrt(-4)
    0.0
    """
    if x > 0:
        return sqrt(x)
    else:
        return 0.0
    # if_(x > 0, sqrt(x), 0.0)

# Control Expressions

def has_big_sqrt(x):
    """Return whether x has a big square root.

    >>> has_big_sqrt(1000)
    True
    >>> has_big_sqrt(100)
    False
    >>> has_big_sqrt(0)
    False
    >>> has_big_sqrt(-1000)
    False
    """
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    """Is N small enough that 1/N can be represented?

    >>> reasonable(100)
    True
    >>> reasonable(0)
    True
    >>> reasonable(-100)
    True
    >>> reasonable(10 ** 1000)
    False
    """
    return n == 0 or 1/n != 0.0
