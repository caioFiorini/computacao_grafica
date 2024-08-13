import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.layout = QtWidgets.QHBoxLayout()

        self.sidebar_layout = QtWidgets.QVBoxLayout()
        
        self.button = QtWidgets.QPushButton("Click me!")
        self.button.setFixedSize(100,20)
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.paint_widget = QtWidgets.QVBoxLayout()
        self.paint_widget.addWidget(self.text)
        
        self.sidebar_layout.addWidget(self.button)
        
        self.button.clicked.connect(self.magic)
        
        self.layout.addLayout(self.paint_widget)
        self.layout.addLayout(self.sidebar_layout)
        
        self.sidebar_layout.setStyleSheet("background-color: lightblue;")
        
        self.setLayout(self.layout)
        self.show()

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)

    sys.exit(app.exec())