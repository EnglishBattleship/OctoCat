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
        
        x = 0
        y = 0
        butt='click'
        
        self.text = "x: {1},  y: {0}".format(x, y)

        self.text2=butt
        
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.cliclabel= QLabel(self.text2, self)
        grid.addWidget(self.cliclabel,30,30,Qt.AlignTop)
        

        self.setMouseTracking(True)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()
        
        
    def mouseMoveEvent(self, e):
        
        x = e.x()
        y = e.y()
        
        text = "x: {1},  y: {0}".format(x, y)
        self.label.setText(text)

    def mousePressEvent(self,e):
        butt=e

    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())