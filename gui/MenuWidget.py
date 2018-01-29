import sys, os
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter, QFont
from PyQt5.QtCore import QRect


class MenuWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainWidget = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.mainTitle = QLabel("Battlesheeeeep")
        self.mainTitle.setAlignment(Qt.AlignCenter)
        self.mainTitle.setFont(QFont("Arial", pointSize=40))

        self.playButton = QPushButton("Jouer")
        self.playButton.clicked.connect(self.onPlayButtonClicked)

        self.quitButton = QPushButton("Quitter")
        self.quitButton.clicked.connect(sys.exit)

        layout.addWidget(self.mainTitle)
        layout.addWidget(self.playButton)
        layout.addWidget(self.quitButton)

    def onPlayButtonClicked(self):
        self.mainWidget.play()