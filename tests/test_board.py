import os, sys
sys.path.append(os.path.abspath('..'))
import pytest
import src.chess as chess

class TestBoard:
    @pytest.fixture
    def create_board(self):
        self.board = chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

    def test_get_row(self, create_board):
        assert ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] == [str(n) for n in self.board.get_row('1')]
        assert [None, None, None, None, None, None, None, None]  == self.board.get_row('4')
        assert ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'] == [str(n) for n in self.board.get_row('8')]
        with pytest.raises(ValueError):
            self.board.get_row('9')
        with pytest.raises(ValueError):
            self.board.get_row('0')

    def test_board_data(self, create_board):
        pass