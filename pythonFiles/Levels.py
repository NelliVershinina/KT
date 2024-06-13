from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Third_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Fon = QtWidgets.QLabel(self.centralwidget)
        self.Fon.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.Fon.setText("")
        self.Fon.setPixmap(QtGui.QPixmap('C:/Users/Home/Desktop/clava/image/4.png'))
        self.Fon.setObjectName("Fon")
        self.ButtonNazad = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonNazad.setGeometry(QtCore.QRect(1700, 10, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ButtonNazad.setFont(font)
        self.ButtonNazad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonNazad.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.ButtonNazad.setObjectName("ButtonNazad")
        self.VyborYrovny = QtWidgets.QLabel(self.centralwidget)
        self.VyborYrovny.setGeometry(QtCore.QRect(400, 0, 1000, 200))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.VyborYrovny.setFont(font)
        self.VyborYrovny.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(86, 86, 86);")
        self.VyborYrovny.setText("")
        self.VyborYrovny.setPixmap(QtGui.QPixmap('C:/Users/Home/Desktop/clava/image/2.png'))
        self.VyborYrovny.setAlignment(QtCore.Qt.AlignCenter)
        self.VyborYrovny.setObjectName("VyborYrovny")
        self.Bukva = QtWidgets.QPushButton(self.centralwidget)
        self.Bukva.setGeometry(QtCore.QRect(250, 450, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Bukva.setFont(font)
        self.Bukva.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bukva.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Bukva.setObjectName("Bukva")
        self.Slova = QtWidgets.QPushButton(self.centralwidget)
        self.Slova.setGeometry(QtCore.QRect(250, 600, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Slova.setFont(font)
        self.Slova.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Slova.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Slova.setObjectName("Slova")
        self.Text = QtWidgets.QPushButton(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(250, 900, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Text.setFont(font)
        self.Text.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Text.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Text.setObjectName("Text")
        self.Bukva_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Bukva_2.setGeometry(QtCore.QRect(1270, 450, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Bukva_2.setFont(font)
        self.Bukva_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Bukva_2.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Bukva_2.setObjectName("Bukva_2")
        self.Slova_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Slova_2.setGeometry(QtCore.QRect(1270, 600, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Slova_2.setFont(font)
        self.Slova_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Slova_2.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Slova_2.setObjectName("Slova_2")
        self.Text_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Text_2.setGeometry(QtCore.QRect(1270, 900, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Text_2.setFont(font)
        self.Text_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Text_2.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Text_2.setObjectName("Text_2")
        
        self.Predloshenia_Eng = QtWidgets.QPushButton(self.centralwidget)
        self.Predloshenia_Eng.setGeometry(QtCore.QRect(1270, 750, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Predloshenia_Eng.setFont(font)
        self.Predloshenia_Eng.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Predloshenia_Eng.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Predloshenia_Eng.setObjectName("Text_2")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 40, 271, 81))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(207, 207, 207);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.Mark = QtWidgets.QPushButton(self.centralwidget)
        self.Mark.setGeometry(QtCore.QRect(720, 750, 450, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Mark.setFont(font)
        self.Mark.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mark.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Mark.setObjectName("Mark")
        
        self.Predloshenia = QtWidgets.QPushButton(self.centralwidget)
        self.Predloshenia.setGeometry(QtCore.QRect(250, 750, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Predloshenia.setFont(font)
        self.Predloshenia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Predloshenia.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(255, 255, 255, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Predloshenia.setObjectName("Bukva_2")
        
        self.Cherta1 = QtWidgets.QLabel(self.centralwidget)
        self.Cherta1.setGeometry(QtCore.QRect(50, 350, 3031, 16))
        self.Cherta1.setStyleSheet("color: rgb(236, 236, 236);")
        self.Cherta1.setObjectName("Cherta1")
        
        self.Russian = QtWidgets.QLabel(self.centralwidget)
        self.Russian.setGeometry(QtCore.QRect(300, 270, 500, 100))
        self.Russian.setStyleSheet("color: rgb(236, 236, 236);")
        self.Russian.setObjectName("Russian")
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Russian.setFont(font)
        
        self.English = QtWidgets.QLabel(self.centralwidget)
        self.English.setGeometry(QtCore.QRect(1260, 270, 500, 100))
        self.English.setStyleSheet("color: rgb(236, 236, 236);")
        self.English.setObjectName("English")
        font = QtGui.QFont()
        font.setPointSize(40)
        self.English.setFont(font)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.ButtonNazad.setText(_translate("MainWindow", "Назад"))
        self.Bukva.setText(_translate("MainWindow", "Буквы"))
        self.Slova.setText(_translate("MainWindow", "Слова"))
        self.Text.setText(_translate("MainWindow", "Текст"))
        self.Bukva_2.setText(_translate("MainWindow", "Буквы"))
        self.Slova_2.setText(_translate("MainWindow", "Слова"))
        self.Text_2.setText(_translate("MainWindow", "Текст"))
        self.label.setText(_translate("MainWindow", "Уровни"))
        self.Mark.setText(_translate("MainWindow", "Знаки препинания"))
        self.Predloshenia.setText(_translate("MainWindow", "Предложения"))
        self.Predloshenia_Eng.setText(_translate("MainWindow", "Предложения"))
        self.Cherta1.setText(_translate("MainWindow", "______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.Russian.setText(_translate("MainWindow", "Русский"))
        self.English.setText(_translate("MainWindow", "Английский"))