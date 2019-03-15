import sys

from PyQt5 import QtWidgets

import controller
from ui.lab2_ui import Ui_MainWindow


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAdd_Image.triggered.connect(self.add_image)
        self.ui.actionAdd_Folder.triggered.connect(self.add_image_folder)

    def add_image(self):
        controller.add_image(self.ui)

    def add_image_folder(self):
        controller.add_image_folder(self.ui)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
