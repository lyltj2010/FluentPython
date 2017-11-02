"""
Typically
A decorator replaces the decorated function with a new
function that accepts the same arguments and(usually) returns
whatever the decorated function was supposed to return, while
also doing some extra processing.
"""

import time

def clock(func):
    # func encompassed as free variable
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print("[%0.8fs] %s(%s) -> %r" % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock # callable
def snooze(seconds):
    time.sleep(seconds)

# The same as factorial = clock(factorial)
# factorial hold a reference to `clocked` function
@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

if __name__ == "__main__":
    print("*" * 40, "Calling snooze(.123)")
    snooze(.123)
    print("*" * 40, "Calling factorial(6")
    print("6! =", factorial(6))

# Output something like this
# **************************************** Calling snooze(.123)
# [0.12818915s] snooze(0.123) -> None
# **************************************** Calling factorial(6
# [0.00000215s] factorial(1) -> 1
# [0.00004745s] factorial(2) -> 2
# [0.00007767s] factorial(3) -> 6
# [0.00010755s] factorial(4) -> 24
# [0.00013669s] factorial(5) -> 120
# [0.00017143s] factorial(6) -> 720
# 6! = 720