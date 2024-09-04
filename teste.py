import sys
import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui

class DrawingWidget(QtWidgets.QWidget):
    
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

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
        
        while aceito != True:
            c1 = self.region_code(x1,y1)
            c2 = self.region_code(x2,y2)
            if (c1 == 0 and c2 == 0):
                aceito = True
                feito = True
            elif (c1 != 0  and c2 != 0):
                feito = True
            else:
                if(c1 != 0):
                    cfora = c1
                else: 
                    cfora = c2
                if (self.verificaBit(cfora, 0) == 1):
                    x_int = self.xmin
                    y_int = y1 + (y2-y1)*((self.x_min-x1)/(x2-x1))
                elif(self.verificaBit(cfora, 1) == 1):
                    x_int = self.x_max
                    y_int = y1 + (y2-y1)*((self.x_max-x1)/(x2-x1))
                elif(self.verificaBit(cfora, 2) == 1):
                    y_int = self.y_min
                    x_int = x1+(x2-x1)*((self.y_min-y1)/(y2-y1))
                elif(self.verificaBit(cfora, 3) == 1):
                    y_int = self.y_min
                    x_int = x1 + (x2-x1)*((self.y_max-y1)/(y2-y1))
                if(cfora == c1):
                    x1 = x_int
                    y1 = y_int
                else:
                    x2 = x_int
                    y2 = y_int
        if aceito:
            dda(round(x1), round(y1), round(x2), round(y2))
       
