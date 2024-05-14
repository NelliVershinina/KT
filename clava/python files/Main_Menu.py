from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QMainWindow
import sys 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1910, 1057)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 90, 1141, 151))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(740, 320, 381, 191))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Play.setFont(font)
        self.Play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Play.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(36, 36, 36, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Play.setObjectName("Play")
        self.Settings = QtWidgets.QPushButton(self.centralwidget)
        self.Settings.setGeometry(QtCore.QRect(740, 760, 381, 191))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Settings.setFont(font)
        self.Settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Settings.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(36, 36, 36, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Settings.setObjectName("Settings")
        self.Ruls = QtWidgets.QPushButton(self.centralwidget)
        self.Ruls.setGeometry(QtCore.QRect(740, 540, 381, 191))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Ruls.setFont(font)
        self.Ruls.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ruls.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(36, 36, 36, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Ruls.setObjectName("Ruls")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 80, 1141, 181))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("2.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("3.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(1700, 810, 131, 121))
        self.Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Exit.setFont(font)
        self.Exit.setStyleSheet("QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(36, 36, 36, 255), stop:1 rgba(120, 120, 120, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0          rgba(97, 97, 97, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.Exit.setObjectName("Exit")
        self.label_2.raise_()
        self.Play.raise_()
        self.Settings.raise_()
        self.Ruls.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.Exit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Клавиатурный тренажер"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d1d1d1;\">КЛАВИАТУРНЫЙ ТРЕНАЖЕР</span></p></body></html>"))
        self.Play.setText(_translate("MainWindow", "Начать тренировку"))
        self.Settings.setText(_translate("MainWindow", "Настройки"))
        self.Ruls.setText(_translate("MainWindow", "Правила "))
        self.Exit.setText(_translate("MainWindow", "Выход"))
