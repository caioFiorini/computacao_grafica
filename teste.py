from PySide6 import QtWidgets, QtCore

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # Layout principal horizontal
        self.layout = QtWidgets.QHBoxLayout(self)

        # Widget central
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self.paint_widget = QtWidgets.QVBoxLayout()
        self.paint_widget.addWidget(self.text)

        # Barra lateral (sidebar)
        self.sidebar_widget = QtWidgets.QWidget()  # Widget contêiner para a barra lateral
        self.sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar_widget)

        self.button = QtWidgets.QPushButton("Click me!")
        self.button.setFixedSize(100, 20)

        # Adiciona o botão à barra lateral
        self.sidebar_layout.addWidget(self.button)

        # Conecta o clique do botão a uma função
        self.button.clicked.connect(self.magic)

        # Adiciona o widget central e a barra lateral ao layout principal
        self.layout.addLayout(self.paint_widget)
        self.layout.addWidget(self.sidebar_widget)

        # Define a cor de fundo da barra lateral
        self.sidebar_widget.setStyleSheet("background-color: lightblue;")

        # Exibe a janela
        self.setWindowTitle("My Widget")
        self.show()

    def magic(self):
        self.text.setText(self.hello[0])  # Exemplo simples de ação ao clicar no botão

if __name__ == "__main__":
    app = QtWidgets.QApplication([])  # Inicializa a aplicação
    widget = MyWidget()  # Cria a instância da classe MyWidget
    app.exec()  # Executa o loop de eventos
