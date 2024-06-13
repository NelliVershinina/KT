from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import os
import time
from path_fon import get_fon

class Ui_Letters_Ru(QtCore.QObject):
    def setupUi(self, MainWindow):
        super(Ui_Letters_Ru, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.is_exercise_completed = False

        self.Fon = QtWidgets.QLabel(self.centralwidget)
        self.Fon.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.Fon.setText("")
        self.Fon.setPixmap(QtGui.QPixmap(get_fon()))
        self.Fon.setScaledContents(True)
        self.Fon.setObjectName("Fon")

        self.key_image_mapping = {
            '1': os.path.abspath('image/1.png'),
            '2': os.path.abspath('image/@.png'),
            '3': os.path.abspath('image/#.png'),
            '4': os.path.abspath('image/$.png'),
            '5': os.path.abspath('image/5.png'),
            '6': os.path.abspath('image/6.png'),
            '7': os.path.abspath('image/7.png'),
            '8': os.path.abspath('image/8.png'),
            '9': os.path.abspath('image/9.png'),
            '0': os.path.abspath('image/0.png'),
            ',': os.path.abspath('image/,.png'),
            '.': os.path.abspath('image/,.png'),
            ':': os.path.abspath('image/6.png'),
            ';': os.path.abspath('image/$.png'),
            '?': os.path.abspath('image/7.png'),
            '!': os.path.abspath('image/1.png'),
            '-': os.path.abspath('image/-.png'),
            'Enter': os.path.abspath('image/enter.png'),
            ' ': os.path.abspath('image/Space.png'), 
            
            'а': os.path.abspath('image/F.png'),
            'б': os.path.abspath('image/б.png'),
            'в': os.path.abspath('image/D.png'),
            'г': os.path.abspath('image/U.png'),
            'д': os.path.abspath('image/L.png'),
            'е': os.path.abspath('image/T.png'),
            'ё': os.path.abspath('image/ё.png'),
            'ж': os.path.abspath('image/ж.png'),
            'з': os.path.abspath('image/P.png'),
            'и': os.path.abspath('image/B.png'),
            'й': os.path.abspath('image/Q.png'),
            'к': os.path.abspath('image/R.png'),
            'л': os.path.abspath('image/K.png'),
            'м': os.path.abspath('image/V.png'),
            'н': os.path.abspath('image/Y.png'),
            'о': os.path.abspath('image/J.png'),
            'п': os.path.abspath('image/G.png'),
            'р': os.path.abspath('image/H.png'),
            'с': os.path.abspath('image/C.png'),
            'т': os.path.abspath('image/N.png'),
            'у': os.path.abspath('image/E.png'),
            'ф': os.path.abspath('image/A.png'),
            'х': os.path.abspath('image/х.png'),
            'ц': os.path.abspath('image/W.png'),
            'ч': os.path.abspath('image/X.png'),
            'ш': os.path.abspath('image/I.png'),
            'щ': os.path.abspath('image/O.png'),
            'ы': os.path.abspath('image/S.png'),
            'ъ': os.path.abspath('image/ъ.png'),
            'ь': os.path.abspath('image/M.png'),
            'э': os.path.abspath('image/э.png'),
            'ю': os.path.abspath('image/ю.png'),
            'я': os.path.abspath('image/Z.png'),
            
            'А': os.path.abspath('image/F.png'),
            'Б': os.path.abspath('image/б.png'),
            'В': os.path.abspath('image/D.png'),
            'Г': os.path.abspath('image/U.png'),
            'Д': os.path.abspath('image/L.png'),
            'Е': os.path.abspath('image/T.png'),
            'Ё': os.path.abspath('image/ё.png'),
            'Ж': os.path.abspath('image/ж.png'),
            'З': os.path.abspath('image/P.png'),
            'И': os.path.abspath('image/B.png'),
            'Й': os.path.abspath('image/Q.png'),
            'К': os.path.abspath('image/R.png'),
            'Л': os.path.abspath('image/K.png'),
            'М': os.path.abspath('image/V.png'),
            'Н': os.path.abspath('image/Y.png'),
            'О': os.path.abspath('image/J.png'),
            'П': os.path.abspath('image/G.png'),
            'Р': os.path.abspath('image/H.png'),
            'С': os.path.abspath('image/C.png'),
            'Т': os.path.abspath('image/N.png'),
            'У': os.path.abspath('image/E.png'),
            'Ф': os.path.abspath('image/A.png'),
            'Х': os.path.abspath('image/х.png'),
            'Ц': os.path.abspath('image/W.png'),
            'Ч': os.path.abspath('image/X.png'),
            'Ш': os.path.abspath('image/I.png'),
            'Щ': os.path.abspath('image/O.png'),
            'Ы': os.path.abspath('image/S.png'),
            'Ъ': os.path.abspath('image/ъ.png'),
            'Ь': os.path.abspath('image/M.png'),
            'Э': os.path.abspath('image/э.png'),
            'Ю': os.path.abspath('image/ю.png'),
            'Я': os.path.abspath('image/Z.png'),
        }

        self.P_Fon = QtWidgets.QLabel(self.centralwidget)
        self.P_Fon.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.P_Fon.setText("")
        self.P_Fon.setObjectName("P_Fon")

        self.Text = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(50, 40, 1800, 300))
        self.Text.setStyleSheet("background-color: rgb(140, 140, 140);")
        self.Text.setObjectName("Text")

        self.VvodTexta = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.VvodTexta.setGeometry(QtCore.QRect(50, 360, 1800, 200))
        self.VvodTexta.setObjectName("VvodTexta")
        self.VvodTexta.textChanged.connect(self.handle_text_changed)
        self.VvodTexta.installEventFilter(self)

        self.KartinkaKlavish = QtWidgets.QLabel(self.centralwidget)
        self.KartinkaKlavish.setGeometry(QtCore.QRect(300, 580, 1400, 360))
        self.KartinkaKlavish.setObjectName("KartinkaKlavish")
        self.KartinkaKlavish.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.text_to_type =  "а а а ааа б б б б бабабаба ууу у у у еееее ээ ъ ъ эъэъэъэъ фф ц ы фцы фцы фыц фыц цыф цыф и и иии ит ит ит ти ти ь ъ ю"
        self.Text.setStyleSheet("background-color: rgb(200, 200, 200); font-size: 15pt;")
        self.Text.setText(self.text_to_type)
        self.current_index = 0
        self.VvodTexta.setFocus()

        self.start_time = None
        self.total_errors = 0
        self.total_characters = 0
        self.Text.setText(self.text_to_type)
        self.current_index = 0
        self.VvodTexta.setFocus()

        self.MenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.MenuButton.setGeometry(QtCore.QRect(1100, 950, 200, 100))
        self.MenuButton.setObjectName("mainMenuButton")
        self.MenuButton.setText("В главное меню")

        MainWindow.setCentralWidget(self.centralwidget)

        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(850, 950, 200, 100))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.mainMenuButton.setText("Пауза")
        self.mainMenuButton.clicked.connect(self.Pause)
        self.is_paused = False

        MainWindow.setCentralWidget(self.centralwidget)

        self.endExerciseButton = QtWidgets.QPushButton(self.centralwidget)
        self.endExerciseButton.setGeometry(QtCore.QRect(600, 950, 200, 100))
        self.endExerciseButton.setObjectName("endExerciseButton")
        self.endExerciseButton.setText("Завершить упражнение")
        self.endExerciseButton.clicked.connect(self.end_exercise)

        MainWindow.setCentralWidget(self.centralwidget)

        self.show_next_key_image()

    def show_next_key_image(self):
        if self.current_index < len(self.text_to_type):
            next_char = self.text_to_type[self.current_index]
            if next_char == '\n':
                next_char = 'Enter'
            self.change_keyboard_image(next_char)

    def end_exercise(self):
        if not self.is_exercise_completed:
            self.display_results()
            self.is_exercise_completed = True
            self.VvodTexta.setReadOnly(True)
            self.mainMenuButton.setEnabled(False)
            self.endExerciseButton.setEnabled(False)

    def Pause(self):
        if self.is_exercise_completed:
            return

        if self.is_paused:
            self.is_paused = False
            self.VvodTexta.setReadOnly(False)
            self.mainMenuButton.setText("Пауза")
        else:
            self.is_paused = True
            self.VvodTexta.setReadOnly(True)
            self.mainMenuButton.setText("Продолжить")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typing Tutor"))

    def change_keyboard_image(self, key):
        if key in self.key_image_mapping:
            image_path = self.key_image_mapping[key]
            if os.path.exists(image_path):
                self.KartinkaKlavish.setPixmap(QtGui.QPixmap(image_path))

    def eventFilter(self, obj, event):
        if obj == self.VvodTexta and event.type() == QtCore.QEvent.KeyPress:
            if not self.is_paused and not self.is_exercise_completed:
                input_text = self.VvodTexta.toPlainText()
                if input_text == self.text_to_type[:len(input_text)]:
                    self.current_index = len(input_text)
                    self.show_next_key_image()
        return super(Ui_Letters_Ru, self).eventFilter(obj, event)

    def handle_text_changed(self):
        if self.is_paused or self.is_exercise_completed:
            return

        input_text = self.VvodTexta.toPlainText()
        if self.start_time is None and not self.is_paused:
            self.start_time = time.time()

        if input_text == self.text_to_type[:len(input_text)]:
            self.VvodTexta.setStyleSheet("background-color: lightgreen;")
            self.current_index = len(input_text)
            if len(input_text) == len(self.text_to_type):
                self.display_results()
        else:
            self.VvodTexta.setStyleSheet("background-color: pink;")
            self.total_errors += 1

        if len(input_text) > len(self.text_to_type):
            self.VvodTexta.setPlainText(self.text_to_type)
            self.VvodTexta.moveCursor(QtGui.QTextCursor.End)

        self.show_next_key_image()

    def display_results(self):
        if self.start_time is None:
            QMessageBox.warning(None, "Ошибка", "Невозможно отобразить результаты: Вы не начали писать. Попробуйте заново! Напишите что-нибудь и затем завершайте упражнение!")
            return

        elapsed_time = time.time() - self.start_time
        input_text = self.VvodTexta.toPlainText().replace(" ", "")
        accuracy = ((len(input_text) - self.total_errors) / len(self.text_to_type)) * 100
        self.Text.setText(f"Вы закончили упражнение! \nВремя: {elapsed_time:.2f} секунд\nПроцент точности: {accuracy:.2f}%\nВведено знаков: {len(input_text)}")
        self.Text.setStyleSheet("background-color: rgb(200, 200, 200); font-size: 15pt;")
        self.is_exercise_completed = True
        self.VvodTexta.setReadOnly(True)
        self.mainMenuButton.setEnabled(False)
        self.endExerciseButton.setEnabled(False)