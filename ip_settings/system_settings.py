from PySide2.QtWidgets import QApplication, QWidget
from ip_settings.settings_ui import Ui_Widget


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)



