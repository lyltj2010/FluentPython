"""
Tuple is cannot be changed. But it's items may be mutable
>>> t = (1, 2, [30, 40])
>>> t[2].extend([50, 60])
>>> t
(1, 2, [30, 40, 50, 60])

However`t[2] += [50, 60]` will throw TypeError:
'tuple' object does not support item assignment
And t[2] will be changed at the same time.

+ Putting mutable items in tuples is not a good idea
+ Augmented assignment is not an atomic operations `+=`
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
