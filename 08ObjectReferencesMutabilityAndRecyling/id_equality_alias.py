"""
Python variables are like Java reference vairables, Just think
of them as labels attached to objects. They are not boxes.

>>> charles = {'name': 'Charles Dodgson', 'born': 1832}
>>> lewis = charles # alising
>>> lewis is charles
True
>>> id(lewis) == id(charles) # they point to the same object
True
>>> lewis['balance'] = 950
>>> charles['balance'] # also changed
950
>>> alex = {'name': 'Charles Dodgson', 'born': 1832, 'balance': 950}
>>> alex == charles # __eq__
True
>>> alex is not charles
True
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
