# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1180, 20, 721, 1021))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.inspect_func_2 = QGroupBox(self.layoutWidget)
        self.inspect_func_2.setObjectName(u"inspect_func_2")
        self.inspect_func_2.setEnabled(True)
        self.inspect_func_2.setMaximumSize(QSize(9999, 90))
        self.OK = QPushButton(self.inspect_func_2)
        self.OK.setObjectName(u"OK")
        self.OK.setGeometry(QRect(590, 20, 75, 51))
        self.func3 = QPushButton(self.inspect_func_2)
        self.func3.setObjectName(u"func3")
        self.func3.setGeometry(QRect(370, 20, 75, 51))
        self.func3.setIconSize(QSize(75, 51))
        self.func2 = QPushButton(self.inspect_func_2)
        self.func2.setObjectName(u"func2")
        self.func2.setGeometry(QRect(280, 20, 75, 51))
        self.func2.setIconSize(QSize(100, 51))
        self.func4 = QPushButton(self.inspect_func_2)
        self.func4.setObjectName(u"func4")
        self.func4.setGeometry(QRect(470, 20, 75, 51))
        self.func4.setIconSize(QSize(75, 51))
        self.func1 = QPushButton(self.inspect_func_2)
        self.func1.setObjectName(u"func1")
        self.func1.setGeometry(QRect(190, 20, 75, 51))
        self.func1.setIconSize(QSize(75, 100))
        self.label = QLabel(self.inspect_func_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 161, 61))

        self.verticalLayout.addWidget(self.inspect_func_2)

        self.inspect_area = QGroupBox(self.layoutWidget)
        self.inspect_area.setObjectName(u"inspect_area")
        self.graphicsView_2 = QGraphicsView(self.inspect_area)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(20, 20, 691, 421))

        self.verticalLayout.addWidget(self.inspect_area)

        self.result = QGroupBox(self.layoutWidget)
        self.result.setObjectName(u"result")
        self.widget_result = QTableWidget(self.result)
        if (self.widget_result.columnCount() < 5):
            self.widget_result.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.widget_result.rowCount() < 2):
            self.widget_result.setRowCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.widget_result.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.widget_result.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.widget_result.setItem(0, 0, __qtablewidgetitem7)
        self.widget_result.setObjectName(u"widget_result")
        self.widget_result.setGeometry(QRect(20, 30, 691, 381))

        self.verticalLayout.addWidget(self.result)

        self.inspect = QGroupBox(self.centralwidget)
        self.inspect.setObjectName(u"inspect")
        self.inspect.setGeometry(QRect(10, 10, 1151, 1031))
        self.graphicsView = QGraphicsView(self.inspect)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 30, 1131, 941))
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.graphicsView.setForegroundBrush(brush1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8bd5\u98de/\u5728\u7ffc\u7f3a\u9677\u68c0\u6d4b\u8f6f\u4ef6", None))
        self.inspect_func_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u91cf\u529f\u80fd", None))
        self.OK.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.func3.setText("")
        self.func2.setText("")
        self.func4.setText("")
        self.func1.setText("")
        self.label.setText("")
        self.inspect_area.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u91cf\u533a\u57df", None))
        self.result.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u8bb0\u5f55", None))
        ___qtablewidgetitem = self.widget_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Marked_1", None));
        ___qtablewidgetitem1 = self.widget_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Marked_2", None));
        ___qtablewidgetitem2 = self.widget_result.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PTP_Distance", None));
        ___qtablewidgetitem3 = self.widget_result.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"area", None));
        ___qtablewidgetitem4 = self.widget_result.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Deepth", None));
        ___qtablewidgetitem5 = self.widget_result.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem6 = self.widget_result.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.widget_result.isSortingEnabled()
        self.widget_result.setSortingEnabled(False)
        self.widget_result.setSortingEnabled(__sortingEnabled)

        self.inspect.setTitle(QCoreApplication.translate("MainWindow", u"\u76d1\u6d4b\u753b\u9762", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u76d1\u63a7", None))
    # retranslateUi

