import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def window():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.setGeometry(200, 200, 320, 200)
    widget.setWindowTitle("Microtome")

    button1 = QPushButton(widget)
    button1.setText("Take Sections")
    button1.move(1, 32)
    button1.clicked.connect(take_sections_button)

    button2 = QPushButton(widget)
    button2.setText("Teardown Phase 1")
    button2.move(1, 64)
    button2.clicked.connect(teardown_phase_one)

    button2 = QPushButton(widget)
    button2.setText("Teardown Phase 2")
    button2.move(1, 96)
    button2.clicked.connect(teardown_phase_two)

    button2 = QPushButton(widget)
    button2.setText("Final Process")
    button2.move(1, 128)
    button2.clicked.connect(final_process)

    button2 = QPushButton(widget)
    button2.setText("Discard tissue")
    button2.move(1, 160)
    button2.clicked.connect(discard_tissue)

    widget.show()
    sys.exit(app.exec_())


def take_sections_button():
    print("Take Section process")


def teardown_phase_one():
    print("Teardown process 1")


def teardown_phase_two():
    print("Teardown process 2")


def final_process():
    print("Final Process")


def discard_tissue():
    print("Discard Tissue")


if __name__ == '__main__':
    window()