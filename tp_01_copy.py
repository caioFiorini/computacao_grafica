import sys
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui
import math

class DrawingWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.setFixedSize(600, 600)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)
        self.drawing = False
        self.last_point = QtCore.QPoint()
        self.start_point = None
        self.ativa_dda = False
        self.ativa_bres = False
        self.ativa_bres_circ = False

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.last_point = event.position().toPoint()  # Converte para QPoint

        elif self.ativa_dda:  # Verifica se DDA está ativado
            if event.button() == QtCore.Qt.RightButton:
                if self.start_point is None:
                    self.x1 = event.position().x()
                    self.y1 = event.position().y()
                    self.start_point = (self.x1, self.y1)
                    self.drawing = True
                else:
                    self.x2 = event.position().x()
                    self.y2 = event.position().y()
                    self.DDA(self.x1, self.y1, self.x2, self.y2)
                    self.drawing = False
                    self.start_point = None
                    self.update()

        elif self.ativa_bres:  # Verifica se Bresenham está ativado
            if event.button() == QtCore.Qt.RightButton:
                if self.start_point is None:
                    self.x3 = event.position().x()
                    self.y3 = event.position().y()
                    self.start_point = (self.x3, self.y3)
                    self.drawing = True
                else:
                    self.x4 = event.position().x()
                    self.y4 = event.position().y()
                    self.alg_bresenham(self.x3, self.y3, self.x4, self.y4)
                    self.drawing = False
                    self.start_point = None
                    self.update()
        
        elif self.ativa_bres_circ:  # Verifica se Bresenham_circ está ativado
            if event.button() == QtCore.Qt.RightButton:
                if self.start_point is None:
                    self.x5 = event.position().x()
                    self.y5 = event.position().y()
                    self.start_point = (self.x5, self.y5)
                    self.drawing = True
                else:
                    self.x6 = event.position().x()
                    self.y6 = event.position().y()
                    raio = math.sqrt((self.x6 - self.x5) ** 2 + (self.y6 - self.y5) ** 2)
                    self.alg_Bresenham_circulo(self.x5, self.y5, raio)
                    self.drawing = False
                    self.start_point = None
                    self.update()

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.drawing:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            painter.drawLine(self.last_point, event.position().toPoint())
            self.last_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvas_painter = QtGui.QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    def clearEvent(self):
        self.image.fill(QtCore.Qt.white)
        self.update()

    def DDA(self, x1, y1, x2, y2):
        painter = QtGui.QPainter(self.image)
        pen = QtGui.QPen(QtGui.Qt.black, 2)
        painter.setPen(pen)
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) > abs(dy):
            passos = abs(dx)
        else:
            passos = abs(dy)
        x_incr = dx / passos
        y_incr = dy / passos
        x = x1
        y = y1
        painter.drawPoint(round(x), round(y))
        for i in range(int(passos)):
            x = x + x_incr
            y = y + y_incr
            painter.drawPoint(round(x), round(y))

    def alg_bresenham(self, x1, y1, x2, y2):
        painter = QtGui.QPainter(self.image)
        pen = QtGui.QPen(QtGui.Qt.black, 2)
        painter.setPen(pen)
        dx = x2 - x1
        dy = y2 - y1
        if (dx >= 0):
            incrx = 1
        else:
            incrx = -1
            dx = -dx
        if (dy >= 0):
            incry = 1
        else:
            incry = -1
            dy = -dy
        x = x1
        y = y1
        painter.drawPoint(x,y)
        if (dy < dx):
            p = 2*dy-dx
            const1 = 2*dy
            const2 =  2*(dy-dx)
            for i in range(int(dx)):
                x += incrx
                if (p<0):
                    p += const1
                else:
                    y += incry
                    p += const2
                painter.drawPoint(x, y)
        else:
            p = 2*dx-dy
            const1 = 2*dx
            const2 = 2*(dx-dy)
            for i in range(int(dy)):
                y += incry
                if (p<0):
                    p += const1
                else:
                    x += incrx
                    p += const2
                painter.drawPoint(x, y)
    
    def alg_Bresenham_circulo(self, xc, yc, raio):
        x = 0
        y = raio
        p= 3-2*raio
        self.plot_circule_points(xc, x, yc, y)
        while(x < y):
            if p < 0:
                p = p + 4*x+6
            else:
                p = p + 4*(x-y) + 10
                y = y-1
            x = x+1
            self.plot_circule_points(xc, x, yc, y)
    
    def plot_circule_points(self, xc, x, yc, y):
        painter = QtGui.QPainter(self.image)
        pen = QtGui.QPen(QtGui.Qt.black, 2)
        painter.setPen(pen)
        painter.drawPoint(xc+x, yc+y)
        painter.drawPoint(xc-x, yc+y)
        painter.drawPoint(xc+x, yc-y)
        painter.drawPoint(xc-x, yc-y)
        painter.drawPoint(xc+y, yc+x)
        painter.drawPoint(xc-y, yc+x)
        painter.drawPoint(xc+y, yc-x)
        painter.drawPoint(xc-y, yc-x)
