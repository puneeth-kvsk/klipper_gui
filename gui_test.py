from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import api_calls_higher
import api_calls_lower

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(868, 589)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(40, 10, 771, 501))
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
        self.take_section_button = QPushButton(self.verticalLayoutWidget)
        self.take_section_button.setObjectName(u"take_section_button")
        self.take_section_button.setFlat(False)

        self.verticalLayout.addWidget(self.take_section_button)

        self.first_tissue_pickup_button = QPushButton(self.verticalLayoutWidget)
        self.first_tissue_pickup_button.setObjectName(u"first_tissue_pickup_button")

        self.verticalLayout.addWidget(self.first_tissue_pickup_button)

        self.second_tissue_pickup_button = QPushButton(self.verticalLayoutWidget)
        self.second_tissue_pickup_button.setObjectName(u"second_tissue_pickup_button")

        self.verticalLayout.addWidget(self.second_tissue_pickup_button)

        self.discard_tissue_button = QPushButton(self.verticalLayoutWidget)
        self.discard_tissue_button.setObjectName(u"discard_tissue_button")

        self.verticalLayout.addWidget(self.discard_tissue_button)

        self.api_calls_higher_label = QLabel(self.frame)
        self.api_calls_higher_label.setObjectName(u"api_calls_higher_label")
        self.api_calls_higher_label.setGeometry(QRect(330, 10, 131, 61))
        self.verticalLayoutWidget_9 = QWidget(self.frame)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(570, 200, 160, 80))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.go_to_api_calls_lower_button = QPushButton(self.verticalLayoutWidget_9)
        self.go_to_api_calls_lower_button.setObjectName(u"go_to_api_calls_lower_button")

        self.verticalLayout_9.addWidget(self.go_to_api_calls_lower_button)

        self.stackedWidget.addWidget(self.Main_Page)
        self.TakeSection = QWidget()
        self.TakeSection.setObjectName(u"TakeSection")
        self.thickness_input = QTextEdit(self.TakeSection)
        self.thickness_input.setObjectName(u"thickness_input")
        self.thickness_input.setGeometry(QRect(460, 50, 201, 41))
        self.count_input = QTextEdit(self.TakeSection)
        self.count_input.setObjectName(u"count_input")
        self.count_input.setGeometry(QRect(460, 100, 201, 41))
        self.take_section_label = QLabel(self.TakeSection)
        self.take_section_label.setObjectName(u"take_section_label")
        self.take_section_label.setGeometry(QRect(320, 20, 101, 17))
        self.thickness_label = QLabel(self.TakeSection)
        self.thickness_label.setObjectName(u"thickness_label")
        self.thickness_label.setGeometry(QRect(220, 60, 67, 17))
        self.count_label = QLabel(self.TakeSection)
        self.count_label.setObjectName(u"count_label")
        self.count_label.setGeometry(QRect(220, 110, 67, 17))
        self.backButton1 = QPushButton(self.TakeSection)
        self.backButton1.setObjectName(u"backButton1")
        self.backButton1.setGeometry(QRect(570, 260, 89, 25))
        self.saveButton1 = QPushButton(self.TakeSection)
        self.saveButton1.setObjectName(u"saveButton1")
        self.saveButton1.setGeometry(QRect(430, 260, 89, 25))
        self.saveButton1.setStyleSheet(u"\n"
"background-color: rgb(143, 240, 164);")
        self.take_section_speed_label = QLabel(self.TakeSection)
        self.take_section_speed_label.setObjectName(u"take_section_speed_label")
        self.take_section_speed_label.setGeometry(QRect(220, 180, 67, 17))
        self.take_section_speed_input = QTextEdit(self.TakeSection)
        self.take_section_speed_input.setObjectName(u"take_section_speed_input")
        self.take_section_speed_input.setGeometry(QRect(460, 160, 201, 41))
        self.stackedWidget.addWidget(self.TakeSection)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 10, 67, 17))
        self.api_calls_lower = QLabel(self.page_4)
        self.api_calls_lower.setObjectName(u"api_calls_lower")
        self.api_calls_lower.setGeometry(QRect(320, 0, 131, 41))
        self.verticalLayoutWidget_3 = QWidget(self.page_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(490, 40, 263, 244))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.home_slide_gantry_button = QPushButton(self.verticalLayoutWidget_3)
        self.home_slide_gantry_button.setObjectName(u"home_slide_gantry_button")

        self.verticalLayout_3.addWidget(self.home_slide_gantry_button)

        self.move_slide_gantry_to_button = QPushButton(self.verticalLayoutWidget_3)
        self.move_slide_gantry_to_button.setObjectName(u"move_slide_gantry_to_button")

        self.verticalLayout_3.addWidget(self.move_slide_gantry_to_button)

        self.move_slide_to_first_pickup_position_button = QPushButton(self.verticalLayoutWidget_3)
        self.move_slide_to_first_pickup_position_button.setObjectName(u"move_slide_to_first_pickup_position_button")

        self.verticalLayout_3.addWidget(self.move_slide_to_first_pickup_position_button)

        self.move_slide_to_first_pivot_position_button = QPushButton(self.verticalLayoutWidget_3)
        self.move_slide_to_first_pivot_position_button.setObjectName(u"move_slide_to_first_pivot_position_button")

        self.verticalLayout_3.addWidget(self.move_slide_to_first_pivot_position_button)

        self.move_slide_to_first_final_position_button = QPushButton(self.verticalLayoutWidget_3)
        self.move_slide_to_first_final_position_button.setObjectName(u"move_slide_to_first_final_position_button")

        self.verticalLayout_3.addWidget(self.move_slide_to_first_final_position_button)

        self.move_slide_to_second_pickup_position_button = QPushButton(self.verticalLayoutWidget_3)
        self.move_slide_to_second_pickup_position_button.setObjectName(u"move_slide_to_second_pickup_position_button")

        self.verticalLayout_3.addWidget(self.move_slide_to_second_pickup_position_button)

        self.move_slide_to_second_pivot_position_button = QPushButton(self.verticalLayoutWidget_3)
        self.move_slide_to_second_pivot_position_button.setObjectName(u"move_slide_to_second_pivot_position_button")

        self.verticalLayout_3.addWidget(self.move_slide_to_second_pivot_position_button)

        self.move_slide_to_second_final_position_button = QPushButton(self.verticalLayoutWidget_3)
        self.move_slide_to_second_final_position_button.setObjectName(u"move_slide_to_second_final_position_button")

        self.verticalLayout_3.addWidget(self.move_slide_to_second_final_position_button)

        self.verticalLayoutWidget_5 = QWidget(self.page_4)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 150, 311, 244))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.home_wire_gantry_button = QPushButton(self.verticalLayoutWidget_5)
        self.home_wire_gantry_button.setObjectName(u"home_wire_gantry_button")

        self.verticalLayout_5.addWidget(self.home_wire_gantry_button)

        self.move_wire_gantry_to_button = QPushButton(self.verticalLayoutWidget_5)
        self.move_wire_gantry_to_button.setObjectName(u"move_wire_gantry_to_button")

        self.verticalLayout_5.addWidget(self.move_wire_gantry_to_button)

        self.move_wire_gantry_to_safe_pos_button = QPushButton(self.verticalLayoutWidget_5)
        self.move_wire_gantry_to_safe_pos_button.setObjectName(u"move_wire_gantry_to_safe_pos_button")

        self.verticalLayout_5.addWidget(self.move_wire_gantry_to_safe_pos_button)

        self.move_wire_gantry_to_dip_pos_button = QPushButton(self.verticalLayoutWidget_5)
        self.move_wire_gantry_to_dip_pos_button.setObjectName(u"move_wire_gantry_to_dip_pos_button")

        self.verticalLayout_5.addWidget(self.move_wire_gantry_to_dip_pos_button)

        self.move_wire_gantry_to_preteardown_pos_button = QPushButton(self.verticalLayoutWidget_5)
        self.move_wire_gantry_to_preteardown_pos_button.setObjectName(u"move_wire_gantry_to_preteardown_pos_button")

        self.verticalLayout_5.addWidget(self.move_wire_gantry_to_preteardown_pos_button)

        self.move_wire_gantry_to_postteardown_pos_button = QPushButton(self.verticalLayoutWidget_5)
        self.move_wire_gantry_to_postteardown_pos_button.setObjectName(u"move_wire_gantry_to_postteardown_pos_button")

        self.verticalLayout_5.addWidget(self.move_wire_gantry_to_postteardown_pos_button)

        self.move_wire_gantry_to_first_pickup_pos_button = QPushButton(self.verticalLayoutWidget_5)
        self.move_wire_gantry_to_first_pickup_pos_button.setObjectName(u"move_wire_gantry_to_first_pickup_pos_button")

        self.verticalLayout_5.addWidget(self.move_wire_gantry_to_first_pickup_pos_button)

        self.move_wire_gantry_to_second_pickup_pos_button = QPushButton(self.verticalLayoutWidget_5)
        self.move_wire_gantry_to_second_pickup_pos_button.setObjectName(u"move_wire_gantry_to_second_pickup_pos_button")

        self.verticalLayout_5.addWidget(self.move_wire_gantry_to_second_pickup_pos_button)

        self.verticalLayoutWidget_6 = QWidget(self.page_4)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(540, 300, 160, 80))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.hot_pool_gate_open_button = QPushButton(self.verticalLayoutWidget_6)
        self.hot_pool_gate_open_button.setObjectName(u"hot_pool_gate_open_button")

        self.verticalLayout_6.addWidget(self.hot_pool_gate_open_button)

        self.hot_pool_gate_close_button = QPushButton(self.verticalLayoutWidget_6)
        self.hot_pool_gate_close_button.setObjectName(u"hot_pool_gate_close_button")

        self.verticalLayout_6.addWidget(self.hot_pool_gate_close_button)

        self.home_flywheel_and_block_button = QPushButton(self.page_4)
        self.home_flywheel_and_block_button.setObjectName(u"home_flywheel_and_block_button")
        self.home_flywheel_and_block_button.setGeometry(QRect(60, 100, 191, 25))
        self.burn_wire_button = QPushButton(self.page_4)
        self.burn_wire_button.setObjectName(u"burn_wire_button")
        self.burn_wire_button.setGeometry(QRect(580, 400, 89, 25))
        self.discard_pump_actuation_button = QPushButton(self.page_4)
        self.discard_pump_actuation_button.setObjectName(u"discard_pump_actuation_button")
        self.discard_pump_actuation_button.setGeometry(QRect(540, 440, 171, 25))
        self.home_all_button = QPushButton(self.page_4)
        self.home_all_button.setObjectName(u"home_all_button")
        self.home_all_button.setGeometry(QRect(60, 50, 189, 25))
        self.backButton5 = QPushButton(self.page_4)
        self.backButton5.setObjectName(u"backButton5")
        self.backButton5.setGeometry(QRect(370, 470, 89, 25))
        self.stackedWidget.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.move_slide_gantry_to_label = QLabel(self.page)
        self.move_slide_gantry_to_label.setObjectName(u"move_slide_gantry_to_label")
        self.move_slide_gantry_to_label.setGeometry(QRect(270, 20, 151, 41))
        self.verticalLayoutWidget_2 = QWidget(self.page)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(160, 110, 160, 131))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.h_value_label = QLabel(self.verticalLayoutWidget_2)
        self.h_value_label.setObjectName(u"h_value_label")

        self.verticalLayout_2.addWidget(self.h_value_label)

        self.i_value_label = QLabel(self.verticalLayoutWidget_2)
        self.i_value_label.setObjectName(u"i_value_label")

        self.verticalLayout_2.addWidget(self.i_value_label)

        self.j_value_label = QLabel(self.verticalLayoutWidget_2)
        self.j_value_label.setObjectName(u"j_value_label")

        self.verticalLayout_2.addWidget(self.j_value_label)

        self.move_slide_gantry_speed_label = QLabel(self.verticalLayoutWidget_2)
        self.move_slide_gantry_speed_label.setObjectName(u"move_slide_gantry_speed_label")

        self.verticalLayout_2.addWidget(self.move_slide_gantry_speed_label)

        self.verticalLayoutWidget_4 = QWidget(self.page)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(380, 110, 160, 131))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.h_value_input = QTextEdit(self.verticalLayoutWidget_4)
        self.h_value_input.setObjectName(u"h_value_input")

        self.verticalLayout_4.addWidget(self.h_value_input)

        self.i_value_input = QTextEdit(self.verticalLayoutWidget_4)
        self.i_value_input.setObjectName(u"i_value_input")

        self.verticalLayout_4.addWidget(self.i_value_input)

        self.j_value_input = QTextEdit(self.verticalLayoutWidget_4)
        self.j_value_input.setObjectName(u"j_value_input")

        self.verticalLayout_4.addWidget(self.j_value_input)

        self.move_slide_gantry_speed_input = QTextEdit(self.verticalLayoutWidget_4)
        self.move_slide_gantry_speed_input.setObjectName(u"move_slide_gantry_speed_input")

        self.verticalLayout_4.addWidget(self.move_slide_gantry_speed_input)

        self.horizontalLayoutWidget = QWidget(self.page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(260, 280, 186, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.saveButton2 = QPushButton(self.horizontalLayoutWidget)
        self.saveButton2.setObjectName(u"saveButton2")

        self.horizontalLayout.addWidget(self.saveButton2)

        self.backButton2 = QPushButton(self.horizontalLayoutWidget)
        self.backButton2.setObjectName(u"backButton2")

        self.horizontalLayout.addWidget(self.backButton2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.move_wire_gantry_to_label = QLabel(self.page_2)
        self.move_wire_gantry_to_label.setObjectName(u"move_wire_gantry_to_label")
        self.move_wire_gantry_to_label.setGeometry(QRect(290, 80, 151, 31))
        self.move_wire_gantry_to_label.setFrameShape(QFrame.NoFrame)
        self.verticalLayoutWidget_7 = QWidget(self.page_2)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(160, 130, 160, 80))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.x_value_label = QLabel(self.verticalLayoutWidget_7)
        self.x_value_label.setObjectName(u"x_value_label")

        self.verticalLayout_7.addWidget(self.x_value_label)

        self.y_value_label = QLabel(self.verticalLayoutWidget_7)
        self.y_value_label.setObjectName(u"y_value_label")

        self.verticalLayout_7.addWidget(self.y_value_label)

        self.move_wire_gantry_speed = QLabel(self.verticalLayoutWidget_7)
        self.move_wire_gantry_speed.setObjectName(u"move_wire_gantry_speed")

        self.verticalLayout_7.addWidget(self.move_wire_gantry_speed)

        self.verticalLayoutWidget_8 = QWidget(self.page_2)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(400, 130, 160, 81))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.x_value_input = QTextEdit(self.verticalLayoutWidget_8)
        self.x_value_input.setObjectName(u"x_value_input")

        self.verticalLayout_8.addWidget(self.x_value_input)

        self.y_value_input = QTextEdit(self.verticalLayoutWidget_8)
        self.y_value_input.setObjectName(u"y_value_input")

        self.verticalLayout_8.addWidget(self.y_value_input)

        self.move_wire_gantry_speed_input = QTextEdit(self.verticalLayoutWidget_8)
        self.move_wire_gantry_speed_input.setObjectName(u"move_wire_gantry_speed_input")

        self.verticalLayout_8.addWidget(self.move_wire_gantry_speed_input)

        self.horizontalLayoutWidget_2 = QWidget(self.page_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(270, 250, 186, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveButton3 = QPushButton(self.horizontalLayoutWidget_2)
        self.saveButton3.setObjectName(u"saveButton3")

        self.horizontalLayout_2.addWidget(self.saveButton3)

        self.backButton3 = QPushButton(self.horizontalLayoutWidget_2)
        self.backButton3.setObjectName(u"backButton3")

        self.horizontalLayout_2.addWidget(self.backButton3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayoutWidget_3 = QWidget(self.page_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(280, 100, 181, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.delay_label = QLabel(self.horizontalLayoutWidget_3)
        self.delay_label.setObjectName(u"delay_label")

        self.horizontalLayout_3.addWidget(self.delay_label)

        self.delay_input = QTextEdit(self.horizontalLayoutWidget_3)
        self.delay_input.setObjectName(u"delay_input")

        self.horizontalLayout_3.addWidget(self.delay_input)

        self.burn_wire_label = QLabel(self.page_3)
        self.burn_wire_label.setObjectName(u"burn_wire_label")
        self.burn_wire_label.setGeometry(QRect(330, 40, 67, 17))
        self.horizontalLayoutWidget_4 = QWidget(self.page_3)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(280, 220, 186, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.saveButton4 = QPushButton(self.horizontalLayoutWidget_4)
        self.saveButton4.setObjectName(u"saveButton4")

        self.horizontalLayout_4.addWidget(self.saveButton4)

        self.backButton4 = QPushButton(self.horizontalLayoutWidget_4)
        self.backButton4.setObjectName(u"backButton4")

        self.horizontalLayout_4.addWidget(self.backButton4)

        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 868, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
        
        # Linking Pages

        self.stackedWidget.setCurrentIndex(0)

        # Go to API Lower calls page
        self.go_to_api_calls_lower_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        # Go back to MAIN page
        self.backButton5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        # Take Section Page
        self.take_section_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.backButton1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        

        # Move slide gantry page
        self.move_slide_gantry_to_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.backButton2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        

        # Move wire gantry page
        self.move_wire_gantry_to_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.backButton3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        

        # Burn Wire Page
        self.burn_wire_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.backButton4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        

        # Highest Level API calls
        self.saveButton1.clicked.connect(self.take_section_func)
        self.first_tissue_pickup_button.clicked.connect(api_calls_higher.first_tissue_pickup)
        self.second_tissue_pickup_button.clicked.connect(api_calls_higher.second_tissue_pickup)
        self.discard_tissue_button.clicked.connect(api_calls_higher.discard_tissue)

        # Lower Level API Calls
        # Home all
        self.home_all_button.clicked.connect(api_calls_lower.home_all)
        # Home Flywheel and Block
        self.home_flywheel_and_block_button.clicked.connect(api_calls_lower.home_flywheel_and_block)
        # Home Wire Gantry
        self.home_wire_gantry_button.clicked.connect(api_calls_lower.home_wire_gantry)
        # Move Wire Gantry To - takes inputs
        self.saveButton3.clicked.connect(self.move_wire_gantry_input)
        # Move Wire Gantry to safe position
        self.move_wire_gantry_to_safe_pos_button.clicked.connect(api_calls_lower.move_wire_gantry_to_safe_pos)
        # Move Wire Gantry to dip position
        self.move_wire_gantry_to_dip_pos_button.clicked.connect(api_calls_lower.move_wire_gantry_to_dip_pos)
        # Move Wire Gantry to pre-teardown position
        self.move_wire_gantry_to_preteardown_pos_button.clicked.connect(api_calls_lower.move_wire_gantry_to_preteardown_pos)
        # Move Wire Gantry to post-teardown positon
        self.move_wire_gantry_to_postteardown_pos_button.clicked.connect(api_calls_lower.move_wire_gantry_to_postteardown_pos)
        # Move Wire Gantry to First Pickup position
        self.move_wire_gantry_to_first_pickup_pos_button.clicked.connect(api_calls_lower.move_wire_gantry_to_first_pickup_pos)
        # Move Wire Gantry to Second Pickup position
        self.move_wire_gantry_to_second_pickup_pos_button.clicked.connect(api_calls_lower.move_wire_gantry_to_second_pickup_pos)
        # Home Slide Gantry
        self.home_slide_gantry_button.clicked.connect(api_calls_lower.home_slide_gantry)
        # Move Slide Gantry To - takes inputs
        self.saveButton2.clicked.connect(self.move_slide_gantry_input)
        # Move Slide to first pickup position
        self.move_slide_to_first_pickup_position_button.clicked.connect(api_calls_lower.move_slide_to_first_pickup_position)
        # Move Slide to first pivot position
        self.move_slide_to_first_pivot_position_button.clicked.connect(api_calls_lower.move_slide_to_first_pivot_position)
        # Move Slide to first final position
        self.move_slide_to_first_final_position_button.clicked.connect(api_calls_lower.move_slide_to_first_final_position)
        # Move Slide to second pickup postion
        self.move_slide_to_second_pickup_position_button.clicked.connect(api_calls_lower.move_slide_to_second_pickup_position)
        # Move Slide to second pivot position
        self.move_slide_to_second_pivot_position_button.clicked.connect(api_calls_lower.move_slide_to_second_pivot_position)
        # Move Slide to second final position
        self.move_slide_to_second_final_position_button.clicked.connect(api_calls_lower.move_slide_to_second_final_position)
        # Burn Wire     
        self.saveButton4.clicked.connect(self.burn_wire_input)
        # Discard Pump Actuation
        self.discard_pump_actuation_button.clicked.connect(api_calls_lower.discard_pump_actuation)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.take_section_button.setText(QCoreApplication.translate("MainWindow", u"Take Section ", None))
        self.first_tissue_pickup_button.setText(QCoreApplication.translate("MainWindow", u"First Tissue Pickup", None))
        self.second_tissue_pickup_button.setText(QCoreApplication.translate("MainWindow", u"Second Tissue Pickup", None))
        self.discard_tissue_button.setText(QCoreApplication.translate("MainWindow", u"Discard Tissue ", None))
        self.api_calls_higher_label.setText(QCoreApplication.translate("MainWindow", u"API CALLS HIGHER", None))
        self.go_to_api_calls_lower_button.setText(QCoreApplication.translate("MainWindow", u"Lower API", None))
        self.take_section_label.setText(QCoreApplication.translate("MainWindow", u"TAKE SECTION", None))
        self.thickness_label.setText(QCoreApplication.translate("MainWindow", u"Thickness ", None))
        self.count_label.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.backButton1.setText(QCoreApplication.translate("MainWindow", u"Back ", None))
        self.saveButton1.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.take_section_speed_label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_4.setText("")
        self.api_calls_lower.setText(QCoreApplication.translate("MainWindow", u"API CALLS LOWER", None))
        self.home_slide_gantry_button.setText(QCoreApplication.translate("MainWindow", u"Home Slide Gantry", None))
        self.move_slide_gantry_to_button.setText(QCoreApplication.translate("MainWindow", u"Move Slide Gantry To", None))
        self.move_slide_to_first_pickup_position_button.setText(QCoreApplication.translate("MainWindow", u"Move Slide To First Pickup Position", None))
        self.move_slide_to_first_pivot_position_button.setText(QCoreApplication.translate("MainWindow", u"Move Slide To First Pivot Position", None))
        self.move_slide_to_first_final_position_button.setText(QCoreApplication.translate("MainWindow", u"Move Slide to First Final Position", None))
        self.move_slide_to_second_pickup_position_button.setText(QCoreApplication.translate("MainWindow", u"Move Slide to Second Pickup Position", None))
        self.move_slide_to_second_pivot_position_button.setText(QCoreApplication.translate("MainWindow", u"Move Slide to Second Pivot Position", None))
        self.move_slide_to_second_final_position_button.setText(QCoreApplication.translate("MainWindow", u"Move Slide To Second Final Position", None))
        self.home_wire_gantry_button.setText(QCoreApplication.translate("MainWindow", u"Home Wire Gantry", None))
        self.move_wire_gantry_to_button.setText(QCoreApplication.translate("MainWindow", u"Move Wire Gantry to", None))
        self.move_wire_gantry_to_safe_pos_button.setText(QCoreApplication.translate("MainWindow", u"Move Wire Gantry to Safe Position", None))
        self.move_wire_gantry_to_dip_pos_button.setText(QCoreApplication.translate("MainWindow", u"Move Wire Gantry to Dip Position", None))
        self.move_wire_gantry_to_preteardown_pos_button.setText(QCoreApplication.translate("MainWindow", u"Move Wire Gantry to Pre-teardown position", None))
        self.move_wire_gantry_to_postteardown_pos_button.setText(QCoreApplication.translate("MainWindow", u"Move Wire Gantry to Post-teardown positon", None))
        self.move_wire_gantry_to_first_pickup_pos_button.setText(QCoreApplication.translate("MainWindow", u"Move Wire Gantry to First Pickup Position", None))
        self.move_wire_gantry_to_second_pickup_pos_button.setText(QCoreApplication.translate("MainWindow", u"Move Wire Gantry to Second Pickup Position", None))
        self.hot_pool_gate_open_button.setText(QCoreApplication.translate("MainWindow", u"Hot Pool Gate Open", None))
        self.hot_pool_gate_close_button.setText(QCoreApplication.translate("MainWindow", u"Hot Pool Gate Close", None))
        self.home_flywheel_and_block_button.setText(QCoreApplication.translate("MainWindow", u"Home Flywheel and Block", None))
        self.burn_wire_button.setText(QCoreApplication.translate("MainWindow", u"Burn Wire", None))
        self.discard_pump_actuation_button.setText(QCoreApplication.translate("MainWindow", u"Discard Pump Actuation", None))
        self.home_all_button.setText(QCoreApplication.translate("MainWindow", u"Home All", None))
        self.backButton5.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.move_slide_gantry_to_label.setText(QCoreApplication.translate("MainWindow", u"Move Slide Gantry To", None))
        self.h_value_label.setText(QCoreApplication.translate("MainWindow", u"H Value", None))
        self.i_value_label.setText(QCoreApplication.translate("MainWindow", u"I Value", None))
        self.j_value_label.setText(QCoreApplication.translate("MainWindow", u"J Value", None))
        self.move_slide_gantry_speed_label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.saveButton2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.backButton2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.move_wire_gantry_to_label.setText(QCoreApplication.translate("MainWindow", u"Move Wire Gantry To", None))
        self.x_value_label.setText(QCoreApplication.translate("MainWindow", u"X Value", None))
        self.y_value_label.setText(QCoreApplication.translate("MainWindow", u"Y Value:", None))
        self.move_wire_gantry_speed.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.saveButton3.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.backButton3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.delay_label.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.burn_wire_label.setText(QCoreApplication.translate("MainWindow", u"Burn Wire", None))
        self.saveButton4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.backButton4.setText(QCoreApplication.translate("MainWindow", u"Back", None))

    # HIGHEST LEVEL API

    # Take thickness and count input from GUI
    def take_section_func(self):
        print('debug test')
        thickness = int(str(self.thickness_input.toPlainText()))
        count = int(str(self.count_input.toPlainText()))
        #speed = int(str(self.take_section_speed_input.toPlainText()))
        api_calls_higher.take_sections(thickness, count)
        self.thickness_input.clear()
        self.count_input.clear()
        self.take_section_speed_input.clear()

    # LOWER LEVEL API

    # Move slide gantry to
    def move_slide_gantry_input(self):
        h_input = int(str(self.h_value_input.toPlainText()))
        i_input = int(str(self.i_value_input.toPlainText()))
        j_input = int(str(self.j_value_input.toPlainText()))
        speed_input = int(str(self.move_slide_gantry_speed_input.toPlainText()))
        api_calls_lower.move_slide_gantry_to(h_input, i_input, j_input)
        self.h_value_input.clear()
        self.i_value_input.clear()
        self.j_value_input.clear()

    # Move wire gantry to
    def move_wire_gantry_input(self):
        x_input = int(str(self.x_value_input.toPlainText()))
        y_input = int(str(self.y_value_input.toPlainText()))
        speed_input = int(str(self.move_wire_gantry_speed_input.toPlainText()))
        api_calls_lower.move_wire_gantry_to(x_input, y_input)
        self.x_value_input.clear()
        self.y_value_input.clear()
    
    # Burn Wire
    def burn_wire_input(self):
        delay_input = int(str(self.delay_input.toPlainText()))
        api_calls_lower.burn_wire(delay_input)
        self.delay_input.clear()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

