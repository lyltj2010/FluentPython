"""
A function to compute the mean of an ever increasing
series of values.
>>> avg = Averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
"""

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
