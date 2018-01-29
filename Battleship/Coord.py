

class Coord(object):

    def __init__(self, x, y, board=-1):
        self.x = int(x)
        self.y = int(y)
        self.board = board

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))