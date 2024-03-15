import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)  # Устанавливаем размеры окна
        self.setWindowTitle("Моя форма")

        exit_button = QPushButton("Выход", self)
        exit_button.setGeometry(50, 200, 100, 30)  # Устанавливаем размеры кнопки
        exit_button.clicked.connect(self.close)  # При нажатии на кнопку вызываем метод close

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
