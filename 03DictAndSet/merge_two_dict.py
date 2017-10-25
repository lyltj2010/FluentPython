"""
In Python 3.5 or greater: z = {**x, **y}
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
>>> z = {**x, **y}
>>> z['a']
1
>>> z['b']
3
>>> z['c']
4

In Python 2, (or 3.4 or lower) write a function
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
>>> z = x.copy() # make a copy
>>> z.update(y) # update with y, after changing z with success, return None
>>> z['a']
1
>>> z['b']
3
>>> z['c']
4
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
