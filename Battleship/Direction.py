import math


class Direction(object):

    RIGHT = 0
    LEFT = math.pi
    UP = math.pi/2
    DOWN = 3/2*math.pi

    def __init__(self, direction):
        self.direction = direction

    def getDirection(self):
        return [-round(math.sin(self.direction)), round(math.cos(self.direction))]