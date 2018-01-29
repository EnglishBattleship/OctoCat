from Battleship.Coord import Coord
from Battleship.Direction import Direction


class Boat(object):

    def __init__(self, id, name, length, coord=Coord(0,0), direction=Direction(Direction.RIGHT)):
        self.id = id # int
        self.name = name # string
        self.length = length #int
        self.position = coord # object : the coordonates of the rear of the boat
        self.direction = direction # object
        self.squares = self.initSquares() # dict, keys : coordonates, values : 0 or 1

    def replace(self, direction, position):
        self.direction = direction
        self.position = position
        self.squares = self.initSquares()

    def getCoords(self):
        coords = [self.position]
        for i in range(self.length-1):
            coords.append(Coord(self.position.x + (i+1)*self.direction.getDirection()[0], self.position.y + (i+1)*self.direction.getDirection()[1]))
        return coords

    def isInBoard(self, boardSize):
        coords = self.getCoords()
        for coord in coords:
            if 0 > coord.x or coord.x > boardSize - 1 or 0 > coord.y or coord.y > boardSize - 1:
                return False
        return True

    def initSquares(self):
        squares = {}
        for coord in self.getCoords():
            squares[coord] = 0
        return squares

    def shoot(self, targetCoord): # target : coordonates of the target
        for square in self.squares:
            if square == targetCoord:
                self.squares[square] = 1

    def isDestroyed(self):
        for square in self.squares:
            if self.squares[square] != 1:
                return False
        return True


if __name__ == '__main__':
    boat = Boat(0, 'toto', 4, Coord(0,0), Direction(Direction.RIGHT))
    print(boat.squares)
    boat.shoot(Coord(0,0))
    boat.shoot(Coord(1, 0))
    boat.shoot(Coord(2, 0))
    boat.shoot(Coord(3, 0))
    print(boat.squares)
    print(boat.isDestroyed())