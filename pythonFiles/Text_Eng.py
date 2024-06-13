from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import os
import time
from path_fon import get_fon

class Ui_Text_Eng_Window(QtCore.QObject):
    def setupUi(self, MainWindow):
        super(Ui_Text_Eng_Window, self).__init__()
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
            
            'a': os.path.abspath('image/A.png'),
            'b': os.path.abspath('image/B.png'),
            'c': os.path.abspath('image/C.png'),
            'd': os.path.abspath('image/D.png'),
            'e': os.path.abspath('image/E.png'),
            'f': os.path.abspath('image/F.png'),
            'g': os.path.abspath('image/G.png'),
            'h': os.path.abspath('image/H.png'),
            'i': os.path.abspath('image/I.png'),
            'j': os.path.abspath('image/J.png'),
            'k': os.path.abspath('image/K.png'),
            'l': os.path.abspath('image/L.png'),
            'm': os.path.abspath('image/M.png'),
            'n': os.path.abspath('image/N.png'),
            'o': os.path.abspath('image/O.png'),
            'p': os.path.abspath('image/P.png'),
            'q': os.path.abspath('image/Q.png'),
            'r': os.path.abspath('image/R.png'),
            's': os.path.abspath('image/S.png'),
            't': os.path.abspath('image/T.png'),
            'u': os.path.abspath('image/U.png'),
            'v': os.path.abspath('image/V.png'),
            'w': os.path.abspath('image/W.png'),
            'x': os.path.abspath('image/X.png'),
            'y': os.path.abspath('image/Y.png'),
            'z': os.path.abspath('image/Z.png'),
            
            'A': os.path.abspath('image/A.png'),
            'B': os.path.abspath('image/B.png'),
            'C': os.path.abspath('image/C.png'),
            'D': os.path.abspath('image/D.png'),
            'E': os.path.abspath('image/E.png'),
            'F': os.path.abspath('image/F.png'),
            'G': os.path.abspath('image/G.png'),
            'H': os.path.abspath('image/H.png'),
            'I': os.path.abspath('image/I.png'),
            'J': os.path.abspath('image/J.png'),
            'K': os.path.abspath('image/K.png'),
            'L': os.path.abspath('image/L.png'),
            'M': os.path.abspath('image/M.png'),
            'N': os.path.abspath('image/N.png'),
            'O': os.path.abspath('image/O.png'),
            'P': os.path.abspath('image/P.png'),
            'Q': os.path.abspath('image/Q.png'),
            'R': os.path.abspath('image/R.png'),
            'S': os.path.abspath('image/S.png'),
            'T': os.path.abspath('image/T.png'),
            'U': os.path.abspath('image/U.png'),
            'V': os.path.abspath('image/V.png'),
            'W': os.path.abspath('image/W.png'),
            'X': os.path.abspath('image/X.png'),
            'Y': os.path.abspath('image/Y.png'),
            'Z': os.path.abspath('image/Z.png'),
            
            'Enter': os.path.abspath('image/enter.png'),
            ' ': os.path.abspath('image/Space.png'), 
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

        self.text_to_type = '''There was no point in lingering, especially since I felt overwhelmed - the shock I had experienced affected me, and the whiskey I had drunk made itself felt. Alvin volunteered to accompany me. As we stumbled over the hummocks towards my house, Oln hesitantly said:
- John, I hope you do... how to put it more precisely.. I hope you won't be offended by my brother's lack of restraint.
I mumbled something evasive.
- He didn't throw a grenade at me out of spite, just because he'd had too much.
- Yeah.
- I'm glad you agree with me. I can't even imagine that he was the one who staged the prank in the tavern. I definitely don't question it. Bertie, of course, is a wild fellow, but he is not capable of such a thing.
Isn't Alvin overly protective of his brother? Something in his tone made me suspect that he was trying to convince not only me of Bertie's innocence, but himself as well. My presumption that there was a secret conspiracy between them now seemed to me ridiculous, like the inventions of a sick mind; it quickly disappeared in a quiet wind, which smelled on me the fragrance of dew-moistened grass.'''
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
        return super(Ui_Text_Eng_Window, self).eventFilter(obj, event)

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