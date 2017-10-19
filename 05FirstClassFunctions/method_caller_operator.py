"""
Return a callable object that calls the method name on its operand.
If additional arguments and/or keyword arguments are given, they 
will be given to the method as well
* After f = methodcaller('name'), the call f(b) returns b.name().
* After f = methodcaller('name', 'foo', bar=1), the call f(b) returns b.name('foo', bar=1).

# def methodcaller(name, *args, **kwargs):
#     def caller(obj):
#         return getattr(obj, name)(*args, **kwargs)
#     return caller

>>> from operator import methodcaller
>>> s = 'The time has come'
>>> upcase = methodcaller('upper')
>>> upcase(s)
'THE TIME HAS COME'
>>> s.upper()
'THE TIME HAS COME'
>>> hiphenate = methodcaller('replace', ' ', '-')
>>> hiphenate(s)
'The-time-has-come'

# Equivalent to:
>>> def methodcaller(name, *args, **kwargs):
...     def caller(obj):
...         return getattr(obj, name)(*args, **kwargs)
...     return caller
>>> tidle = methodcaller('replace', ' ', '~')
>>> tidle(s)
'The~time~has~come'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
