from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QFont, QBrush, QTransform, QColor
from Battleship.Direction import Direction


class BattleshipPainter(QPainter):

    def __init__(self):
        super().__init__()

    def drawGrid(self, xOffset, yOffset, sqSize):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        self.setPen(pen)
        for i in range(11):
            self.drawLine(xOffset + i * sqSize, yOffset, xOffset + i * sqSize, yOffset + 10 * sqSize)
        for j in range(11):
            self.drawLine(xOffset, yOffset + j * sqSize, xOffset + 10 * sqSize, yOffset + j * sqSize)

        self.setFont(QFont('Arial', pointSize=16))
        for k in range(1, 11):
            self.drawText(xOffset + (k - 0.5 - 0.1 * len(str(k))) * sqSize, yOffset - 0.1 * sqSize, str(k))
            self.drawText(xOffset - 0.5 * sqSize, yOffset + (k - 0.35) * sqSize, chr(64 + k))

    def drawBoats(self, boats, boatImages, x1, y1, x2, y2, squareSize):
        self.setPen(QPen())
        self.setBrush(QBrush(Qt.blue))
        for boat in boats.values():
            coord = boat.getCoords()[0]
            direction = [abs(x) for x in boat.direction.getDirection()]
            image = boatImages[boat.length - 1]
            if boat.direction.direction in [Direction.UP, Direction.DOWN]:
                rm = QTransform()
                rm.rotate(-90)
                image = image.transformed(rm)
            image = image.scaled((1 - direction[1]) * squareSize + direction[1] * squareSize * boat.length,
                                 (1 - direction[0]) * squareSize + direction[0] * squareSize * boat.length)
            self.drawImage(x1 + coord.y * squareSize, y1 + coord.x * squareSize, image)

    def drawBoatsWithRect(self, boatsRect, boatImages):
        self.setPen(QPen())
        self.setBrush(QBrush(Qt.blue))
        for rect in boatsRect:
            self.drawRect(rect)

    def drawMissedShot(self, rect):
        self.setPen(QPen())
        self.setBrush(QBrush(Qt.blue))
        self.drawCircle(rect)

    def drawCircle(self, rect):
        delta = rect.width() * 0.3
        rect.adjust(delta, delta, -delta, -delta)
        self.drawEllipse(rect)

    def drawHitShot(self, rect):
        self.setPen(QPen())
        color = QColor(Qt.red)
        color.setAlpha(180)
        brush = QBrush(color)
        self.setBrush(brush)
        self.drawRect(rect)