import sys

from io import StringIO
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt



class DoComb(QMainWindow):
    def __init__(self):
        super().__init__()
        f = StringIO(template)
        uic.loadUi(f, self)
        self.start_check.clicked.connect(self.start_comb)

    def create_circle(self):
        print('мне лень делать круг')
       


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DoComb()
    ex.show()
    sys.exit(app.exec())
