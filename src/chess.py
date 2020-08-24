from itertools import product
from enum import Enum

class Color(Enum):
    """
    Represent the owner of the figure
    """
    WHITE = 0
    BLACK = 1

class Board:
    """
    Represent a chessboard
    A chessboard is represented by a FEN string
    Wiki: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    """
    fen_starting_position = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    def __init__(self, fen: str = fen_starting_position):
        self._columns = list('ABCDEFGH')
        self._rows = list('12345678')
        self._board = dict.fromkeys([''.join(n) for n in product(self._columns, self._rows)])

    def __str__(self):
        board = []
        board.append(' ' + ''.join(self._columns) + '\n')
        for row in self._rows:
            board.append(row)
            for column in self._columns:
                board.append(self._board[column+row])
            board.append('\n')
        return ''.join(map(lambda x: '-' if x is None else x, board))

class Figure:
    """
    Abstract class for chess figures
    """
    def __init__(self, color: Color):
        self.color = color

class Pawn(Figure):
    pass

class Rook(Figure):
    pass

class Bishop(Figure):
    pass

class Knight(Figure):
    pass

class Queen(Figure):
    pass

class King(Figure):
    pass
