import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel)


class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Take Sections")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Microtome"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton1 = QPushButton("Take Sections", self)
        self.pushButton1.move(1, 32)
        self.pushButton1.clicked.connect(self.window2)              # <===

        self.pushButton1 = QPushButton("Teardown phase one", self)
        self.pushButton1.move(1, 64)
        self.pushButton1.clicked.connect(teardown_phase_one)

        self.pushButton1 = QPushButton("Teardown phase two", self)
        self.pushButton1.move(1, 96)
        self.pushButton1.clicked.connect(teardown_phase_two)

        self.pushButton1 = QPushButton("Final Process", self)
        self.pushButton1.move(1, 128)
        self.pushButton1.clicked.connect(final_process)

        self.pushButton1 = QPushButton("Discard Tissue", self)
        self.pushButton1.move(1, 128)
        self.pushButton1.clicked.connect(discard_tissue)

        self.main_window()

    def main_window(self):
        self.label = QLabel("Manager", self)
        self.label.move(285, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window2(self):                                             # <===
        self.w = Window2()
        self.w.show()
        self.hide()

def take_sections_button():
    print("Take Section process")
    # Have to take input of THICKNESS and COUNTS
    thickness = input("Enter the thickness of tissue:")
    if thickness == '':
        print('Default thickness set to 3 micron')
        thickness = 0.003
    count = input("Enter number of tissues to cut:")
    api_calls_higher.take_sections(thickness, count)


def teardown_phase_one():
    print("Teardown process 1")
    api_calls_higher.teardown_phase_one()


def teardown_phase_two():
    print("Teardown process 2")
    api_calls_higher.teardown_phase_two()


def final_process():
    print("Final Process")
    api_calls_higher.final_process()


def discard_tissue():
    print("Discard Tissue")
    api_calls_higher.discard_tissue()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window()
    sys.exit(app.exec())
