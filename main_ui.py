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
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 70, 1141, 931))
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.graphicsView.setForegroundBrush(brush1)
        self.widget_result = QTableWidget(self.centralwidget)
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
        self.widget_result.setGeometry(QRect(1190, 660, 691, 381))
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(1180, 70, 701, 561))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 0, 601, 77))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.realtime_monitor = QPushButton(self.layoutWidget)
        self.realtime_monitor.setObjectName(u"realtime_monitor")
        self.realtime_monitor.setMinimumSize(QSize(75, 51))

        self.horizontalLayout.addWidget(self.realtime_monitor)

        self.file = QPushButton(self.layoutWidget)
        self.file.setObjectName(u"file")
        self.file.setMinimumSize(QSize(75, 51))

        self.horizontalLayout.addWidget(self.file)

        self.Traking = QPushButton(self.layoutWidget)
        self.Traking.setObjectName(u"Traking")
        self.Traking.setMinimumSize(QSize(75, 51))

        self.horizontalLayout.addWidget(self.Traking)

        self.setting = QPushButton(self.layoutWidget)
        self.setting.setObjectName(u"setting")
        self.setting.setMinimumSize(QSize(75, 51))

        self.horizontalLayout.addWidget(self.setting)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1210, 10, 361, 53))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.func1 = QPushButton(self.layoutWidget1)
        self.func1.setObjectName(u"func1")
        self.func1.setMinimumSize(QSize(75, 51))
        self.func1.setIconSize(QSize(75, 100))

        self.horizontalLayout_2.addWidget(self.func1)

        self.func3 = QPushButton(self.layoutWidget1)
        self.func3.setObjectName(u"func3")
        self.func3.setMinimumSize(QSize(75, 51))
        self.func3.setIconSize(QSize(75, 51))

        self.horizontalLayout_2.addWidget(self.func3)

        self.func2 = QPushButton(self.layoutWidget1)
        self.func2.setObjectName(u"func2")
        self.func2.setMinimumSize(QSize(75, 51))
        self.func2.setIconSize(QSize(100, 51))

        self.horizontalLayout_2.addWidget(self.func2)

        self.func4 = QPushButton(self.layoutWidget1)
        self.func4.setObjectName(u"func4")
        self.func4.setMinimumSize(QSize(75, 51))
        self.func4.setIconSize(QSize(75, 51))

        self.horizontalLayout_2.addWidget(self.func4)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(1610, 10, 239, 53))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.back = QPushButton(self.layoutWidget2)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(75, 51))
        self.back.setIconSize(QSize(75, 51))

        self.horizontalLayout_3.addWidget(self.back)

        self.save = QPushButton(self.layoutWidget2)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(75, 51))
        self.save.setIconSize(QSize(75, 51))

        self.horizontalLayout_3.addWidget(self.save)

        self.delete_2 = QPushButton(self.layoutWidget2)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setMinimumSize(QSize(75, 51))
        self.delete_2.setIconSize(QSize(75, 51))

        self.horizontalLayout_3.addWidget(self.delete_2)

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

        self.realtime_monitor.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u76d1\u6d4b", None))
        self.file.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bfb\u53d6", None))
        self.Traking.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u8e2a\u6a21\u5f0f", None))
        self.setting.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.func1.setText("")
        self.func3.setText("")
        self.func2.setText("")
        self.func4.setText("")
        self.back.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u76d1\u63a7", None))
    # retranslateUi

