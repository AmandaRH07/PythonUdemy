"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para
criação de aplicações GUI (Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação de rede,
etc...
pip install pyqt5
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

class App(QMainWindow):
    def __init(self, parent=None):
        super().__init__(parent)


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()