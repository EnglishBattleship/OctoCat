import numpy as np
import random

from Battleship.Coord import Coord


class Board(object):

    SHOT_MISSED = 1
    SHOT_HIT = 2
    SHOT_SUNK = 3

    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size))

    def getCoord(self, coord):
        return self.get(coord.x, coord.y)

    def get(self, x, y):
        return self.board[x, y]

    def getFreeCoord(self):
        coords = []
        for x in range(self.board.shape[0]):
            for y in range(self.board.shape[1]):
                if self.get(x, y) == 0:
                    coords.append(Coord(x, y))
        rand = random.randint(0, len(coords) - 1)
        return coords[rand]


