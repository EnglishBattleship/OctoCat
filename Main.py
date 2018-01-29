import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtGui import QFont

from gui.MenuWidget import MenuWidget
from gui.BattleshipWidget import BattleshipWidget


class MainWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(500, 200, 600, 500)
        self.menuWidget = MenuWidget(self)
        self.battleshipWidget = BattleshipWidget(self)

        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.menuWidget)
        self.stackedWidget.addWidget(self.battleshipWidget)
        self.stackedWidget.setCurrentWidget(self.menuWidget)
        layout.addWidget(self.stackedWidget)

    def play(self):
        self.stackedWidget.setCurrentWidget(self.battleshipWidget)
        self.setGeometry(100, 100, 1200, 700)
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())
