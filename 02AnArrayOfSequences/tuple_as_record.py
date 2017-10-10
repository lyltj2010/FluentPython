"""
Tuple can be used as record with no field names.
The number of items is fixed and their order matters!
>>> city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
>>> city
'Tokyo'
>>> year
2003

A list of tupels of the form (country_code, passport_number)
>>> traveler_ids = [('USA', '31195855'), ('UK', '30002109')]
>>> for country, _ in traveler_ids:
...     print(country)
...
USA
UK
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
