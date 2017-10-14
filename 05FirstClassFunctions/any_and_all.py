"""
all(iterable)
Return True if every element of the iterable is truthy; all([]) returns True
>>> all([0, 1, 3])
False
>>> all([1, 1, 3])
True
>>> all([])
True

# Equivalent to
>>> def all(iterable):
...     for element in iterable:
...         if not element:
...             return False
...     return True

any(iterable)
Return True if any element of the iterable is true. If the iterable is empty, return False
>>> any([0, 0, 1])
True
>>> any([0, 0, 0])
False
>>> any([])
False

# Equivalent to
>>> def any(iterable):
...     for element in iterable:
...         if not element:
...             return True
...     return False
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
