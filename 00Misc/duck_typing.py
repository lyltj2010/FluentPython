"""
If it looks like a duck and quacks like a duck, it's a duck.
The idea is that you don't need a type in order to invoke an existing
    method on an object - if a method is defined on it, you can invoke it.
Like the following example:
    list.extend() support list, tuple, str and any other iterable class
>>> lst = []
>>> l = [1, 2]
>>> t = (3, 4)
>>> s = "Hi"
>>> lst.extend(l)
>>> lst
[1, 2]
>>> lst.extend(t)
>>> lst
[1, 2, 3, 4]
>>> lst.extend(s)
>>> lst
[1, 2, 3, 4, 'H', 'i']
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
