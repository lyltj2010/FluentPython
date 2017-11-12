"""
# One item
>>> [1, 2, 3, 4, 1, 4, 1].count(1)
3

# Each item
>>> from collections import Counter
>>> lst = [1, 2, 3, 4, 1, 4, 1]
>>> counter = Counter(lst)
>>> counter[1]
3
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
