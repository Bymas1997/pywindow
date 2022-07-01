from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QGraphicsScene, QTableWidgetItem, QHeaderView, \
    QFileDialog
from PySide2.QtGui import QIcon
from PySide2.QtCore import QTimer, Signal, Slot
from main_ui import Ui_MainWindow
from graph import MyFigureCanvas
import matplotlib
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
import matplotlib.pyplot as plt
import numpy as np
import xlwt
from inspect_func import Inspect_Func

matplotlib.use("Qt5Agg")  # 声明使用QT5


class Stats(QMainWindow):
    _signal = Signal(list)

    def __init__(self):
        super(Stats, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.func1.setEnabled(False)

        self.area_x = []
        self.area_y = []
        self.cu_dataxx = None
        self.cu_datayy = None
        self.marked_x = []
        self.marked_y = []
        self.x = None
        self.y = None
        self.xlim = None  # 用来存储左边原始图像的x坐标轴范围
        self.ylim = None  # 用来存储左边原始图像的y坐标轴范围
        self.distance = None
        inspect_func = Inspect_Func()

        self.ui.widget_result.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.widget_result.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.widget_result.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        # Icon
        self.ui.func1.setIcon(QIcon('png/func1.png'))
        self.ui.func2.setIcon(QIcon('png/func2.png'))
        self.ui.func3.setIcon(QIcon('png/func3.png'))
        self.ui.func4.setIcon(QIcon('png/func4.png'))
        # Signal
        self.ui.file.clicked.connect(Inspect_Func.file)
        self.ui.func1.clicked.connect(self.pick)
        self.ui.func2.clicked.connect(self._depth)
        self.ui.func3.clicked.connect(self._area)
        self.ui.delete_2.clicked.connect(self.delete)
        self.ui.save.clicked.connect(self.save)
        self.ui.setting.clicked.connect(Inspect_Func.system_settings)
        self.ui.back.clicked.connect(self.back)
        self.ui.realtime_monitor.clicked.connect(Inspect_Func.monitor)
        self._signal.connect(Inspect_Func._render_func)

        self.ui.Traking.setEnabled(False)
        # self.ui.Traking.clicked.connect(self.Track)
        if self.distance is None:
            self.ui.func1.setEnabled(True)
        # self._signal.connect(self._render_func)

    def pick(self):  # func1

        self.gv_visual_data_content1.axes.scatter(self.x, self.y, picker=True, s=0.001)
        self.gv_visual_data_content1.mpl_connect('pick_event', self._pick)

    def _pick(self, event):
        if self.ui.func1.isEnabled():
            xx = np.array(self.x)
            yy = np.array(self.y)
            ind = event.ind
            xxx = np.array(xx[ind])
            cu_datax = xxx[1]
            cu_dataxx = np.array(cu_datax)
            yyy = np.array(yy[ind])
            cu_datay = yyy[1]
            cu_datayy = np.array(cu_datay)
            xy1 = (cu_datax, cu_datay)
            print(xy1)  # 打印选定数据
            dataxy = str(cu_datax) + '  ' + str(cu_datay) + '\n' + '\n'  # text函数转换数字类型至字符串打印
            self.gv_visual_data_content1.axes.text(cu_dataxx, cu_datayy, dataxy)  # 打印选定数据点
            self.gv_visual_data_content1.axes.plot(cu_dataxx, cu_datayy, '.r')
            print(cu_dataxx, cu_datayy)
            self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
            self.marked_x.append(cu_dataxx)
            self.marked_y.append(cu_datayy)
            self.gv_visual_data_content1.axes.plot(self.marked_x, self.marked_y)
            self.distance = pow(
                pow(self.marked_x[0] - self.marked_x[1], 2) + pow(self.marked_y[0] - self.marked_y[1], 2), 0.5)
            r = 'd :' + str(self.distance) + '\n' + '\n'
            self.gv_visual_data_content1.axes.text((self.marked_x[0] + self.marked_x[1]) / 2,
                                                   (self.marked_y[0] + self.marked_y[1]) / 2, r)

        else:
            pass
        if self.distance is not None:
            self.ui.widget_result.setItem(0, 0, QTableWidgetItem(str(self.marked_x[0]) + ',' + str(self.marked_y[0])))
            self.ui.widget_result.setItem(0, 1, QTableWidgetItem(str(self.marked_x[1]) + ',' + str(self.marked_y[1])))
            self.ui.widget_result.setItem(0, 2, QTableWidgetItem(str(self.distance)))
        if self.marked_x[1] > self.marked_x[0]:
            bigger_x = self.marked_x[1]
            smaller_x = self.marked_x[0]
        else:
            bigger_x = self.marked_x[0]
            smaller_x = self.marked_x[1]
        if self.marked_y[1] > self.marked_y[0]:
            bigger_y = self.marked_y[1]
            smaller_y = self.marked_y[0]
        else:
            bigger_y = self.marked_y[0]

        self.marked_data = [i for i in zip(self.x, self.y) if
                            bigger_x >= i[0] >= smaller_x and bigger_y >= i[1] >=
                            -999]
        if self.distance is not None:
            self.ui.func1.setEnabled(False)

    def _area(self):  # func3
        for num in self.marked_data:
            self.area_x.append(num[0])
            self.area_y.append(num[1])
        area1 = np.trapz(self.marked_y, x=self.marked_x)
        area2 = np.trapz(self.area_x, x=self.area_y)
        area = area2 - area1
        area_data = str(abs(area))
        area_plot = 's :' + str(abs(area))
        self.gv_visual_data_content1.axes.text((self.marked_x[0] + self.marked_x[1]) / 2,
                                               (self.marked_y[0] + self.marked_y[1] - 0.7) / 2, area_plot)
        self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
        self.ui.widget_result.setItem(0, 3, QTableWidgetItem(area_data))

    def _depth(self):
        p1 = np.array([self.marked_x[0], self.marked_y[0]])
        p2 = np.array([self.marked_x[1], self.marked_y[1]])
        _p1 = p2 - p1
        _p2 = self.marked_data - p1
        cross = np.cross(_p1, _p2)
        cross_norm = np.absolute(cross)
        depth = cross_norm / self.distance
        self.depth_max = max(depth)
        max_depth_index = np.argmax(depth)
        depth_point = self.marked_data[max_depth_index]
        drop_foot_x, drop_foot_y = np.linalg.solve(
            [[self.marked_y[0] - self.marked_y[1], self.marked_x[1] - self.marked_x[0]],
             [-(self.marked_x[1] - self.marked_x[0]) / (self.marked_y[0] - self.marked_y[1]), 1]],
            [self.marked_x[1] * self.marked_y[0] - self.marked_x[0] * self.marked_y[1],
             (-(depth_point[0] * (self.marked_x[1] - self.marked_x[0])) / (self.marked_y[0] - self.marked_y[1])) +
             depth_point[1]])
        self.gv_visual_data_content1.axes.plot([depth_point[0], drop_foot_x], [depth_point[1], drop_foot_y])
        print(depth_point)
        print(drop_foot_x, drop_foot_y)
        depth_plot = 'd :' + str(self.depth_max)
        self.ui.widget_result.setItem(0, 4, QTableWidgetItem(str(self.depth_max)))
        self.gv_visual_data_content1.axes.text((self.marked_x[0] + self.marked_x[1]) / 2,
                                               (self.marked_y[0] + self.marked_y[1] - 0.8) / 2, depth_plot)

        self.gv_visual_data_content1.axes.set_aspect(1)

        self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
        # self.cln_data()

    def cln_data(self):  # 清空數據

        self.marked_x = []
        self.marked_y = []
        self.area_x = []
        self.area_y = []

        # self.xlim = None  # 用来存储左边原始图像的x坐标轴范围
        # self.ylim = None  # 用来存储左边原始图像的y坐标轴范围
        self.distance = None

    def delete(self):
        self.ui.widget_result.clearContents()
        self.gv_visual_data_content1.axes.cla()
        self.gv_visual_data_content1.axes.plot(self.x, self.y)
        self.gv_visual_data_content1.axes.set_xlim(self.rect_x[0], self.rect_x[1])
        self.gv_visual_data_content1.axes.set_ylim(self.rect_y[0], self.rect_y[1])
        self.gv_visual_data_content1.draw_idle()
        self.cln_data()
        if self.distance is None:
            self.ui.func1.setEnabled(True)

    def save(self):

        filenames, _ = QFileDialog.getSaveFileName(self, caption='保存文件', dir='', filter=".xls(*.xls)")
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        for currentColumn in range(self.ui.widget_result.columnCount()):
            for currentRow in range(self.ui.widget_result.rowCount()):
                teext = str(self.ui.widget_result.item(currentRow, currentColumn).text())
                sheet.write(currentRow, currentColumn, teext)
        wbk.save(filenames)

    def back(self):
        if len(self.marked_x) == 2:
            del self.marked_x[1]
            del self.marked_y[1]

            self.ui.widget_result.clearContents()
            self.ui.widget_result.setItem(0, 0, QTableWidgetItem(str(self.marked_x[0]) + ',' + str(self.marked_y[0])))
            self.gv_visual_data_content1.axes.cla()
            self.gv_visual_data_content1.axes.set_xlim(self.rect_x[0], self.rect_x[1])
            self.gv_visual_data_content1.axes.set_ylim(self.rect_y[0], self.rect_y[1])
            self.gv_visual_data_content1.axes.plot(self.x, self.y)
            self.gv_visual_data_content1.axes.plot(self.marked_x[0], self.marked_y[0], '.r')
            self.gv_visual_data_content1.axes.text(self.marked_x[0], self.marked_y[0],
                                                   str(self.marked_x[0]) + '  ' + str(
                                                       self.marked_y[0]) + '\n' + '\n')  # 打印选定数据点
            self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
            self.area_x = []
            self.area_y = []
            self.distance = None
        elif len(self.marked_x) == 1:
            del self.marked_x[0]
            del self.marked_y[0]
            self.ui.widget_result.clearContents()
            self.gv_visual_data_content1.axes.cla()
            self.gv_visual_data_content1.axes.set_xlim(self.rect_x[0], self.rect_x[1])
            self.gv_visual_data_content1.axes.set_ylim(self.rect_y[0], self.rect_y[1])
            self.gv_visual_data_content1.axes.plot(self.x, self.y)
            self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
        if self.distance is None:
            self.ui.func1.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.showMaximized()
    app.exec_()
