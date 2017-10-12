"""
Basic usage of slicing
>>> s = 'bicycle'
>>> s[::3]
'bye'
>>> s[::-1] # reversed
'elcycib'
>>> s[::-2] # backword steping
'eccb'

Advanced form of slicing.
a:b:c is only valid within [] when used as the indexing or
subscript operator, and it produces a slice object: slice(a, b, c)

>>> invoice0 = "0.....6.................................40........52...55........"
>>> invoice1 = "1909  Pimoroni PiBrella                     $17.50    3    $52.50"
>>> invoice2 = "1489  6mm Tactile Switch x20                 $4.95    2     $9.90"
>>> SKU = slice(0, 6)
>>> DESC = slice(6, 40)
>>> UNIT_PRICE = slice(40, 52)
>>> QUANTITY = slice(52, 55)
>>> ITEM_TOL = slice(55, None)
>>> items = [invoice1, invoice2]
>>> for item in items:
...     print(item[UNIT_PRICE], item[DESC])
... 
    $17.50   Pimoroni PiBrella                 
     $4.95   6mm Tactile Switch x20            
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
