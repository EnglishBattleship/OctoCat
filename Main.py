from Battleship.Battleship import Battleship
from Battleship.Coord import Coord
from Battleship.Direction import Direction


if __name__ == "__main__":
    battleship = Battleship()
    battleship.placeBoat(1, Coord(3,3), Direction(Direction.RIGHT))
    for c in battleship.boardsP1[0].boats[1].getCoords():
        print(c)
