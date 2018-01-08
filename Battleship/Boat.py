import math
from Coord import Coord
from Direction import Direction

class Boat(object):

    def __init__(self, id, name, length, coord=Coord(0,0), direction=Direction(0)):
        self.id = id # int
        self.name = name # string
        self.length = length #int
        self.position = coord # object : the coordonates of the rear of the boat
        self.direction = direction # object
        self.coords = self.getCoords()
        self.squares = self.setSquares() # dict, keys : coordonates, values : 0 or 1

    def getCoords(self):
        Coords = [self.position]
        for i in range(self.length-1):
            Coords.append(Coord(self.position.x + (i+1)*self.direction.getDirection()[0], self.position.y + (i+1)*self.direction.getDirection()[1]))
        return Coords

    def setSquares(self):
        squares = {}
        for i in range(len(self.coords)):
            squares[self.coords[i]] = 0
        return squares

    def shoot(self, cibleCoord): # cible : coordonates of the cible
        cible = [cibleCoord.x, cibleCoord.y]
        for x in self.squares:
            if [x.x, x.y] == cible :
                self.squares[x] = 1


    def isDestroyed(self):
        for x in self.squares:
            if self.squares[x] != 1:
                return False
        return True


if __name__ == '__main__':
    boat = Boat(0, 'toto', 4, Coord(0,0), Direction(0))
    print(boat.squares)
    boat.shoot(Coord(0,0))
    boat.shoot(Coord(1, 0))
    boat.shoot(Coord(2, 0))
    boat.shoot(Coord(3, 0))
    print(boat.squares)
    print(boat.isDestroyed())