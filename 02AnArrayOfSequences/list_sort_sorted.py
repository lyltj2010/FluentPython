"""
list.sort sort a list in place and return None
Important Python API:
    Functions or methods that change an object in-place should return None
    to make it clear to the caller that the object itself was changed, and
    no new object was created. The same behavior can be seen, for example,
    in the random.shuffle function.
>>> a = [1, 3, 2]
>>> a.sort(reverse = True) # return None
>>> a
[3, 2, 1]
>>> from random import shuffle
>>> shuffle(a) == None
True

sorted(support any iterable object) create a new list and return it
>>> fruits = ['grape', 'raspberry', 'apple', 'banana']
>>> sorted(fruits, reverse=True)
['raspberry', 'grape', 'banana', 'apple']
>>> sorted(fruits, key=len)
['grape', 'apple', 'banana', 'raspberry']
>>> fruits # left unchanged
['grape', 'raspberry', 'apple', 'banana']
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
