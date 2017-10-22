"""
Return a new partialmethod descriptor which behaves like partial except that
it is designed to be used as a method definition rather than being directly callable
>>> c = Cell()
>>> c.alive
False
>>> c.set_alive()
>>> c.alive
True
"""

from functools import partialmethod


class Cell(object):
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
