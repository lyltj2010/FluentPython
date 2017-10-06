from math import hypot


class Vector:
    """
    A class emulating numeric types.
    Some of the special methods usage are demonstrated here.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Or you will see sth like <__main__.Vector object at 0x10f673dd8>
        The str returned by __repr__ should be unambiguous,if possible,match
        the source code necessary to recreate the object being represented.
        >>> Vector(3, 4) # test __repr__
        Vector(3, 4)
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        """
        >>> abs(Vector(3, 4)) # test __abs__
        5.0
        """
        return hypot(self.x, self.y)

    def __bool__(self):
        """
        >>> bool(Vector(1, 2)) # test __bool__
        True
        >>> bool(Vector(0, 0))
        False
        """
        return bool(self.x or self.y)

    def __add__(self, other):
        """
        >>> Vector(1, 1) + Vector(1, 2) # test __add__
        Vector(2, 3)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        """
        >>> Vector(1, 1) * 3 # test __mul__
        Vector(3, 3)
        """
        x = other * self.x
        y = other * self.y
        return Vector(x, y)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
