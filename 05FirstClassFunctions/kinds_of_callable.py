"""
See the seven flavors of callable objects
>>> abs, str, 13
(<built-in function abs>, <class 'str'>, 13)
>>> [callable(obj) for obj in (abs, str, 13)]
[True, True, False]
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
