from PyQt5 import QtCore, QtGui, QtWidgets
from path_fon import set_fon

class Ui_Settings_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(3262, 1563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Fon = QtWidgets.QLabel(self.centralwidget)
        self.Fon.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.Fon.setText("")
        self.Fon.setPixmap(QtGui.QPixmap("C:\\Users\\Home\\Desktop\\clava\\image\\4.png"))
        self.Fon.setScaledContents(True)
        self.Fon.setObjectName("Fon")
        self.Text1 = QtWidgets.QLabel(self.centralwidget)
        self.Text1.setGeometry(QtCore.QRect(30, 60, 491, 171))
        font = QtGui.QFont()
        font.setPointSize(52)
        self.Text1.setFont(font)
        self.Text1.setStyleSheet("background-color: rgb(157, 157, 157);\n"
"color: rgb(227, 227, 227);")
        self.Text1.setObjectName("Text1")
        self.Text2 = QtWidgets.QLabel(self.centralwidget)
        self.Text2.setGeometry(QtCore.QRect(30, 440, 601, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Text2.setFont(font)
        self.Text2.setStyleSheet("color: rgb(236, 236, 236);")
        self.Text2.setObjectName("Text2")
        self.Cherta1 = QtWidgets.QLabel(self.centralwidget)
        self.Cherta1.setGeometry(QtCore.QRect(30, 510, 3031, 16))
        self.Cherta1.setStyleSheet("color: rgb(236, 236, 236);")
        self.Cherta1.setObjectName("Cherta1")
        self.Cherta2 = QtWidgets.QLabel(self.centralwidget)
        self.Cherta2.setGeometry(QtCore.QRect(30, 730, 3031, 16))
        self.Cherta2.setStyleSheet("color: rgb(236, 236, 236);")
        self.Cherta2.setObjectName("Cherta2")
        self.Text3 = QtWidgets.QLabel(self.centralwidget)
        self.Text3.setGeometry(QtCore.QRect(30, 660, 601, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Text3.setFont(font)
        self.Text3.setStyleSheet("color: rgb(236, 236, 236);")
        self.Text3.setObjectName("Text3")
        self.BFon = QtWidgets.QPushButton(self.centralwidget)
        self.BFon.setGeometry(QtCore.QRect(1600, 400, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.BFon.setFont(font)
        self.BFon.setObjectName("BFon")
        self.BFon_2 = QtWidgets.QPushButton(self.centralwidget)
        self.BFon_2.setGeometry(QtCore.QRect(1600, 620, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.BFon_2.setFont(font)
        self.BFon_2.setObjectName("BFon_2")
        self.Cherta3 = QtWidgets.QLabel(self.centralwidget)
        self.Cherta3.setGeometry(QtCore.QRect(30, 940, 3031, 16))
        self.Cherta3.setStyleSheet("color: rgb(236, 236, 236);")
        self.Cherta3.setObjectName("Cherta3")
        self.Text4 = QtWidgets.QLabel(self.centralwidget)
        self.Text4.setGeometry(QtCore.QRect(30, 870, 601, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Text4.setFont(font)
        self.Text4.setStyleSheet("color: rgb(236, 236, 236);")
        self.Text4.setObjectName("Text4")
        self.BFon_3 = QtWidgets.QPushButton(self.centralwidget)
        self.BFon_3.setGeometry(QtCore.QRect(1600, 830, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.BFon_3.setFont(font)
        self.BFon_3.setObjectName("BFon_3")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonBack.setGeometry(QtCore.QRect(1620, 100, 100, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ButtonBack.setFont(font)
        self.ButtonBack.setObjectName("ButtonBack")
        self.ButtonBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BFon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BFon_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BFon_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonBack.clicked.connect(self.showMainWindow)
        
        self.BFon.setStyleSheet("QPushButton {\n"
                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(36, 36, 36, 255), stop:1 rgba(120, 120, 120, 255));\n"
                        "color: #d1d1d1; /* Светло-серый цвет текста */\n"
                        "}\n"
                        "\n"
                        "QPushButton:pressed {\n"
                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
                        "}")
        
        self.BFon_3.setStyleSheet("QPushButton {\n"
                           "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(36, 36, 36, 255), stop:1 rgba(120, 120, 120, 255));\n"
                           "color: #d1d1d1; /* Светло-серый цвет текста */\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed {\n"
                           "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
                           "}")
        
        self.BFon_2.setStyleSheet("QPushButton {\n"
                           "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(36, 36, 36, 255), stop:1 rgba(120, 120, 120, 255));\n"
                           "color: #d1d1d1; /* Светло-серый цвет текста */\n"
                           "}\n"
                           "\n"
                           "QPushButton:pressed {\n"
                           "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
                           "}")
    
        self.ButtonBack.setStyleSheet("QPushButton {\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(36, 36, 36, 255), stop:1 rgba(120, 120, 120, 255));\n"
                               "color: #d1d1d1; /* Светло-серый цвет текста */\n"
                               "}\n"
                               "\n"
                               "QPushButton:pressed {\n"
                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
                               "}")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.BFon.clicked.connect(self.openBackgroundSelection)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Text1.setText(_translate("MainWindow", "Настройки"))
        self.Text2.setText(_translate("MainWindow", "Выбор фона"))
        self.Cherta1.setText(_translate("MainWindow", "_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.Cherta2.setText(_translate("MainWindow", "_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.Text3.setText(_translate("MainWindow", "Музыка"))
        self.BFon.setText(_translate("MainWindow", "V"))
        self.BFon_2.setText(_translate("MainWindow", "Вкл/выкл"))
        self.Cherta3.setText(_translate("MainWindow", "_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.Text4.setText(_translate("MainWindow", "Полный экран"))
        self.BFon_3.setText(_translate("MainWindow", "Вкл/выкл"))
        self.ButtonBack.setText(_translate("MainWindow", "Назад"))
        
    def showMainWindow(self):
        self.stacked_widget.setCurrentWidget(self.main_window)
        
    def openBackgroundSelection(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog.setWindowTitle("Выбор фона")
        self.dialog.resize(300, 200)
        layout = QtWidgets.QVBoxLayout(self.dialog)
        
        self.button1 = QtWidgets.QPushButton(self.dialog)
        self.button1.setStyleSheet(r"QPushButton {background-image: url('C:/Users/Home/Desktop/clava/image/dlack.jpg');}")
        self.button1.clicked.connect(lambda: self.changeBackground('C:/Users/Home/Desktop/clava/image/dlack.jpg'))
        layout.addWidget(self.button1)

        self.button2 = QtWidgets.QPushButton(self.dialog)
        self.button2.setStyleSheet(r"QPushButton {background-image: url('C:/Users/Home/Desktop/clava/image/gray.jpg');}")
        self.button2.clicked.connect(lambda: self.changeBackground('C:/Users/Home/Desktop/clava/image/gray.jpg'))
        layout.addWidget(self.button2)

        self.button3 = QtWidgets.QPushButton(self.dialog)
        self.button3.setStyleSheet(r"QPushButton {background-image: url('C:/Users/Home/Desktop/clava/image/red.jpg');}")
        self.button3.clicked.connect(lambda: self.changeBackground('C:/Users/Home/Desktop/clava/image/red.jpg'))
        layout.addWidget(self.button3)
        
        self.button4 = QtWidgets.QPushButton(self.dialog)
        self.button4.setStyleSheet(r"QPushButton {background-image: url('C:/Users/Home/Desktop/clava/image/pink.jpg');}")
        self.button4.clicked.connect(lambda: self.changeBackground('C:/Users/Home/Desktop/clava/image/pink.jpg'))
        layout.addWidget(self.button4)
        
        self.button5 = QtWidgets.QPushButton(self.dialog)
        self.button5.setStyleSheet(r"QPushButton {background-image: url('C:/Users/Home/Desktop/clava/image/blue.jpg');}")
        self.button5.clicked.connect(lambda: self.changeBackground('C:/Users/Home/Desktop/clava/image/blue.jpg'))
        layout.addWidget(self.button5)
        
        self.button6 = QtWidgets.QPushButton(self.dialog)
        self.button6.setStyleSheet(r"QPushButton {background-image: url('C:/Users/Home/Desktop/clava/image/gray-black.jpg');}")
        self.button6.clicked.connect(lambda: self.changeBackground('C:/Users/Home/Desktop/clava/image/gray-black.jpg'))
        layout.addWidget(self.button6)
        
        self.button7 = QtWidgets.QPushButton(self.dialog)
        self.button7.setStyleSheet(r"QPushButton {background-image: url('C:/Users/Home/Desktop/clava/image/black.jpg');}")
        self.button7.clicked.connect(lambda: self.changeBackground('C:/Users/Home/Desktop/clava/image/black.jpg'))
        layout.addWidget(self.button7)

        self.dialog.setLayout(layout)
        self.dialog.exec_()
        
    def changeBackground(self, imagePath):
        set_fon(imagePath)