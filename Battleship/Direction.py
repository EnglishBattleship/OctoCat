import math

class Direction(object):

    RIGHT = 0
    LEFT = math.pi
    UP = math.pi/2
    DOWN = 3/2*math.pi

    def __init__(self, direction):
        self.direction = direction

    def getDirection(self):
        if self.direction == self.RIGHT:
            return [1,0]
        if self.direction == self.LEFT:
            return [-1,0]
        if self.direction == self.UP:
            return [0,1]
        if self.direction == self.DOWN:
            return [0,-1]
        else :
            return None