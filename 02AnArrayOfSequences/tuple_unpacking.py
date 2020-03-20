"""
# Parallel Assignment
>>> lax_coordinates = (33.94, -18.41)
>>> latitude, longitude = lax_coordinates
>>> latitude
33.94
>>> longitude
-18.41


# Swapping values of variables
>>> a = 1; b = 2
>>> a, b = b, a
>>> a
2


# Prefixing an argument with a star when calling a funnction
>>> divmod(20, 8) # 8 * 2 + 4 = 20
(2, 4)
>>> t = (20, 8)
>>> divmod(*t)
(2, 4)
>>> quotient, remainder = divmod(*t)
>>> quotient
2


# Using * to grab excess items, *args
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])
>>> a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)


# Nested tuple unpacking
>>> area = ('Tokyo', 'JP', 36.933, (35.6897, 139.6917))
>>> name, cc, pop, (latitude, longitude) = area
>>> cc
'JP'
>>> latitude
35.6897
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
