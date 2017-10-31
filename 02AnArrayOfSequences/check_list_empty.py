"""
Pythonic way to check if a list is empty
Using the implicit booleanness of the empty list.
>>> lst = []
>>> bool(lst)
False
>>> if not lst:
...     print("Empty list!")
... 
Empty list!
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
