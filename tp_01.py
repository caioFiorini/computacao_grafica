import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

from PySide6 import QtWidgets, QtGui, QtCore
import sys

class DrawingWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)
        self.drawing = False
        self.last_point = QtCore.QPoint()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.drawing:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = False

    def paintEvent(self,event):
        canvas_painter = QtGui.QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())
    
    def clearEvent(self,event):
        # Limpa o conteúdo da tela
        self.image.fill(QtCore.Qt.white)
        self.update()
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # layout principal
        self.layout = QtWidgets.QHBoxLayout(self)

        # Drawing_widget

        self.drawing_widget = DrawingWidget()

        # setando os botões
        self.button = QtWidgets.QPushButton("Clear", self)
        self.button.setFixedSize(100,20)
        self.button.clicked.connect(self.drawing_widget.clearEvent)
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        
        #futuro layout do paint
        self.paint_widget = QtWidgets.QVBoxLayout()
        self.paint_widget.addWidget(self.drawing_widget)
        
        # bara lateral
        self.sidebar_widget = QtWidgets.QWidget()
        self.sidebar_widget.setFixedWidth(200)
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar_widget)
        self.sidebar_layout.addWidget(self.button)
        
        #função de evento do click
        # self.button.clicked.connect(self.magic)
        
        # Junção dos layouts em 1 só
        self.layout.addLayout(self.paint_widget)
        self.layout.addWidget(self.sidebar_widget)
        
        # style sheet
        self.sidebar_widget.setStyleSheet("background-color: lightblue;")
        
        self.setLayout(self.layout)
        self.show()

    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)

    sys.exit(app.exec())