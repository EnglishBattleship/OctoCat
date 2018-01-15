import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        #grid = QGridLayout()
        #grid.setSpacing(10)
        
        self.coords=[0,0,0]        

        self.setMouseTracking(True)
        
        #self.setLayout(grid)
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Battleship')
        self.showShip()
        self.show()

        
    def mousePressEvent(self,e):
        self.coords=[e.x(),e.y(),e.button()]
        #emit?

    def getcoords(self):
        return(self.coords)

    def showShip(self):
        label =QLabel(self)
        pixmap = QPixmap('Submarine_3.png')
        label.setPixmap(pixmap)
        #self.resize(pixmap.width(),pixmap.height()) 
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())