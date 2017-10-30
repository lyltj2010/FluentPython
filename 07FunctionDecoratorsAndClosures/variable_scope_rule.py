"""
# No Surprise
>>> b = 6
>>> def f(a):
...     print(a)
...     print(b)
>>> f(3)
3
6

# This may suprise you
>>> b = 6
>>> def f1(a):
...     print(a)
...     print(b)
...     b = 9

By calling f1(3) you will get
3 
Traceback(most recent call last):
    File "<stdin>", line 1 ...
    File "<stdin>", line 3 ...
UnboundLocalError: local variable 'b' referenced before assignment

It is Unbound(not assigned) Local(inside the function) Error!

The fact is:
1. When Python compiles the body of the function, it decides that b is a local
   variable because it is assigned within the function
2. It will fetch b from the local environment and find it is unbound
3. It is a design choice
   Python does not require you to declare variables
   but assumes that a variable assigned in the body of a function is local
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
