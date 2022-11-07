from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 781, 571))
        self.stackedWidget.setObjectName("stackedWidget")
        self.PageOne = QtWidgets.QWidget()
        self.PageOne.setObjectName("PageOne")
        self.ClickMe = QtWidgets.QPushButton(self.PageOne)
        self.ClickMe.setGeometry(QtCore.QRect(340, 270, 75, 23))
        self.ClickMe.setObjectName("ClickMe")
        self.stackedWidget.addWidget(self.PageOne)
        self.PageTwo = QtWidgets.QWidget()
        self.PageTwo.setObjectName("PageTwo")
        self.label = QtWidgets.QLabel(self.PageTwo)
        self.label.setGeometry(QtCore.QRect(360, 280, 47, 13))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.PageTwo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ClickMe.setText(_translate("MainWindow", "Click me!"))
        self.label.setText(_translate("MainWindow", "Hello!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())