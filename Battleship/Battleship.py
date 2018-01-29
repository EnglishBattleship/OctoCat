from Battleship.TopBoard import TopBoard
from Battleship.BottomBoard import BottomBoard
from Battleship.Coord import Coord

import random


class Battleship(object):

    def __init__(self):
        self.boardSize = 10
        self.boardsP1 = [BottomBoard(self.boardSize), TopBoard(self.boardSize)]
        self.boardsP2 = [BottomBoard(self.boardSize), TopBoard(self.boardSize)]
        self.currentPlayer = 1
        self.lastHitP2 = None
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
        return shotResult

    def nextPlayer(self):
        self.currentPlayer = (self.currentPlayer % 2) + 1

    def placeBoat(self, boatId, position, direction):
        boards = self.getCurrentPlayerBoards()
        return boards[0].placeBoat(boatId, position, direction)

    def getAvailableBoats(self):
        boards = self.getCurrentPlayerBoards()
        return boards[0].availableBoats

    def getFreeCoord(self):
        return self.getCurrentPlayerBoards()[1].getFreeCoord()

    def advancedShooting(self, lastHit):
        #print(lastHit.x, lastHit.y)
        closestSquares = lastHit.getClosestSquares(self.boardSize)
        potentialTargets = []
        for coord in closestSquares:
            if self.getPlayerBoards(1)[0].getCoord(coord) == 0:
                potentialTargets.append(coord)
        # for c in potentialTargets:
        #     print(c.x, c.y)
        if len(potentialTargets) > 0:
            rand = random.randint(0, len(potentialTargets)-1)
            #print(potentialTargets[rand].x, potentialTargets[rand].y)
            return potentialTargets[rand]
        else:
            return None


    def botTurn(self):
        result = 0
        target = None
        if self.lastHitP2 is not None:
            target = self.advancedShooting(self.lastHitP2)
            if target is not None:
                result = self.shoot(target)
                # print(target)
        if target is None:
            target = self.getFreeCoord()
            result = self.shoot(target)
            # print(target)
        if result == BottomBoard.SHOT_SUNK:
            self.lastHitP2 = None
            self.botTurn()
        elif result == BottomBoard.SHOT_HIT:
            self.lastHitP2 = target
            self.botTurn()


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

