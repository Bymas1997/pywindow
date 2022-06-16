# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1180, 20, 721, 1021))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inspect_func_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.inspect_func_2.setEnabled(True)
        self.inspect_func_2.setMaximumSize(QtCore.QSize(9999, 90))
        self.inspect_func_2.setObjectName("inspect_func_2")
        self.OK = QtWidgets.QPushButton(self.inspect_func_2)
        self.OK.setGeometry(QtCore.QRect(590, 20, 75, 51))
        self.OK.setObjectName("OK")
        self.func3 = QtWidgets.QPushButton(self.inspect_func_2)
        self.func3.setGeometry(QtCore.QRect(370, 20, 75, 51))
        self.func3.setText("")
        self.func3.setIconSize(QtCore.QSize(75, 51))
        self.func3.setObjectName("func3")
        self.func2 = QtWidgets.QPushButton(self.inspect_func_2)
        self.func2.setGeometry(QtCore.QRect(280, 20, 75, 51))
        self.func2.setText("")
        self.func2.setIconSize(QtCore.QSize(100, 51))
        self.func2.setObjectName("func2")
        self.func4 = QtWidgets.QPushButton(self.inspect_func_2)
        self.func4.setGeometry(QtCore.QRect(470, 20, 75, 51))
        self.func4.setText("")
        self.func4.setIconSize(QtCore.QSize(75, 51))
        self.func4.setObjectName("func4")
        self.func1 = QtWidgets.QPushButton(self.inspect_func_2)
        self.func1.setGeometry(QtCore.QRect(190, 20, 75, 51))
        self.func1.setText("")
        self.func1.setIconSize(QtCore.QSize(75, 100))
        self.func1.setObjectName("func1")
        self.label = QtWidgets.QLabel(self.inspect_func_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.inspect_func_2)
        self.inspect_area = QtWidgets.QGroupBox(self.layoutWidget)
        self.inspect_area.setObjectName("inspect_area")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.inspect_area)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 20, 691, 421))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout.addWidget(self.inspect_area)
        self.result = QtWidgets.QGroupBox(self.layoutWidget)
        self.result.setObjectName("result")
        self.widget_result = QtWidgets.QTableWidget(self.result)
        self.widget_result.setGeometry(QtCore.QRect(20, 30, 691, 381))
        self.widget_result.setObjectName("widget_result")
        self.widget_result.setColumnCount(5)
        self.widget_result.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.widget_result.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_result.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.widget_result.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.widget_result.setItem(0, 0, item)
        self.verticalLayout.addWidget(self.result)
        self.inspect = QtWidgets.QGroupBox(self.centralwidget)
        self.inspect.setGeometry(QtCore.QRect(10, 10, 1151, 1031))
        self.inspect.setObjectName("inspect")
        self.graphicsView = QtWidgets.QGraphicsView(self.inspect)
        self.graphicsView.setGeometry(QtCore.QRect(10, 30, 1131, 941))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setForegroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "试飞/在翼缺陷检测软件"))
        self.inspect_func_2.setTitle(_translate("MainWindow", "测量功能"))
        self.OK.setText(_translate("MainWindow", "选择文件"))
        self.inspect_area.setTitle(_translate("MainWindow", "测量区域"))
        self.result.setTitle(_translate("MainWindow", "结果记录"))
        item = self.widget_result.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.widget_result.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.widget_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Marked_1"))
        item = self.widget_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Marked_2"))
        item = self.widget_result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PTP_Distance"))
        item = self.widget_result.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "area"))
        item = self.widget_result.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Deepth"))
        __sortingEnabled = self.widget_result.isSortingEnabled()
        self.widget_result.setSortingEnabled(False)
        self.widget_result.setSortingEnabled(__sortingEnabled)
        self.inspect.setTitle(_translate("MainWindow", "监测画面"))
        self.menu.setTitle(_translate("MainWindow", "开始监控"))
