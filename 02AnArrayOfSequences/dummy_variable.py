"""
We can assign _ to a variable which we are not interested
>>> for _ in range(2):
...     print("Hi")
...
Hi
Hi
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
