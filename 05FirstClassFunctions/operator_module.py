"""
It is convenient to use an arithmetic operator as a function
The operator module save you the trouble of writting trivial
anonymous functions like `lambda a, b: a * b`
>>> from functools import reduce
>>> import operator
>>> from operator import mul
>>> def fact1(n):
...     return reduce(lambda a, b: a*b, range(1, n+1))
>>> def fact(n): # use mul
...     return reduce(mul, range(1, n+1))
>>> mul(3, 4) # behaves like a function
12
>>> type(mul)
<class 'builtin_function_or_method'>
>>> fact1(5)
120
>>> fact(5)
120

# Have a look at what operator provides
>>> names = [name for name in dir(operator) if not name.startswith('_')]
>>> for name in names:
...     print(name)
...
abs
add
and_
attrgetter
concat
contains
countOf
delitem
eq
floordiv
ge
getitem
gt
iadd
iand
iconcat
ifloordiv
ilshift
imatmul
imod
imul
index
indexOf
inv
invert
ior
ipow
irshift
is_
is_not
isub
itemgetter
itruediv
ixor
le
length_hint
lshift
lt
matmul
methodcaller
mod
mul
ne
neg
not_
or_
pos
pow
rshift
setitem
sub
truediv
truth
xor
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
