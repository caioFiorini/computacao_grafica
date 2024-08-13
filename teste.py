import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal horizontal
        main_layout = QHBoxLayout()

        # Widget central (pode ser qualquer widget, aqui usarei um QLabel como exemplo)
        central_widget = QLabel('Central Widget')
        central_widget.setStyleSheet("background-color: lightgray;")
        central_widget.setMinimumSize(300, 300)  # Definindo um tamanho mínimo para o widget central

        # Layout vertical para a barra de configurações na lateral
        sidebar_layout = QVBoxLayout()
        
        # Exemplo de botões de configuração na barra lateral
        config_button1 = QPushButton('Config 1')
        config_button2 = QPushButton('Config 2')
        config_button3 = QPushButton('Config 3')

        # Adicionando os botões ao layout da barra lateral
        sidebar_layout.addWidget(config_button1)
        sidebar_layout.addWidget(config_button2)
        sidebar_layout.addWidget(config_button3)
        sidebar_layout.addStretch()  # Adiciona um espaço flexível para empurrar os botões para o topo

        # Adicionando o widget central e a barra lateral ao layout principal
        main_layout.addWidget(central_widget)
        main_layout.addLayout(sidebar_layout)

        # Define o layout principal na janela
        self.setLayout(main_layout)
        self.setWindowTitle('Central Widget with Sidebar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
