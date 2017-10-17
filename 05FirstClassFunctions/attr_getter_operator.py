"""
Return a callable object that fetches attr(by name) from its operand
* After f = attrgetter('name'), the call f(b) returns b.name.
* After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date)
* After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last)
If several attribute names given as arguments, it returns a tuple of values
If any argument name contains a.(dot), attrgetter navigates through nested objects to retrieve the attribute
>>> from collections import namedtuple
>>> metro_data = [
... ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
... ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
... ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
... ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
... ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
>>> LatLong = namedtuple('LatLong', 'lat long')
>>> Metropolis = namedtuple('Metropolis', 'name cc pop coord')
>>> metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
...     for name, cc, pop, (lat, long) in metro_data]
>>> metro_areas[0]
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722, long=139.691667))
>>> metro_areas[0].coord.lat
35.689722
>>> from operator import attrgetter
>>> name_lat = attrgetter('name', 'coord.lat') # define a attrgetter
>>> for city in sorted(metro_areas, key=attrgetter('coord.lat')):
...     print(name_lat(city))
('Sao Paulo', -23.547778)
('Mexico City', 19.433333)
('Delhi NCR', 28.613889)
('Tokyo', 35.689722)
('New York-Newark', 40.808611)
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
