"""
`enumerate(iterable, start=0)`
Return an enumerate object.
    * iterable must be a sequence, an iterator, or some other object which supports iteration
    * The __next__() method of the iterator returned by enumerate() returns a tuple containing
    * a count (from start which defaults to 0) and the values obtained from iterating over iterable.
>>> sizes = ['S', 'M', 'L', 'XL']
>>> list(enumerate(sizes))
[(0, 'S'), (1, 'M'), (2, 'L'), (3, 'XL')]
>>> list(enumerate(sizes, start=1))
[(1, 'S'), (2, 'M'), (3, 'L'), (4, 'XL')]

# Equivalent to:
>>> def enumerate(sequence, start=0):
...     n = start
...     for elem in sequence:
...         yield n, elem
...         n += 1
>>> list(enumerate(sizes, start=1))
[(1, 'S'), (2, 'M'), (3, 'L'), (4, 'XL')]
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
