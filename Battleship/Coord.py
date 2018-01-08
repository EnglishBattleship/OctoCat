

class Coord(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getName(self):
        return self.x + str(self.y + 1)