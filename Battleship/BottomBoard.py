from Battleship.Board import Board
from Battleship.Boat import Boat


class BottomBoard(Board):

    def __init__(self, size):
        super(BottomBoard, self).__init__(size)
        self.boats = dict()
        self.availableBoats = {
            0: Boat(0, "Aircraft Carrier", 5),
            1: Boat(1, "Battleship", 4),
            2: Boat(2, "Submarine", 3),
            3: Boat(3, "Destroyer", 3),
            4: Boat(4, "Patrol Boat", 2)
        }

    def shoot(self, shotCoord):
        shotResult = self.getShotResult(shotCoord)
        self.board[shotCoord.x, shotCoord.y] = shotResult
        return shotResult

    def getShotResult(self, shotCoord):
        for boat in self.boats.values():
            coords = boat.getCoords()
            for coord in coords:
                if shotCoord == coord:
                    boat.shoot(shotCoord)
                    if boat.isDestroyed():
                        return self.SHOT_SUNK
                    else:
                        return self.SHOT_HIT
        return self.SHOT_MISSED

    def getAvailableBoats(self):
        return self.availableBoats

    def placeBoat(self, boatId, position, direction):
        if boatId not in self.availableBoats.keys():
            raise Exception("Unavailable boat")
        newBoat = self.availableBoats[boatId]
        newBoat.position = position
        newBoat.direction = direction
        newCoords = newBoat.getCoords()
        for boat in self.boats.values():
            coords = boat.getCoords()
            for coord in newCoords:
                if coord in coords:
                    return False
        self.availableBoats.pop(boatId)
        self.boats[boatId] = newBoat
        return True