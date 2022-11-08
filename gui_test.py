from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import api_calls_higher

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(758, 339)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 751, 291))
        self.Main_Page = QWidget()
        self.Main_Page.setObjectName(u"Main_Page")
        self.frame = QFrame(self.Main_Page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 741, 291))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 241, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.takeSection = QPushButton(self.verticalLayoutWidget)
        self.takeSection.setObjectName(u"takeSection")
        self.takeSection.setFlat(False)

        self.verticalLayout.addWidget(self.takeSection)

        self.teardownPhaseOne = QPushButton(self.verticalLayoutWidget)
        self.teardownPhaseOne.setObjectName(u"teardownPhaseOne")

        self.verticalLayout.addWidget(self.teardownPhaseOne)

        self.teardownPhaseTwo = QPushButton(self.verticalLayoutWidget)
        self.teardownPhaseTwo.setObjectName(u"teardownPhaseTwo")

        self.verticalLayout.addWidget(self.teardownPhaseTwo)

        self.finalProcess = QPushButton(self.verticalLayoutWidget)
        self.finalProcess.setObjectName(u"finalProcess")

        self.verticalLayout.addWidget(self.finalProcess)

        self.discardTissue = QPushButton(self.verticalLayoutWidget)
        self.discardTissue.setObjectName(u"discardTissue")

        self.verticalLayout.addWidget(self.discardTissue)

        self.stackedWidget.addWidget(self.Main_Page)
        self.TakeSection = QWidget()
        self.TakeSection.setObjectName(u"TakeSection")
        self.thicknessInput = QTextEdit(self.TakeSection)
        self.thicknessInput.setObjectName(u"thicknessInput")
        self.thicknessInput.setGeometry(QRect(460, 50, 201, 41))
        self.countInput = QTextEdit(self.TakeSection)
        self.countInput.setObjectName(u"countInput")
        self.countInput.setGeometry(QRect(460, 100, 201, 41))
        self.takeSectionLabel = QLabel(self.TakeSection)
        self.takeSectionLabel.setObjectName(u"takeSectionLabel")
        self.takeSectionLabel.setGeometry(QRect(320, 20, 101, 17))
        self.label_2 = QLabel(self.TakeSection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 60, 67, 17))
        self.label_3 = QLabel(self.TakeSection)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 110, 67, 17))
        self.backButton = QPushButton(self.TakeSection)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(570, 170, 89, 25))
        self.saveButton = QPushButton(self.TakeSection)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(470, 170, 89, 25))
        self.saveButton.setStyleSheet(u"\n""background-color: rgb(143, 240, 164);")
        self.stackedWidget.addWidget(self.TakeSection)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 10, 67, 17))
        self.stackedWidget.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 758, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.takeSection.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1)) 
        self.backButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0)) 
        self.saveButton.clicked.connect(self.thickness_and_count_output)

    def thickness_and_count_output(self):
        thickness = int(str(self.thicknessInput.toPlainText()))
        count = int(str(self.countInput.toPlainText()))
        api_calls_higher.test_function(thickness, count)
        #print(int(str(self.thicknessInput.toPlainText())))
        #print(int(str(self.countInput.toPlainText())))
        self.thicknessInput.clear()
        self.countInput.clear()
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.takeSection.setText(QCoreApplication.translate("MainWindow", u"Take Section ", None))
        self.teardownPhaseOne.setText(QCoreApplication.translate("MainWindow", u"Teardown phase one", None))
        self.teardownPhaseTwo.setText(QCoreApplication.translate("MainWindow", u"Teardown phase two", None))
        self.finalProcess.setText(QCoreApplication.translate("MainWindow", u"Final Process ", None))
        self.discardTissue.setText(QCoreApplication.translate("MainWindow", u"Discard Tissue ", None))
        self.takeSectionLabel.setText(QCoreApplication.translate("MainWindow", u"Take Section ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Thickness ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back ", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_4.setText("")
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

