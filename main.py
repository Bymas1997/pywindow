from PySide2.QtWidgets import QApplication, QMessageBox, QPushButton
from PySide2.QtUiTools import QUiLoader


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('main.ui')

        # self.ui.func1.clicked.connect(self.func1)

    # def func1(self):
    #     print('a')
    #     QMessageBox.about(self.ui,
    #                       '',
    #                       f'''func1'''
    #                       )


class button_click_func(Stats):

    def load(self):
        QPushButton.click()
        print('a')

    def func1(self):
        print('a')

        QMessageBox.about(self.ui,
                          '',
                          f'''func1'''
                          )


app = QApplication([])
stats = Stats()
stats.ui.show()
Button_click_func = button_click_func()
Button_click_func.load()
app.exec_()
