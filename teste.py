import sys
from PySide6 import QtWidgets, QtGui, QtCore

class TransformWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(600, 600)
        self.translation_x = 0
        self.translation_y = 0
        self.rotation_angle = 0
        self.scale_factor = 1
        self.reflect_x = False
        self.reflect_y = False

        self.initUI()

    def initUI(self):
        layout = QtWidgets.QVBoxLayout()

        # Slider para translação no eixo X
        self.slider_translation_x = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_translation_x.setRange(-200, 200)
        self.slider_translation_x.valueChanged.connect(self.update_translation_x)
        layout.addWidget(QtWidgets.QLabel("Translação X"))
        layout.addWidget(self.slider_translation_x)

        # Slider para translação no eixo Y
        self.slider_translation_y = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_translation_y.setRange(-200, 200)
        self.slider_translation_y.valueChanged.connect(self.update_translation_y)
        layout.addWidget(QtWidgets.QLabel("Translação Y"))
        layout.addWidget(self.slider_translation_y)

        # Slider para rotação
        self.slider_rotation = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_rotation.setRange(0, 360)
        self.slider_rotation.valueChanged.connect(self.update_rotation)
        layout.addWidget(QtWidgets.QLabel("Rotação"))
        layout.addWidget(self.slider_rotation)

        # Slider para escala
        self.slider_scale = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider_scale.setRange(1, 200)  # Escala de 1% a 200%
        self.slider_scale.setValue(100)  # Valor inicial em 100% (sem escala)
        self.slider_scale.valueChanged.connect(self.update_scale)
        layout.addWidget(QtWidgets.QLabel("Escala (%)"))
        layout.addWidget(self.slider_scale)

        # Checkbox para reflexão no eixo X
        self.checkbox_reflect_x = QtWidgets.QCheckBox("Reflexão X")
        self.checkbox_reflect_x.stateChanged.connect(self.update_reflect_x)
        layout.addWidget(self.checkbox_reflect_x)

        # Checkbox para reflexão no eixo Y
        self.checkbox_reflect_y = QtWidgets.QCheckBox("Reflexão Y")
        self.checkbox_reflect_y.stateChanged.connect(self.update_reflect_y)
        layout.addWidget(self.checkbox_reflect_y)

        # Set layout
        container = QtWidgets.QWidget(self)
        container.setLayout(layout)
        container.move(0, 0)

    def update_translation_x(self, value):
        self.translation_x = value
        self.update()

    def update_translation_y(self, value):
        self.translation_y = value
        self.update()

    def update_rotation(self, value):
        self.rotation_angle = value
        self.update()

    def update_scale(self, value):
        self.scale_factor = value / 100.0  # Converter para fator de escala
        self.update()

    def update_reflect_x(self, state):
        self.reflect_x = (state == QtCore.Qt.Checked)
        self.update()

    def update_reflect_y(self, state):
        self.reflect_y = (state == QtCore.Qt.Checked)
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        # Mover a origem do desenho para o centro da tela
        painter.translate(self.width() / 2, self.height() / 2)

        # Aplicar translações, rotações, escalas e reflexões
        painter.translate(self.translation_x, self.translation_y)
        painter.rotate(self.rotation_angle)
        if self.reflect_x or self.reflect_y:
            scale_x = -1 if self.reflect_x else 1
            scale_y = -1 if self.reflect_y else 1
            painter.scale(scale_x * self.scale_factor, scale_y * self.scale_factor)
        else:
            painter.scale(self.scale_factor, self.scale_factor)

        # Desenhar o quadrado
        rect = QtCore.QRectF(-50, -50, 100, 100)
        painter.setBrush(QtCore.Qt.blue)
        painter.drawRect(rect)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TransformWidget()
    window.show()
    sys.exit(app.exec())
