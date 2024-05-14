from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import time
from path_fon import get_fon

class Ui_Text_Ru_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.is_exercise_completed = False
        
        self.Fon = QtWidgets.QLabel(self.centralwidget)
        self.Fon.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.Fon.setText("")
        self.Fon.setPixmap(QtGui.QPixmap(get_fon()))
        self.Fon.setScaledContents(True)
        self.Fon.setObjectName("Fon")
        
        self.P_Fon = QtWidgets.QLabel(self.centralwidget)
        self.P_Fon.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.P_Fon.setText("")
        self.P_Fon.setObjectName("P_Fon")
        
        self.Text = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(200, 150, 1500, 400))
        self.Text.setStyleSheet("background-color: rgb(140, 140, 140);")
        self.Text.setObjectName("Text")
        
        self.VvodTexta = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.VvodTexta.setGeometry(QtCore.QRect(200, 600, 1500, 300))
        self.VvodTexta.setObjectName("VvodTexta")
        self.VvodTexta.textChanged.connect(self.handle_text_changed)
        
        self.KartinkaKlavish = QtWidgets.QLabel(self.centralwidget)
        self.KartinkaKlavish.setGeometry(QtCore.QRect(74, 395, 671, 111))
        self.KartinkaKlavish.setObjectName("KartinkaKlavish")
        
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

        self.text_to_type = '''Задерживаться не имело смысла, тем более что я чувствовал себя разбитым - сказывалось пережитое потрясение, да и выпитое виски давало о себе знать. Элвин вызвался проводить меня. Когда мы, спотыкаясь о кочки, брели к моему дому, олн нерешительно произнес:
- Джон, надкеюсь вы... как бы поточнее сказать.. надеюсь, вы не обидитесь на моего брата за его несдержанность.
Я проборомтал что-то уклончивое.
- Он запустил в меня гранатой не по злобе, просто потому что перебрал.
- Угу.
- Я рад, что вы со мной согласны. Не допускаю даже и мысли, что это он устроил розыгрыш в таверне. Решительно не допсукаю. Берти, конечно, малый необузданный, но на такое не способен.
Не слишком ли рьяно защищает Элвин своего брата? Что-то в его тоне наводило меня на подозрение, что он пытается убедить в невинности Берти не только меня, но и себя самого. Мое предполжение, будто между ними существует тайный заговор, казалось мне теперь нелепым, как измышления больного ума; оно быстро улетучилось на тихом ветру, который пахнул на меня благоуханием увлажненной росой травы.'''
        self.Text.setStyleSheet("background-color: rgb(200, 200, 200); font-size: 15pt;")
        self.Text.setText(self.text_to_type)
        self.current_index = 0
        self.update_keyboard_image()
        self.VvodTexta.setFocus()
        self.VvodTexta.installEventFilter(self.VvodTexta)
        
        self.start_time = None
        self.total_errors = 0
        self.total_characters = 0
        self.Text.setText(self.text_to_type)
        self.current_index = 0
        self.update_keyboard_image()
        self.VvodTexta.setFocus()
        
        self.MenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.MenuButton.setGeometry(QtCore.QRect(1100, 950, 200, 100))
        self.MenuButton.setObjectName("mainMenuButton")
        self.MenuButton.setText("В главное меню")

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setGeometry(QtCore.QRect(550, 950, 200, 100))
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.mainMenuButton.setText("Пауза")
        self.mainMenuButton.clicked.connect(self.Pause)
        self.is_paused = False

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.endExerciseButton = QtWidgets.QPushButton(self.centralwidget)
        self.endExerciseButton.setGeometry(QtCore.QRect(840, 950, 200, 100))
        self.endExerciseButton.setObjectName("endExerciseButton")
        self.endExerciseButton.setText("Завершить упражнение")
        self.endExerciseButton.clicked.connect(self.end_exercise)

        MainWindow.setCentralWidget(self.centralwidget)
        
    def end_exercise(self):
        if not self.is_exercise_completed:
            self.display_results()  # Показываем результаты
            self.is_exercise_completed = True
            self.VvodTexta.setReadOnly(True)  # Блокируем ввод текста
            self.mainMenuButton.setEnabled(False)  # Деактивируем кнопку "Пауза"
            self.endExerciseButton.setEnabled(False)  # Деактивируем кнопку "Завершить упражнение
        
    def Pause(self):
        if self.is_exercise_completed:
            return  # Если упражнение завершено, не выполняем никаких действий

        if self.is_paused:
            self.is_paused = False
            self.VvodTexta.setReadOnly(False)  # Разрешаем ввод текста
            self.mainMenuButton.setText("Пауза")
        else:
            self.is_paused = True
            self.VvodTexta.setReadOnly(True)  # Запрещаем ввод текста
            self.mainMenuButton.setText("Продолжить")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typing Tutor"))
        self.KartinkaKlavish.setText(_translate("MainWindow", "TextLabel"))

    def handle_text_changed(self):
        if self.is_paused or self.is_exercise_completed:
            return  # Прекращаем обработку, если приложение на паузе или упражнение завершено

        input_text = self.VvodTexta.toPlainText()
        if self.start_time is None and not self.is_paused:
            self.start_time = time.time()  # Засекаем время начала ввода

        if input_text == self.text_to_type[:len(input_text)]:
            # Ввод правильный
            self.VvodTexta.setStyleSheet("background-color: lightgreen;")
            self.current_index = len(input_text)
            if len(input_text) == len(self.text_to_type):
                self.display_results()
        else:
            # Ввод неправильный
            self.VvodTexta.setStyleSheet("background-color: pink;")
            self.total_errors += 1
            
        if len(input_text) > len(self.text_to_type):
            # Ограничение ввода длиной заданного текста
            self.VvodTexta.setPlainText(self.text_to_type)
            self.VvodTexta.moveCursor(QtGui.QTextCursor.End)
            
    def display_results(self):
        if self.start_time is None:
            # Если время начала не установлено, мы не можем рассчитать продолжительность упражнения
            QMessageBox.warning(None, "Ошибка", "Невозможно отобразить результаты: Вы не начали писать. Попробуйте заново! Напишите что-нибудь и затем завершайте упражнение!")
            return

        elapsed_time = time.time() - self.start_time
        input_text = self.VvodTexta.toPlainText().replace(" ", "")
        accuracy = ((len(input_text) - self.total_errors) / len(self.text_to_type)) * 100
        self.Text.setText(f"Вы закончили упражнение! \nВремя: {elapsed_time:.2f} секунд\nПроцент точности: {accuracy:.2f}%\nВведено знаков: {len(input_text)}")
        self.Text.setStyleSheet("background-color: rgb(200, 200, 200); font-size: 15pt;")
        self.is_exercise_completed = True
        self.VvodTexta.setReadOnly(True)  # Блокировка дальнейшего ввода
        self.mainMenuButton.setEnabled(False)  # Деактивируем кнопку "Пауза"
        self.endExerciseButton.setEnabled(False)  # Деактивируем кнопку "Завершить упражнение"
        
    def update_keyboard_image(self):
        if self.current_index < len(self.text_to_type):
            next_char = self.text_to_type[self.current_index].lower()
            pixmap_path = f"keyboard/{next_char}.png"
            self.KartinkaKlavish.setPixmap(QtGui.QPixmap(pixmap_path))
        self.KartinkaKlavish.show()