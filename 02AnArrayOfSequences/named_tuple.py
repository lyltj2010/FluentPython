"""
The collections.namedtuple function is a factory that produces
subclasses of tuple enhanced with field names and a class name
>>> from collections import namedtuple
>>> Card = namedtuple('Card', ['rank', 'suit']) # list of field names
>>> Card('A', 'spades')
Card(rank='A', suit='spades')

>>> City = namedtuple('City', 'name country population coordinates')
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
>>> tokyo.coordinates
(35.689722, 139.691667)
>>> tokyo[0]
'Tokyo'

# Additional attributes apart that inherited from tuple
# fields are stored in class
>>> City._fields # class attribute
('name', 'country', 'population', 'coordinates')
>>> LatLong = namedtuple('LatLong', 'lat long')
>>> delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
>>> delhi = City._make(delhi_data) # class method
>>> delhi.country
'IN'
>>> delhi._asdict()
OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population', 21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
