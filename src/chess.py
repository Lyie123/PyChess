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
    White -> upper case
    Black -> lower case
    """
    fen_starting_position = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    def __init__(self, fen: str = fen_starting_position):
        self._columns = list('ABCDEFGH')
        self._rows = list('12345678')
        self._board = []
        self.__init_fen(fen)

    def __str__(self):
        # replace None with empty character
        buffer = [n if n is not None else ' ' for n in self._board]

        # chunk list into 8 pieces and join togehter as string
        return '\n'.join([''.join(buffer[n*8:(n+1)*8]) for n in range(8)])

    def __init_fen(self, fen: str):
        """
        Create Board with position dependent of FEN string
        """
        fen_sep = fen.split(' ')

        fen_board = fen_sep[0]
        for n in fen_board:
            if n == '/':
                pass
            elif n.isnumeric():
                for pawn in range(int(n)):
                    self._board.append(None)
            else:
                self._board.append(n)

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
