import sys
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui

class DrawingWidget(QtWidgets.QWidget):
    
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    def verifica_bit(self, num_1, num_2):
        return (num_1 & (1 << num_2)) != 0

    def region_code(self, x,y):
        codigo = 0
        if(x < self.x_min):
            codigo = codigo+1
        elif (x > self.x_max):
            codigo = codigo+2
        elif (y < self.y_min):
            codigo = codigo+4
        elif (y > self.y_max):
            codigo = codigo+8
        return codigo


    def cohen_sutherland_clip(self, x1, y1, x2, y2):
        aceito = False
        feito = False
        while True:
            c1 = self.region_code(x1,y1)
            c2 = self.region_code(x2,y2)
            if (c1 == 0 and c2 == 0):
                aceito = True
                feito = True
            elif (c1 & c2) != 0:
                feito = True
            else:
                if(c1 != 0):
                    cfora = c1
                else: 
                    cfora = c2
                if self.verifica_bit(cfora, 0):
                    x_int = self.x_min
                    y_int = y1 + (y2-y1)*((self.x_min-x1)/(x2-x1))
                elif self.verifica_bit(cfora, 1):
                    x_int = self.x_max
                    y_int = y1 + (y2-y1)*((self.x_max-x1)/(x2-x1))
                elif self.verifica_bit(cfora, 2):
                    y_int = self.y_min
                    x_int = x1+(x2-x1)*((self.y_min-y1)/(y2-y1))
                elif self.verifica_bit(cfora, 3):
                    y_int = self.y_max
                    x_int = x1 + (x2-x1)*((self.y_max-y1)/(y2-y1))
                if(cfora == c1):
                    x1 = x_int
                    y1 = y_int
                else:
                    x2 = x_int
                    y2 = y_int
        
        if aceito:
            dda(round(x1), round(y1), round(x2), round(y2))

    def __init__(self):
        super().__init__()
        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.setFixedSize(600, 600)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)
        self.image.fill(QtCore.Qt.white)
        self.start_point = None
        self.end_point = None
        self.drawing_rectangle = False

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if not self.drawing_rectangle:
                # Primeiro clique - define o ponto inicial
                self.start_point = event.position().toPoint()
                self.drawing_rectangle = True
            else:
                # Segundo clique - define o ponto final e desenha o retângulo
                self.end_point = event.position().toPoint()
                self.drawing_rectangle = False
                self.draw_rectangle(self.start_point, self.end_point)
                self.update()

    def draw_rectangle(self, start_point, end_point):
        painter = QtGui.QPainter(self.image)
        pen = QtGui.QPen(QtCore.Qt.black, 2)
        painter.setPen(pen)
        
        rect = QtCore.QRect(start_point, end_point)
        painter.drawRect(rect)

    def paintEvent(self, event):
        canvas_painter = QtGui.QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DrawingWidget()
    window.show()
    sys.exit(app.exec())
       
