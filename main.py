from PySide2.QtWidgets import QApplication, QMessageBox, QPushButton, QMainWindow
from PySide2.QtUiTools import QUiLoader
from main_ui import Ui_MainWindow


class Stats(QMainWindow):

    def __init__(self):
        super(Stats, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.func1.clicked.connect(self.change_text)

    def change_text(self):
        B = self.ui.func2.text()
        self.ui.func1.setText(B)






# class button_click_func(Stats):

#
#     def load(self):

#         print('a')
#
#     def func1(self):
#         print('a')
#
#         QMessageBox.about(self.ui,
#                           '',
#                           f'''func1'''
#                           )

if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.show()
    app.exec_()
