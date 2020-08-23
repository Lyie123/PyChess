from itertools import product

class Board:

    def __init__(self):
        self._column = list('ABCDEFGH')
        self._row = list('12345678')
        self._board = [''.join(n) for n in product(self._column, self._row)]
