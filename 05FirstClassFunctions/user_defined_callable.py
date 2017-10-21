"""
Arbitrary Python objects can be made to behave like functions.
Implementing a __call__ instance method is all it takes.
>>> bingo = BingoCage([1, 1, 1])
>>> bingo.pick()
1
>>> bingo() # what __call__ provides
1
"""
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)  # build a local copy
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
