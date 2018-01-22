from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QFont, QBrush


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

    def drawBoats(self, boatsRect):
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
        self.setBrush(QBrush(Qt.red))
        self.drawCircle(rect)