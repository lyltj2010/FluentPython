"""
The == operator compares the values of objecs(the data they hold)
`is` compares their ids

When comparing a variable to a singleton, use `is` is better
>>> x = None
>>> x is None
True
>>> x is not None
False
>>> a = 1
>>> b = 1
>>> a == b
True    
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
