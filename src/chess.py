from enum import Enum
from abc import ABC
from typing import List

class Color(Enum):
    """
    Represent the owner of the figure
    """
    WHITE = 0
    BLACK = 1

class Game:
    """
    """
    def __init__(self, fen: str):
        self._fen = fen.split(' ')
        self.player_white = Player(Color.WHITE)
        self.player_black = Player(Color.BLACK)

        # resolve fen

        # piece placement
        self.board = Board(self._fen[0])

        # active color
        if self._fen[1] == 'w':
            self.active_color = Color.WHITE
        elif self._fen[1] == 'b':
            self.active_color = Color.BLACK
        else:
            raise ValueError

        # castling availability

        # en passant

        # halfmove clock

        # fullmove number

    def move(self):
        pass

class Player:
    """
    """
    def __init(self, color: Color):
        self.color = color

class PieceType(Enum):
    """
    """
    PAWN = 'p'
    ROOK = 'r'
    BISHOP = 'b'
    KNIGHT = 'n'
    QUEEN = 'q'
    KING = 'k'

class Piece(ABC):
    """
    Abstract class for chess figures
    """
    def __init__(self, piece_type: PieceType, color: Color):
        self.color = color
        self.type = piece_type
    
    def __str__(self):
        return str(self.type.value) if self.color == Color.BLACK else str(self.type.value).upper()

class Pawn(Piece):
    def __init__(self, color: Color):
       super().__init__(PieceType.PAWN, color)

class Rook(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.ROOK, color)

class Bishop(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.BISHOP, color)

class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.KNIGHT, color)

class Queen(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.QUEEN, color)

class King(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.KING, color)


class Board:
    """
    Represent a chessboard
    A chessboard is represented by a FEN string
    Wiki: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    White -> upper case
    Black -> lower case
    """
    fen_starting_position = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

    def __init__(self, piece_placement: str):
        self._columns = list('ABCDEFGH')
        self._rows = list('12345678')
        self._squares = { (m+j):(i*8+n) for i, j in enumerate(self._rows) for n, m in enumerate(self._columns) }
        self._board = []
        self.__init_board(piece_placement)

    def __str__(self) -> str:
        # replace None with empty character
        rows = [str(n) if n is not None else '-' for n in self._board]
        # chunk list into 8 pieces and join togehter as string
        rows = [rows[i:i+8]  for i in range(0, len(rows), 8)]
        # reverse list to match match prefered chess board view
        rows = rows[::-1]

        return '\n'.join([' '.join(n) for n in rows])

    def __init_board(self, fen: str) -> None:
        """
        Create Board with position depending on FEN string
        """
        fen_sep = fen.split(' ')

        fen_board = fen_sep[0]

        # extend fen string
        board = []
        for section in fen_board.split('/'):
            buffer = []
            for n in section:
                if n.isnumeric():
                    buffer.extend([None for p in range(int(n))])
                else:
                    color = Color.WHITE if n.isupper() else Color.BLACK

                    if n in 'Rr':
                        buffer.append(Rook(color))
                    elif n in 'Nn':
                        buffer.append(Knight(color))
                    elif n in 'Bb':
                        buffer.append(Bishop(color))
                    elif n in 'Qq':
                        buffer.append(Queen(color))
                    elif n in 'Kk':
                        buffer.append(King(color))
                    elif n in 'Pp':
                        buffer.append(Pawn(color))
                    else:
                        raise ValueError

            board.append(buffer)

        board.reverse()
        for n in board:
            self._board.extend(n)


    def get_square(self, square: str) -> str:
        """
        Return figure of the given square
        """
        if square not in self._squares:
            raise ValueError
        else:
            return self._board[self._squares[square]]

    def get_row(self, row: str) -> List[str]:
        if row not in self._rows:
            raise ValueError
        list_index = [self._squares[n] for n in self._squares.keys() if row in n]
        return [self._board[n] for n in list_index]
    
    def get_column(self, column: str) -> List[str]:
        if column not in self._columns:
            raise ValueError
        list_index = [self._squares[n] for n in self._squares.keys() if column in n]
        return [self._board[n] for n in list_index]

    def get_pieces(self, piece:PieceType, color: Color=None) -> List[Piece]:
        return [n for n in self._board if n.type == piece and n.color == color]