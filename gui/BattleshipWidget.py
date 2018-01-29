import sys, os
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter, QFont
from PyQt5.QtCore import QRect
from random import randint

from gui.BattleshipPainter import BattleshipPainter
from Battleship.Coord import Coord
from Battleship.Battleship import Battleship
from Battleship.Direction import Direction
from Battleship.Board import Board


class BattleshipWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.loadBoatImages()
        self.initBattleship()
        self.initUI()

    def loadBoatImages(self):
        self.boatImages = [QImage(os.getcwd() + '/gui/Sheeps/Sheep.png'),
            QImage(os.getcwd() + '/gui/Sheeps/Sheep_bouee.png'),
            QImage(os.getcwd() + '/gui/Sheeps/Sheep_pedalo.png'),
            QImage(os.getcwd() + '/gui/Sheeps/Sheep_surf.png'),
            QImage(os.getcwd() + '/gui/Sheeps/Sheep_pimp.png')]

    def initBattleship(self):
        self.placingBoats = True
        self.directions = [Direction(Direction.RIGHT), Direction(Direction.DOWN)]#, Direction(Direction.LEFT), Direction(Direction.UP)]
        self.placingDirection = 0
        self.currentBoat = None
        self.currentBotBoat=None
        self.battleship = Battleship()
        self.placeBotBoats()

    def placeBotBoats(self):
        self.battleship.nextPlayer()
        while len(self.battleship.getAvailableBoats().keys()) > 0:
            self.currentBotBoat = next(iter(self.battleship.getCurrentPlayerBoards()[0].getAvailableBoats().values()))            
            self.currentBotBoat.replace(self.directions[randint(0,1)],  Coord(randint(0,9), randint(0,9)))
            if self.currentBotBoat.isInBoard(self.battleship.boardSize):
                self.battleship.placeBoat(self.currentBotBoat.id, self.currentBotBoat.position, self.currentBotBoat.direction)
        self.battleship.nextPlayer()

    def initUI(self):
        self.texts = ["Place your boats"]
        self.setMouseTracking(True)
        self.setWindowTitle('Battleship')
        self.show()

    def mouseMoveEvent(self, e):
        if self.placingBoats:
            coord = self.getSquareCoord(e.x(), e.y())
            if coord is None or coord.board == 1:
                return
            if self.currentBoat is None and len(self.battleship.getAvailableBoats().keys()) > 0:
                self.currentBoat = next(iter(self.battleship.getCurrentPlayerBoards()[0].getAvailableBoats().values()))
            elif self.currentBoat is None:
                self.placingBoats = False
                self.update()
                self.texts.append("Your turn")
                return
            self.currentBoat.replace(self.directions[self.placingDirection], coord)
            self.update()

    def mousePressEvent(self, e):
        if e.button() == 1:
            self.onMouseLeftClicked(e)
        elif e.button() == 2:
            self.onMouseRightClicked(e)

    def onMouseLeftClicked(self, e):
        coord = self.getSquareCoord(e.x(), e.y())
        if self.placingBoats:
            if coord is not None and coord.board == 0 and self.currentBoat.isInBoard(self.battleship.boardSize):
                self.battleship.placeBoat(self.currentBoat.id, self.currentBoat.position, self.currentBoat.direction)
                self.currentBoat = None
        elif coord is not None and coord.board == 1 and self.battleship.getCurrentPlayerBoards()[1].getCoord(coord) == 0:
            result = self.battleship.shoot(coord)
            self.update()
            if result == Board.SHOT_MISSED:
                self.texts.append("You missed ! Wait for the computer to play.")
                self.battleship.nextPlayer()
                timer = QTimer(self)
                timer.setSingleShot(True)
                timer.timeout.connect(self.startBotTurn)
                timer.start(500)
            elif result == Board.SHOT_SUNK:
                self.texts.append("Boat sunk ! Shoot again !")
            else:
                self.texts.append("Well done ! You can shoot again !")
            if self.battleship.winner is not None:
                self.texts.append("Player {0} won !!".format(self.battleship.winner))

    def onMouseRightClicked(self, e):
        if self.placingBoats:
            self.placingDirection = (self.placingDirection + 1) % len(self.directions)
            if self.currentBoat is not None:
                coord = self.getSquareCoord(e.x(), e.y())
                self.currentBoat.replace(self.directions[self.placingDirection], coord)
                self.update()

    def startBotTurn(self):
        self.battleship.botTurn()
        self.battleship.nextPlayer()
        self.texts.append("Your turn")
        self.update()

    def paintEvent(self, e):
        x1, y1, x2, y2, squareSize = self.getBoardCoords()
        qp = BattleshipPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.drawGrid(x1, y1, squareSize)
        qp.drawGrid(x2, y2, squareSize)
        qp.drawBoats(self.battleship.getPlayerBoards(1)[0].boats, self.boatImages, x1, y1, x2, y2, squareSize)
        boards = self.battleship.getPlayerBoards(1)
        for i in range(2):
            for x in range(self.battleship.boardSize):
                for y in range(self.battleship.boardSize):
                    coord = Coord(x, y)
                    square = boards[i].getCoord(coord)
                    if square in [Board.SHOT_SUNK, Board.SHOT_HIT]:
                        qp.drawHitShot(self.getSquareRect(coord, i))
                    elif square == Board.SHOT_MISSED:
                        qp.drawMissedShot(self.getSquareRect(coord, i))
        if self.placingBoats and self.currentBoat is not None:
            qp.drawBoats({0: self.currentBoat}, self.boatImages, x1, y1, x2, y2, squareSize)
        nbTexts = len(self.texts)
        font = QFont("Arial", 42)
        qp.setFont(font)
        for k in range(max(0, nbTexts-1), nbTexts):
            qp.drawText(self.width() / 2 - len(self.texts[k]) * 12,  60 + (nbTexts - k) * 20, self.texts[k])
        qp.end()

    def getPlayerBoatsRect(self):
        rects = []
        for boat in self.battleship.getPlayerBoards(1)[0].boats.values():
            for coord in boat.getCoords():
                rects.append(self.getSquareRect(coord, 0))
        return rects

    def getSquareRect(self, coord, board):
        x1, y1, x2, y2, squareSize = self.getBoardCoords()
        x, y = 0, 0
        if board == 0:
            x = x1 + coord.y * squareSize
            y = y1 + coord.x * squareSize
        elif board == 1:
            x = x2 + coord.y * squareSize
            y = y2 + coord.x * squareSize
        return QRect(x, y, squareSize, squareSize)

    def getSquareCoord(self, x, y):
        x1, y1, x2, y2, squareSize = self.getBoardCoords()
        if x1 < x < x1 + squareSize * 10 and y1 < y < y1 + squareSize * 10:
            return Coord((y - y1)//squareSize, (x - x1)//squareSize, 0)
        elif x2 < x < x2 + squareSize * 10 and y2 < y < y2 + squareSize * 10:
            return Coord((y - y2) // squareSize, (x - x2) // squareSize, 1)
        return None

    def getBoardCoords(self):
        width = self.width()
        height = self.height()
        marginX = 0.08 * width
        boardSize = 0.38 * width
        marginY = (height - boardSize) * 0.8
        return marginX, marginY, width - marginX - boardSize, marginY, boardSize / 10


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = BattleshipWidget(app)
    sys.exit(app.exec_())
