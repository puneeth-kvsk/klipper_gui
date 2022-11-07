

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

        self.page_3 = QWidget()

        self.page_3.setObjectName(u"page_3")

        self.frame = QFrame(self.page_3)

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

        self.pushButton = QPushButton(self.verticalLayoutWidget)

        self.pushButton.setObjectName(u"pushButton")

        self.pushButton.setFlat(False)



        self.verticalLayout.addWidget(self.pushButton)



        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)

        self.pushButton_2.setObjectName(u"pushButton_2")



        self.verticalLayout.addWidget(self.pushButton_2)



        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)

        self.pushButton_5.setObjectName(u"pushButton_5")



        self.verticalLayout.addWidget(self.pushButton_5)



        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)

        self.pushButton_4.setObjectName(u"pushButton_4")



        self.verticalLayout.addWidget(self.pushButton_4)



        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)

        self.pushButton_3.setObjectName(u"pushButton_3")



        self.verticalLayout.addWidget(self.pushButton_3)



        self.stackedWidget.addWidget(self.page_3)

        self.TakeSection = QWidget()

        self.TakeSection.setObjectName(u"TakeSection")

        self.textEdit = QTextEdit(self.TakeSection)

        self.textEdit.setObjectName(u"textEdit")

        self.textEdit.setGeometry(QRect(460, 50, 201, 41))

        self.textEdit_2 = QTextEdit(self.TakeSection)

        self.textEdit_2.setObjectName(u"textEdit_2")

        self.textEdit_2.setGeometry(QRect(460, 100, 201, 41))

        self.label = QLabel(self.TakeSection)

        self.label.setObjectName(u"label")

        self.label.setGeometry(QRect(320, 20, 101, 17))

        self.label_2 = QLabel(self.TakeSection)

        self.label_2.setObjectName(u"label_2")

        self.label_2.setGeometry(QRect(220, 60, 67, 17))

        self.label_3 = QLabel(self.TakeSection)

        self.label_3.setObjectName(u"label_3")

        self.label_3.setGeometry(QRect(220, 110, 67, 17))

        self.pushButton_6 = QPushButton(self.TakeSection)

        self.pushButton_6.setObjectName(u"pushButton_6")

        self.pushButton_6.setGeometry(QRect(500, 180, 89, 25))

        self.stackedWidget.addWidget(self.TakeSection)

        self.page_4 = QWidget()

        self.page_4.setObjectName(u"page_4")

        self.label_4 = QLabel(self.page_4)

        self.label_4.setObjectName(u"label_4")

        self.label_4.setGeometry(QRect(310, 10, 67, 17))

        self.stackedWidget.addWidget(self.page_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)

        self.menubar.setObjectName(u"menubar")

        self.menubar.setGeometry(QRect(0, 0, 758, 22))

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)

        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)



        self.stackedWidget.setCurrentIndex(0)





        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi



    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Take Section ", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"teardown phase 1", None))

        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"teardown Phase 2 ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Final Process ", None))

        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"DisCard Tissue ", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Take Section ", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Thickness ", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Count", None))

        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Back ", None))

        self.label_4.setText("")

    # retranslateUi