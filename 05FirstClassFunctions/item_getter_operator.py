"""
A one trick function to pick items from sequences
itemgetter(1) does the same as lambda fields: fields[1]
Return a callable object that fetches item from its operand
using the operand’s __getitem__() method
* After f = itemgetter(2), the call f(r) returns r[2]
* After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
>>> from operator import itemgetter
>>> metro_data = [
... ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
... ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
... ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
... ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
... ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
>>> for city in sorted(metro_data, key=itemgetter(1)):
...     print(city) # sort base on second field
... 
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
('New York-Newark', 'US', 20.104, (40.808611, -74.020386))

Multiple index to itemgetter will return a tuple retrived
>>> cc_name = itemgetter(1, 0)
>>> for city in metro_data:
...     print(cc_name(city))
...
('JP', 'Tokyo')
('IN', 'Delhi NCR')
('MX', 'Mexico City')
('US', 'New York-Newark')
('BR', 'Sao Paulo')
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
