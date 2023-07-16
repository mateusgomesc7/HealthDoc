import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

# Subclasse da classe QMainWindow para criar a janela principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo PySide6")

        # Cria um QLabel e define o texto
        label = QLabel("Olá, PySide6!", self)
        label.setAlignment(Qt.AlignCenter)

        # Define o QLabel como o widget central da janela
        self.setCentralWidget(label)


if __name__ == "__main__":
    # Cria a instância do aplicativo QApplication
    app = QApplication(sys.argv)

    # Cria a instância da janela principal
    window = MainWindow()
    window.show()

    # Executa o loop de eventos do aplicativo
    sys.exit(app.exec())
