import numpy as np


class Board(object):

    SHOT_MISSED = 1
    SHOT_HIT = 2
    SHOT_SUNK = 3

    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size))


