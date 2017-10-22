"""
* Given a function, a partial produces a new callable with 
    some of the arguments of the original function fixed.
* This is useful to adapt a function that takes one or more 
    arguments to an API that requires a callback with less arguments.
>>> from functools import partial
>>> base2 = partial(int, base=2)
>>> base2('110')
6

>>> from operator import mul
>>> triple = partial(mul, 3)
>>> triple(5)
15
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
