"""
A function that takes a function as argument or returns
a function as result is a higher order function.
Like sorted, any one-argument function can be used as the key argument
Other famous higher order functions are map, filter, reduce etc.
>>> def reverse(word):
...     return word[::-1]
>>> reverse("Hello")
'olleH'
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=reverse)
['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
