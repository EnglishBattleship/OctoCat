# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
import numpy as np

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
        
        self.setGeometry(100, 100, 1100, 700)
        self.setWindowTitle('Event object')
        self.show()
        
        
    def mousePressEvent(self,e):
        self.coords=[e.x(),e.y(),e.button()]
        self.choice()
        
        
    def choice(self):
        if (100 < self.coords[0] < 400) and (100 < self.coords[1] < 600):
            if (100 < self.coords[0] < 350) and (150 < self.coords[1] < 200):
                boat = 'Carrier (5)'
            elif (100 < self.coords[0] < 300) and (250 < self.coords[1] < 300):
                    boat = 'Battleship (4)'              
            elif (100 < self.coords[0] < 250) and (350 < self.coords[1] < 400):
                boat = 'Cruiser (3)'
            elif (100 < self.coords[0] < 250) and (450 < self.coords[1] < 500):
                boat = 'Submarine (3)'
            elif (100 < self.coords[0] < 200) and (550 < self.coords[1] < 600):
                boat = 'Destroyer (2)'
            else:
                boat = False
            if boat:
                print('You select the',boat)
            else:
                print('You do not have select any boat')
        if (500 < self.coords[0] < 1000) and (100 < self.coords[1] < 600):
            letters = ['A','B','C','D','E','F','G','H','I','J']
            square = letters[int((self.coords[0]-500)/50)]+str(int((self.coords[1]-100)/50)+1)
            print('Your are in',square)
    
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())