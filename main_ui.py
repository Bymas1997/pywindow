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
        MainWindow.resize(925, 713)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.inspect = QGroupBox(self.centralwidget)
        self.inspect.setObjectName(u"inspect")
        self.graphicsView = QGraphicsView(self.inspect)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 20, 411, 281))
        brush = QBrush(QColor(42, 207, 196, 255))
        brush.setStyle(Qt.SolidPattern)
        self.graphicsView.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.Dense5Pattern)
        self.graphicsView.setForegroundBrush(brush1)

        self.horizontalLayout_2.addWidget(self.inspect)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inspect_func = QGroupBox(self.centralwidget)
        self.inspect_func.setObjectName(u"inspect_func")
        self.inspect_func.setMaximumSize(QSize(9999, 65))
        self.verticalLayout_2 = QVBoxLayout(self.inspect_func)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 8, 5, -1)
        self.fun_frame = QFrame(self.inspect_func)
        self.fun_frame.setObjectName(u"fun_frame")
        self.fun_frame.setMaximumSize(QSize(339, 35))
        self.horizontalLayout = QHBoxLayout(self.fun_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 2, 9, 9)
        self.func1 = QPushButton(self.fun_frame)
        self.func1.setObjectName(u"func1")

        self.horizontalLayout.addWidget(self.func1)

        self.func3 = QPushButton(self.fun_frame)
        self.func3.setObjectName(u"func3")

        self.horizontalLayout.addWidget(self.func3)

        self.func2 = QPushButton(self.fun_frame)
        self.func2.setObjectName(u"func2")

        self.horizontalLayout.addWidget(self.func2)

        self.func4 = QPushButton(self.fun_frame)
        self.func4.setObjectName(u"func4")

        self.horizontalLayout.addWidget(self.func4)


        self.verticalLayout_2.addWidget(self.fun_frame)


        self.verticalLayout.addWidget(self.inspect_func)

        self.inspect_area = QGroupBox(self.centralwidget)
        self.inspect_area.setObjectName(u"inspect_area")

        self.verticalLayout.addWidget(self.inspect_area)

        self.result = QGroupBox(self.centralwidget)
        self.result.setObjectName(u"result")
        self.widget_result = QTableWidget(self.result)
        if (self.widget_result.columnCount() < 4):
            self.widget_result.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.widget_result.rowCount() < 2):
            self.widget_result.setRowCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.widget_result.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.widget_result.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.widget_result.setItem(0, 0, __qtablewidgetitem6)
        self.widget_result.setObjectName(u"widget_result")
        self.widget_result.setGeometry(QRect(10, 20, 411, 211))

        self.verticalLayout.addWidget(self.result)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.inspect.setTitle(QCoreApplication.translate("MainWindow", u"\u76d1\u6d4b\u753b\u9762", None))
        self.inspect_func.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u91cf\u529f\u80fd", None))
        self.func1.setText(QCoreApplication.translate("MainWindow", u"Button1", None))
        self.func3.setText(QCoreApplication.translate("MainWindow", u"Button3", None))
        self.func2.setText(QCoreApplication.translate("MainWindow", u"Button2", None))
        self.func4.setText(QCoreApplication.translate("MainWindow", u"Button4", None))
        self.inspect_area.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u91cf\u533a\u57df", None))
        self.result.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u8bb0\u5f55", None))
        ___qtablewidgetitem = self.widget_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem1 = self.widget_result.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.widget_result.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));

        __sortingEnabled = self.widget_result.isSortingEnabled()
        self.widget_result.setSortingEnabled(False)
        self.widget_result.setSortingEnabled(__sortingEnabled)

        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u76d1\u63a7", None))
    # retranslateUi

