"""
Keeping track all the series is not efficient
Just keep the count and total.
Use nonlocal in Python3
    * Flag a variable as a free variable even it is assigned
    * a new value within the function
    * Otherwise, immutable types in closure can never be assigned,
    * because it will be marked as local
Workarounds of nonlocal in Python2
    * Python2 lacks nonlocal keyword
    * Store the variables the inner functions need to change as items
    * or attributes of some mutable object, like dict or simple instance
    * and bind that object to a free variable
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
"""

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        """Without nonlocal, UnboundLocalError will be raised."""
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

if __name__ == "__main__":
    import doctest
    doctest.testmod()
