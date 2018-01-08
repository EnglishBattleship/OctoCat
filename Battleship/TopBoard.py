from Battleship.Board import Board


class TopBoard(Board):

    def __init__(self, size):
        super(TopBoard, self).__init__(size)

    def shoot(self, shotCoord, shotResult):
        self.board[shotCoord.x, shotCoord.y] = shotResult
