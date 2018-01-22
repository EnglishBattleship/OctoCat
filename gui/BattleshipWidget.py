import sys, os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter
from PyQt5.QtCore import QRect

from BattleshipPainter import BattleshipPainter
from Battleship.Coord import Coord
from Battleship.Battleship import Battleship
from Battleship.Direction import Direction
from Battleship.Board import Board


class BattleshipWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.loadBoatImages()
        self.initBattleship()
        self.initUI()

    def loadBoatImages(self):
        self.carrier = QImage(os.getcwd() + '/Carrier_5.jpg')
        self.battleship = QImage(os.getcwd() + '/Battleship_4.png')
        self.cruiser = QImage(os.getcwd() + '/Cruiser_3.png')
        self.submarine = QImage(os.getcwd() + '/Submarine_3.png')
        self.destroyer = QImage(os.getcwd() + '/Destroyer_2.jpg')

    def initBattleship(self):
        self.battleship = Battleship()
        self.battleship.placeBoat(0, Coord(4, 2), Direction(Direction.DOWN))
        self.battleship.placeBoat(1, Coord(0, 1), Direction(Direction.RIGHT))
        self.battleship.placeBoat(2, Coord(3, 8), Direction(Direction.DOWN))
        self.battleship.placeBoat(3, Coord(5, 4), Direction(Direction.DOWN))
        self.battleship.placeBoat(4, Coord(2, 1), Direction(Direction.RIGHT))

        self.battleship.nextPlayer()
        self.battleship.placeBoat(0, Coord(4, 2), Direction(Direction.DOWN))
        self.battleship.placeBoat(1, Coord(0, 1), Direction(Direction.RIGHT))
        self.battleship.placeBoat(2, Coord(3, 8), Direction(Direction.DOWN))
        self.battleship.placeBoat(3, Coord(5, 4), Direction(Direction.DOWN))
        self.battleship.placeBoat(4, Coord(2, 1), Direction(Direction.RIGHT))
        self.battleship.nextPlayer()

    def initUI(self):
        self.setGeometry(100, 100, 1200, 700)
        self.setWindowTitle('Battleship')
        self.show()

    def mousePressEvent(self, e):
        x, y = e.x(), e.y()
        coord = self.getSquareCoord(x, y)
        if coord.board == 1:
            result = self.battleship.shoot(coord)
            self.update()
            if result == Board.SHOT_MISSED:
                self.battleship.nextPlayer()
                self.battleship.botTurn()
                self.battleship.nextPlayer()

    def paintEvent(self, e):
        x1, y1, x2, y2, squareSize = self.getBoardCoords()
        qp = BattleshipPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.drawGrid(x1, y1, squareSize)
        qp.drawGrid(x2, y2, squareSize)
        qp.drawBoats(self.getPlayerBoatsRect())
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

    def getBoardCoords(self):
        width = self.width()
        height = self.height()
        marginX = 0.08 * width
        boardSize = 0.38 * width
        marginY = (height - boardSize) * 0.8
        return marginX, marginY, width - marginX - boardSize, marginY, boardSize / 10


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = BattleshipWidget()
    sys.exit(app.exec_())
