import collections

"""
>>> Card('7', 'diamonds')
Card(rank='7', suit='diamonds')
"""
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    By implenting __len__ and __getitem__, you leverage the Python Data Model
    >>> deck = FrenchDeck()
    >>> len(deck) # what __len__ provides
    52

    >>> deck[0] # what __getitem__ provides
    Card(rank='2', suit='spades')

    >>> deck[:2] # with slicing supported
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades')]

    >>> for card in reversed(deck): # with iteration supported
    ...     print(card);
    ...     break
    Card(rank='A', suit='hearts')
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