class MyWidget(QtWidgets.QWidget):
    def toggle_algorithm(self, checked):
        if checked:
            self.drawing_widget.ativa_dda = True
            self.drawing_widget.ativa_bres = False  # Desativa Bresenham
            self.drawing_widget.ativa_bres_circ = False
            self.toggle_button.setText("DDA ON")
            self.toggle_button_bres.setChecked(False)  # Desmarca o botão de Bresenham
        else:
            self.drawing_widget.ativa_dda = False
            self.toggle_button.setText("DDA OFF")

    def toggle_algorithm_bres(self, checked):
        if checked:
            self.drawing_widget.ativa_bres = True
            self.drawing_widget.ativa_dda = False  # Desativa DDA
            self.drawing_widget.ativa_bres_circ = False
            self.toggle_button_bres.setText("Bresenham ON")
            self.toggle_button.setChecked(False)  # Desmarca o botão de DDA
        else:
            self.drawing_widget.ativa_bres = False
            self.toggle_button_bres.setText("Bresenham OFF")

    def toggle_algorithm_circ(self, checked):
        if checked:
            self.drawing_widget.ativa_bres_circ = True
            self.drawing_widget.ativa_bres = False
            self.drawing_widget.ativa_dda = False
            self.toggle_button_bres_circ.setText("Bresenham Circ ON")
            self.toggle_button.setChecked(False)
            self.toggle_button_bres.setChecked(False)
        else: 
            self.drawing_widget.ativa_bres_circ = False
            self.toggle_button_bres_circ.setText("Bresengam Circ OFF")

    def __init__(self):
        super().__init__()

        # Layout principal
        self.layout = QtWidgets.QHBoxLayout(self)

        # Drawing_widget
        self.drawing_widget = DrawingWidget()

        # Botões
        self.button = QtWidgets.QPushButton("Clear", self)
        self.button.setFixedSize(100, 20)
        self.button.clicked.connect(self.drawing_widget.clearEvent)

        # DDA
        self.toggle_button = QtWidgets.QPushButton("DDA")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.toggle_algorithm)

        # Bresenham
        self.toggle_button_bres = QtWidgets.QPushButton("Bresenham")
        self.toggle_button_bres.setCheckable(True)
        self.toggle_button_bres.toggled.connect(self.toggle_algorithm_bres)

        # Bresenham Circule

        self.toggle_button_bres_circ = QtWidgets.QPushButton("Bresenham Circule")
        self.toggle_button_bres_circ.setCheckable(True)
        self.toggle_button_bres_circ.toggled.connect(self.toggle_algorithm_circ)

        # Layout de desenho
        self.paint_widget = QtWidgets.QVBoxLayout()
        self.paint_widget.addWidget(self.drawing_widget)

        # Barra lateral
        self.sidebar_widget = QtWidgets.QWidget()
        self.sidebar_widget.setFixedWidth(200)
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar_widget)
        self.sidebar_layout.addWidget(self.button)
        self.sidebar_layout.addWidget(self.toggle_button)
        self.sidebar_layout.addWidget(self.toggle_button_bres)
        self.sidebar_layout.addWidget(self.toggle_button_bres_circ)

        # Junção dos layouts
        self.layout.addLayout(self.paint_widget)
        self.layout.addWidget(self.sidebar_widget)

        self.sidebar_widget.setStyleSheet("background-color: lightblue;")
        self.setLayout(self.layout)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)

    sys.exit(app.exec())
