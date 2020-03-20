"""
use named tuple to build class with bundles of attributes
no custom methods, just like database record
"""
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])
card = Card('7', 'diamonds')
print(card)  # Card(rank='7', suit='diamonds')
