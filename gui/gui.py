import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        self.coords=[0,0,0]        

        self.setMouseTracking(True)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()
        
        
    def mousePressEvent(self,e):
        self.coords=[e.x(),e.y(),e.button()]
        #emit?

    def getcoords(self):
        return(self.coords)
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())