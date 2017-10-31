"""
append: Appends object at end.
extend: Extends list by appending elements from the iterable.
>>> x1 = [1, 2, 3]
>>> x2 = [1, 2, 3]
>>> y = [4, 5]
>>> x1.append(y)
>>> x1
[1, 2, 3, [4, 5]]
>>> x2.extend(y)
>>> x2
[1, 2, 3, 4, 5]
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
