"""
Genexp saves memory because it yields items one by one using the iterator
protocal instead of building a whole list just to feed another constructor.
Just use () instead of []
A list with all 6 tshirts variations is never produced in this example
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
...     print(tshirt)
... 
black S
black M
black L
white S
white M
white L
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
