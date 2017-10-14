"""
function is an instance of the function class
>>> def factorial(n):
...     '''Return n!'''
...     return 1 if n < 2 else n * factorial(n-1)
...
>>> factorial(5)
120
>>> type(factorial)
<class 'function'>
>>> factorial.__doc__ # __doc__ is one of its attributes
'Return n!'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
