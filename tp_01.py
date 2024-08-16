import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # layout principal
        self.layout = QtWidgets.QHBoxLayout(self)

        # setando os botões
        self.button = QtWidgets.QPushButton("Click me!")
        self.button.setFixedSize(100,20)
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        
        #futuro layout do paint
        self.paint_widget = QtWidgets.QVBoxLayout()
        self.paint_widget.addWidget(self.text)
        
        # bara lateral
        self.sidebar_widget = QtWidgets.QWidget()
        self.sidebar_widget.setFixedWidth(200)
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar_widget)
        self.sidebar_layout.addWidget(self.button)
        
        #função de evento do click
        self.button.clicked.connect(self.magic)
        
        # Junção dos layouts em 1 só
        self.layout.addLayout(self.paint_widget)
        self.layout.addWidget(self.sidebar_widget)
        
        # style sheet
        self.sidebar_widget.setStyleSheet("background-color: lightblue;")
        
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