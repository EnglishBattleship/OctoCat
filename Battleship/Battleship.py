from Battleship.TopBoard import TopBoard
from Battleship.BottomBoard import BottomBoard


class Battleship(object):

    def __init__(self):
        self.boardSize = 10
        self.boardsP1 = [BottomBoard(self.boardSize), TopBoard(self.boardSize)]
        self.boardsP2 = [BottomBoard(self.boardSize), TopBoard(self.boardSize)]
        self.currentPlayer = 1

    def shoot(self, coord):
        currentBoards = self.getCurrentPlayerBoards()
        otherBoards = self.getOtherPlayerBoards()
        shotResult = otherBoards[0].shoot(coord)
        currentBoards[1].shoot(coord, shotResult)

    def placeBoat(self, boatId, position, direction):
        boards = self.getCurrentPlayerBoards()
        return boards[0].placeBoat(boatId, position, direction)

    def getPlayerBoards(self, player):
        if player == 1:
            return self.boardsP1
        elif player == 2:
            return self.boardsP2
        raise Exception("Unknown current player")

    def getCurrentPlayerBoards(self):
        return self.getPlayerBoards(self.currentPlayer)

    def getOtherPlayerBoards(self):
        return self.getPlayerBoards((self.currentPlayer % 2) + 1)
