"""
Pick a random sample from a sequence like object
Only method __len__ and __getitem__ needed
"""
from random import choice

lst = [1, 2, 3, 4, 5]
print(choice(lst))
