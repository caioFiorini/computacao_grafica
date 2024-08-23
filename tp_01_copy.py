import sys
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui

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

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = True
            self.last_point = event.position()
        elif event.button() == QtCore.Qt.RightButton:
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

    def mouseMoveEvent(self, event):
        self.drawing = True
        if (event.buttons() & QtCore.Qt.LeftButton) and self.drawing:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            painter.drawLine(self.last_point, event.position())
            self.last_point = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drawing = False

    def paintEvent(self,event):
        canvas_painter = QtGui.QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())
    
    def clearEvent(self):
        # Limpa o conteúdo da tela
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
        x_incr = dx/passos
        y_incr = dy/passos
        x = x1 
        y = y1
        # Drawpoint substitui o set_pixel
        painter.drawPoint(round(x), round(y))
        for i in range(int(passos)):
            x = x + x_incr
            y = y + y_incr
            painter.drawPoint(round(x), round(y))

    def abs(self, num):
        if num < 0 :
            num = num * -1
        return num    


class MyWidget(QtWidgets.QWidget):

        
    
    def toggle_algorithm(self, checked):
        if checked : 
            self.toggle_button.setText("DDA")
        else:
            self.toggle_button.setText("DDA")
    
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
        
        #setando o toggle_button
        
        self.toggle_button = QtWidgets.QPushButton("DDA")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.toggle_algorithm)
        
        #futuro layout do paint
        self.paint_widget = QtWidgets.QVBoxLayout()
        self.paint_widget.addWidget(self.drawing_widget)
        
        # bara lateral
        self.sidebar_widget = QtWidgets.QWidget()
        self.sidebar_widget.setFixedWidth(200)
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar_widget)
        self.sidebar_layout.addWidget(self.button)
        self.sidebar_layout.addWidget(self.toggle_button)
        
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
    
# void alg_bresenham (intx1,y1,x2,y2){
#     int dx, dy, x, y, const1,
#     const2, p;
#     dx = abs (x2-x1);
#     dy = abs (y2-y1);
#     p = 2*dy – dx;
#     const1 = 2*dy;
#     const2 = 2*(dy-dx);
#     x = x1; y = y1;
#     colora_pixel (x,y);
#     while (x < x2) {
#         x = x + 1;
#         if (p < 0)
#             p += const1;
#         else {
#             p+= const2; y++;
#         }
#         colora_pixel (x,y);
#     }
# }
