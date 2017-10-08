"""
In python3 this test will pass, but in python2, you will get 'o'
In python2, listcomps don't have their local scope
>>> x = "Hi"
>>> dummy = [x for x in "Hello"]
>>> x
'Hi'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
