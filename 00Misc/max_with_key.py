"""
>>> lst = [(1, 'a'), (3, 'c'), (4, 'e'), (-1, 'z')]
>>> max(lst)
(4, 'e')
>>> from operator import itemgetter
>>> max(lst, key=itemgetter(1))
(-1, 'z')
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
