import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter, QPen

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        #grid = QGridLayout()
        #grid.setSpacing(10)
        
        self.coords=[0,0,0]        

        self.setMouseTracking(True)

        self.Carrier=QImage('C:\\Users\\selen\\Documents\\GitHub\\OctoCat\\gui\\Carrier_5.jpg')
        self.Battleship=QImage('C:\\Users\\selen\\Documents\\GitHub\\OctoCat\\gui\\Battleship_4.png')
        self.Cruiser=QImage('C:\\Users\\selen\\Documents\\GitHub\\OctoCat\\gui\\Cruiser_3.png')
        self.Submarine=QImage('C:\\Users\\selen\\Documents\\GitHub\\OctoCat\\gui\\Submarine_3.png')
        self.Destroyer=QImage('C:\\Users\\selen\\Documents\\GitHub\\OctoCat\\gui\\Destroyer_2.jpg')
        #self.setLayout(grid)
        
        self.setGeometry(100, 100, 1100,700)
        self.setWindowTitle('Battleship')
        #self.showShip()
        self.show()

        
    def mousePressEvent(self,e):
        self.coords=[e.x(),e.y(),e.button()]
        #emit?

    def getcoords(self):
        return(self.coords)

    def showShip(self):
        label =QLabel(self)
        pixmap = QPixmap(self.Submarine)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height()) 

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawGrid(qp,500,100,50)
        qp.end()

    def drawGrid(self,qp,xOffset,yOffset, sqSize):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        qp.setPen(pen)
        for i in range(11):
            qp.drawLine(xOffset+i*sqSize, yOffset,xOffset+i*sqSize , yOffset+10*sqSize)
        for j in range(11):
            qp.drawLine(xOffset, yOffset+j*sqSize,xOffset+10*sqSize , yOffset+j*sqSize)
        
        for k in range(10):
            qp.drawText()


    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())