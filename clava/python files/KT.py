from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QStackedWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import sys
from Main_Menu import Ui_MainWindow
from Settings import Ui_Settings_Window
from Levels import Ui_Third_Window
from Letters_Ru import Ui_Letters_Ru
from Letters_Eng import Ui_Letters_Eng
from Punctuation_Marks import Ui_Punctuation_Marks_window
from Words_Ru import Ui_Words_Ru_Window
from Words_Eng import Ui_Words_Eng_Window
from Clause_Ru import Ui_Clause_Ru_Window
from Clause_Eng import Ui_Clause_Eng_Window
from Text_Eng import Ui_Text_Eng_Window
from Text_Ru import Ui_Text_Ru_Window

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("6e255b4b6b8375e.mp3")))
        self.player.play()

        # Для управления переключением окон
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.showFullScreen()

        self.main_window = QMainWindow()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self.main_window)
        
        self.second_window = QMainWindow() 
        self.ui_settings = Ui_Settings_Window()
        self.ui_settings.setupUi(self.second_window)
        self.ui_settings.BFon_3.clicked.connect(self.toggleFullScreen)
        self.ui_settings.stacked_widget = self.stacked_widget
        self.ui_settings.main_window = self.main_window
        exerciseWindow = Ui_Punctuation_Marks_window()

        self.third_window = QMainWindow()
        self.ui_levels = Ui_Third_Window()
        self.ui_levels.setupUi(self.third_window)
        self.ui_levels.ButtonNazad.clicked.connect(self.showMainWindow) 
        self.ui_levels.Bukva.clicked.connect(self.showLettersRuWindow)
        self.ui_levels.Bukva_2.clicked.connect(self.showLettersEngWindow)
        self.ui_levels.Mark.clicked.connect(self.showMarks)
        self.ui_levels.Slova.clicked.connect(self.showWordsRuWindow)
        self.ui_levels.Slova_2.clicked.connect(self.showWordsEngWindow)
        self.ui_levels.Predloshenia.clicked.connect(self.showClauseRuWindow)
        self.ui_levels.Predloshenia_Eng.clicked.connect(self.showClauseEngWindow)
        self.ui_levels.Text_2.clicked.connect(self.showTextEngWindow)
        self.ui_levels.Text.clicked.connect(self.showTextRuWindow)

        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.addWidget(self.second_window)
        self.stacked_widget.addWidget(self.third_window)

        self.ui_main.Settings.clicked.connect(self.showSecondWindow)
        self.ui_main.Exit.clicked.connect(self.exit_app)
        self.ui_main.Ruls.clicked.connect(self.show_rules)
        self.ui_main.Play.clicked.connect(self.showThirdWindow)
        self.ui_settings.BFon_2.clicked.connect(self.toggle_music)
        
    def showLettersRuWindow(self):
        self.letters_ru_window = QMainWindow()
        self.ui_letters_ru = Ui_Letters_Ru()
        self.ui_letters_ru.setupUi(self.letters_ru_window)
        self.ui_letters_ru.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.letters_ru_window)
        self.stacked_widget.setCurrentWidget(self.letters_ru_window)
        self.letters_ru_window.showFullScreen()
        
    def showLettersEngWindow(self):
        self.letters_eng_window = QMainWindow()
        self.ui_letters_eng = Ui_Letters_Eng()
        self.ui_letters_eng.setupUi(self.letters_eng_window)
        self.ui_letters_eng.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.letters_eng_window)
        self.stacked_widget.setCurrentWidget(self.letters_eng_window)
        self.letters_eng_window.showFullScreen()
        
    def showMarks(self):
        self.marks_window = QMainWindow()
        self.ui_marks = Ui_Punctuation_Marks_window()
        self.ui_marks.setupUi(self.marks_window)
        self.ui_marks.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.marks_window)
        self.stacked_widget.setCurrentWidget(self.marks_window)
        self.marks_window.showFullScreen()
        
    def showWordsRuWindow(self):
        self.words_ru_window = QMainWindow()
        self.ui_words_ru = Ui_Words_Ru_Window()
        self.ui_words_ru.setupUi(self.words_ru_window)
        self.ui_words_ru.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.words_ru_window)
        self.stacked_widget.setCurrentWidget(self.words_ru_window)
        self.words_ru_window.showFullScreen()
        
    def showWordsEngWindow(self):
        self.words_eng_window = QMainWindow()
        self.ui_words_eng = Ui_Words_Eng_Window()
        self.ui_words_eng.setupUi(self.words_eng_window)
        self.ui_words_eng.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.words_eng_window)
        self.stacked_widget.setCurrentWidget(self.words_eng_window)
        self.words_eng_window.showFullScreen()
        
    def showClauseRuWindow(self):
        self.clause_ru_window = QMainWindow()
        self.ui_clause_ru = Ui_Clause_Ru_Window()
        self.ui_clause_ru.setupUi(self.clause_ru_window)
        self.ui_clause_ru.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.clause_ru_window)
        self.stacked_widget.setCurrentWidget(self.clause_ru_window)
        self.clause_ru_window.showFullScreen()
        
    def showClauseEngWindow(self):
        self.clause_eng_window = QMainWindow()
        self.ui_clause_eng = Ui_Clause_Eng_Window()
        self.ui_clause_eng.setupUi(self.clause_eng_window)
        self.ui_clause_eng.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.clause_eng_window)
        self.stacked_widget.setCurrentWidget(self.clause_eng_window)
        self.clause_eng_window.showFullScreen()
        
    def showTextRuWindow(self):
        self.text_ru_window = QMainWindow()
        self.ui_text_ru = Ui_Text_Ru_Window()
        self.ui_text_ru.setupUi(self.text_ru_window)
        self.ui_text_ru.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.text_ru_window)
        self.stacked_widget.setCurrentWidget(self.text_ru_window)
        self.text_ru_window.showFullScreen()
        
    def showTextEngWindow(self):
        self.text_eng_window = QMainWindow()
        self.ui_text_eng = Ui_Text_Eng_Window()
        self.ui_text_eng.setupUi(self.text_eng_window)
        self.ui_text_eng.MenuButton.clicked.connect(self.showMainWindow)
        self.stacked_widget.addWidget(self.text_eng_window)
        self.stacked_widget.setCurrentWidget(self.text_eng_window)
        self.text_eng_window.showFullScreen()
        
    def showMainWindow(self):
        self.stacked_widget.setCurrentWidget(self.main_window)
        self.main_window.showFullScreen()

    def showSecondWindow(self):
        self.stacked_widget.setCurrentWidget(self.second_window)
        self.second_window.showFullScreen()
        
    def showThirdWindow(self):
        self.stacked_widget.setCurrentWidget(self.third_window)
        self.third_window.showFullScreen()
        
    def toggleFullScreen(self):
        if self.isFullScreen():
            self.showMaximized()
        else:
            self.showFullScreen()
            
    def toggle_music(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.stop()
        else:
            self.player.play()
    
    def show_rules(self):
        rules = QMessageBox()
        rules.setWindowTitle('Правила')
        rules.setText('''1. Изначальное расположение пальцев: левая рука должна управлять клавишами A, S, D, F (и пробелом), а правая рука - клавишами J, K, L, ; (и Enter).
2. На экране Вы увидите буквы, словосочетания и текст, нужно будет прописывать их с помощью клавиатуры.
3. После прохождения первого уровня Вы освоите печать букв и можно переходить к более сложным уровням.
4. Введенный вами текст можно стирать и исправлять!''')
        rules.setIcon(QMessageBox.Information)
        rules.setStandardButtons(QMessageBox.Ok)
        rules.exec_()

    def exit_app(self):
        QApplication.quit()
        
def main():
    app = QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()