

class Coord(object):

    def __init__(self, x, y, board=-1):
        self.x = int(x)
        self.y = int(y)
        self.board = board
        self.targetPosition = None

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def getClosestSquares(self, boardSize):
        coords = []
        temp = [Coord(self.x-1, self.y), Coord(self.x+1, self.y), Coord(self.x, self.y-1), Coord(self.x, self.y+1)]

        for c in temp:
            if 0 <= c.x < boardSize and 0 <= c.y < boardSize:
                    coords.append(c)
        return coords

if __name__ == '__main__':
    c = Coord(9,9)
    for c in c.getClosestSquares(10):
        print(c.x, c.y)