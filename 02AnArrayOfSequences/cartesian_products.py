"""
Listcomp is meant to do one thing only: to build a new list.
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> tshirts = [(color, size) for color in colors for size in sizes] # arranged by color, then size.
>>> tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]


>>> for color in colors:
...     for size in sizes:
...         print((color, size))
...
('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')


>>> tshirts = [(color, size) for size in sizes
...                          for color in colors]  # arranged by size, then color
>>> tshirts
[('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
