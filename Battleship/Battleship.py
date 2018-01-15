from Battleship.TopBoard import TopBoard
from Battleship.BottomBoard import BottomBoard


class Battleship(object):

    def __init__(self):
        self.boardSize = 10
        self.boardsP1 = [BottomBoard(self.boardSize), TopBoard(self.boardSize)]
        self.boardsP2 = [BottomBoard(self.boardSize), TopBoard(self.boardSize)]
        self.currentPlayer = 1
        self.winner = None

    def shoot(self, coord):
        currentBoards = self.getCurrentPlayerBoards()
        otherBoards = self.getOtherPlayerBoards()
        shotResult = otherBoards[0].shoot(coord)
        currentBoards[1].shoot(coord, shotResult)
        if shotResult == BottomBoard.SHOT_SUNK:
            won = True
            for boat in otherBoards[0].boats.values():
                if not boat.isDestroyed(): won = False
            if won:
                print("Player {0} won !!".format(self.currentPlayer))
                self.winner = self.currentPlayer

    def nextPlayer(self):
        self.currentPlayer = (self.currentPlayer % 2) + 1

    def placeBoat(self, boatId, position, direction):
        boards = self.getCurrentPlayerBoards()
        return boards[0].placeBoat(boatId, position, direction)

    def getAvailableBoats(self):
        boards = self.getCurrentPlayerBoards()
        return boards[0].availableBoats

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

