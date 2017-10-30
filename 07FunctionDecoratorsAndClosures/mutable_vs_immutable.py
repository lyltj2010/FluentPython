"""
Immutable types like numbers, strings tuples etc
cannot be updated, all you can is read, but never update
>>> a = 1
>>> id1 = id(a)
>>> a += 1
>>> id2 = id(a)
>>> assert id1 != id2

Mutable types can be updated
>>> b = [1]
>>> id3 = id(b)
>>> b.append(2)
>>> id4 = id(b)
>>> assert id3 == id4
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
