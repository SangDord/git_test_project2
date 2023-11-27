import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainwindow import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.flag = False
        self.pushBtn.clicked.connect(self.is_draw)

    def is_draw(self):
        self.flag = True
        self.update()
        
    def draw_circle(self):
        rad = randint(20, 100)
        pen = self.qp.pen()
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.qp.setPen(pen)
        self.qp.drawEllipse(randint(0, 500 - 2 * rad), randint(0, 600 - 2 * rad), rad, rad)
        
    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_circle()
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
