import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        widget2 = QListWidget()
        widget2.addItems(["Loja", "Quito", "Guayaquil"])

        widget2.currentItemChanged.connect(self.index_changed)
        widget2.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget2)


    def index_changed(self, i):
        print(i.text())

    def text_changed(self, s):
        print(s)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
