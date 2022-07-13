from PySide2.QtCore import Signal, Slot
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QLabel, QTableWidgetItem, QHeaderView, \
    QFileDialog, QMessageBox
from main_ui import Ui_MainWindow
import os
import time
import typing as t
from threading import Thread

import numpy as np
import xlwt

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT

from controller import Controller
from func.graph import MyFigureCanvas
from ip_settings.system_settings import Widget
from sensors import FakeSensor

from scipy.interpolate import make_interp_spline

# from sensor_test import show_result

matplotlib.use("Qt5Agg")  # 声明使用QT5


class Stats(QMainWindow):
    _signal = Signal(list)

    def __init__(self):
        super(Stats, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.func1.setEnabled(False)

        self.marked_x = []
        self.marked_y = []
        self._x_plot = None
        self._y_plot = None
        self._z_plot = None

        self.ptp_distance = None
        self.gv_visual_data_content = MyFigureCanvas(width=self.ui.graphicsView.width() / 101,
                                                     height=self.ui.graphicsView.height() / 101,
                                                     xlim=(-8, 8),
                                                     ylim=(-9, 9))  # 实例化一个FigureCanvas
        self.gv_visual_data_content1 = MyFigureCanvas(width=self.ui.graphicsView_2.width() / 101,
                                                      height=self.ui.graphicsView_2.height() / 101,
                                                      xlim=(-8, 8),
                                                      ylim=(-9, 9))  # 实例化一个FigureCanvas
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene1 = QGraphicsScene()  # 创建一个QGraphicsScene(右边局部)
        self.graphic_scene.addWidget(self.gv_visual_data_content)
        # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.graphic_scene1.addWidget(self.gv_visual_data_content1)

        self.ui.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView_2.setScene(self.graphic_scene1)  # 把QGraphicsScene放入QGraphicsView(右边局部)

        self.ui.graphicsView.show()  # 调用show方法呈现图形
        self.ui.graphicsView_2.show()  # 调用show方法呈现图形
        self.rect = plt.Rectangle((0, 0), 0, 0, color="springgreen", alpha=0.2)  # 选取的范围框
        self.tool = QLabel(self)  # 实例化一个标签，用来作为工具栏的容器
        self.tool.hide()  # 隐藏工具栏
        self.mpl_toolbar = NavigationToolbar2QT(self.gv_visual_data_content, self.tool)  # 实例化工具栏
        self.gv_visual_data_content.toolbar.mode = "zoom rect"  # 将隐藏的画图工具栏的选框放大模式打开
        # self.gv_visual_data_content.mpl_connect('button_release_event', self.release)  # 在原始画布上的鼠标按下事件
        # self.gv_visual_data_content.mpl_connect('button_press_event', self.press)  # 在原始画布上的鼠标释放事件， 该事件绑定了关键操作
        self.xlim = self.gv_visual_data_content.axes.get_xlim()  # 获取原始x轴范围
        self.ylim = self.gv_visual_data_content.axes.get_ylim()  # 获取原始y轴范围

        self.ui.widget_result.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.widget_result.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.widget_result.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        # Icon
        self.ui.func1.setIcon(QIcon('png/func1.png'))
        self.ui.func2.setIcon(QIcon('png/func2.png'))
        self.ui.func3.setIcon(QIcon('png/func3.png'))
        self.ui.func4.setIcon(QIcon('png/func4.png'))
        # Signal
        self.ui.file.clicked.connect(self.file)
        self.ui.func1.clicked.connect(self.pick)
        # self.ui.func2.clicked.connect(self._depth)
        # self.ui.func3.clicked.connect(self._area)
        # self.ui.delete_2.clicked.connect(self.delete)
        # self.ui.save.clicked.connect(self.save)
        self.ui.setting.clicked.connect(self.system_settings)
        # self.ui.back.clicked.connect(self.back)
        self.ui.realtime_monitor.clicked.connect(self.monitor)
        self._signal.connect(self._render_func)
        self.ui.Traking.clicked.connect(self.tracking)

        # self.ui.Traking.setEnabled(False)
        if self.ptp_distance is None:
            self.ui.func1.setEnabled(True)

    @Slot(list)
    def _render_func(self, data_list: t.List[t.List[float]]) -> None:

        self.gv_visual_data_content.axes.cla()
        self.gv_visual_data_content.axes.set_ylim(-8, 8)
        self.gv_visual_data_content.axes.set_xlim(-8, 8)
        data = np.array(data_list)
        print(data_list)

        self.gv_visual_data_content.axes.plot(data[:, 0], data[:, 1])

        self.gv_visual_data_content.draw_idle()

    def show_result(self, data_list: t.List[t.List[float]]) -> None:
        """ Displaying the result list. The input data list has the following format:
            data_list: [
                [x0, y0],
                [x1, y1],
                ...
            ]
        """
        print("The number of data is", len(data_list), ".")
        self._signal.emit(data_list)

    def monitor(self):

        def threadFunc():

            sensor = FakeSensor(
                receiver=self.show_result,
                data_path=r"./profile_1.txt",
                mode="live",
                fps=2
            )

            to_wait: bool = False
            is_waiting: bool = False
            is_notified: bool = False
            start_time = time.time()
            sensor.notify()
            while True:
                if time.time() - start_time <= 5.0:
                    time.sleep(0.05)
                elif not to_wait and not is_waiting:
                    to_wait = True
                elif is_waiting and 7.0 <= time.time() - start_time <= 10.0 and not is_notified:
                    print("Trying to notify...")
                    sensor.notify()
                    is_notified = True
                elif 12.0 < time.time() - start_time:
                    break

                if to_wait:
                    print("Trying to block the thread:")
                    to_wait = False
                    is_waiting = True
                    sensor.wait()

            sensor.exit()

        thread = Thread(target=threadFunc)
        thread.start()
        #
        # """
        #         def update_plot(self):
        #             """
        # filename, _ = QFileDialog.getOpenFileName(self, caption="选择文件", dir=os.getcwd(), filter="(*txt)")
        # mydata = myData(filename)
        # self.x = mydata.x
        # self.y = mydata.y
        # self._plot_ref = None
        # self.i = 1  # cln画法 i= 0
        #
        # self.update_plot()
        # # self.show()
        # self.timer = QTimer()
        # self.timer.setInterval(2)
        # self.timer.timeout.connect(self.update_plot)
        # self.timer.start()
        # self.ui.realtime_monitor.clicked.connect(self.timer.stop)

    def tracking(self):
        pass

    def update_plot(self):
        self.ui.Traking.setEnabled(True)

        """
               Clear and redraw&In-place redraw
               """
        # TODO:
        # self.gv_visual_data_content.axes.cla()
        # self.gv_visual_data_content.axes.set_ylim(-8, 8)
        # self.gv_visual_data_content.axes.set_xlim(-8, 8)
        #
        # self.i += 1
        # self.xdata =self.x[0:self.i]
        # self.ydata =self.y[0:self.i]
        # self.ydata = self.ydata + [random.randint(0, 10)]
        #
        # print(self.xdata, self.ydata)
        # self.gv_visual_data_content.axes.plot(self.xdata,self.ydata)
        # self.gv_visual_data_content.draw_idle()

        # """
        #        以上为Clear and redraw画法
        #        """
        # TODO:

        # self.gv_visual_data_content.axes.set_ylim(-8, 8)
        # self.gv_visual_data_content.axes.set_xlim(-8, 8)
        #
        # self.i += 1
        #
        # if self._plot_ref is None:
        #     self.xdata = self.x[0:1]
        #     self.ydata = self.y[0:1]
        #     plot_refs = self.gv_visual_data_content.axes.plot(self.xdata, self.ydata, 'r')
        #     self._plot_ref = plot_refs[0]
        # else:
        #
        #     self.xdata.append(self.x[self.i])
        #     self.ydata.append(self.y[self.i])
        #     self._plot_ref.set_xdata(self.xdata)
        #     self._plot_ref.set_ydata(self.ydata)
        #
        # self.gv_visual_data_content.draw()
        # """
        #               以上为In-place redraw画法
        #               """

    def file(self):  # 文件读取
        self.gv_visual_data_content.axes.cla()
        self.gv_visual_data_content1.axes.cla()
        filename, _ = QFileDialog.getOpenFileName(self, caption="选择文件", dir=os.getcwd(), filter="(*txt)")
        self.x = Controller.load_file(filename)[0]
        self.y = Controller.load_file(filename)[1]
        self.z = Controller.load_file(filename)[2]
        self.plot_data()

    def system_settings(self):
        self.ss = Widget()
        self.ss.show()

    def plot_data(self):

        # self.gv_visual_data_content.axes.set_ylim(-8, 8)
        # self.gv_visual_data_content.axes.plot3D(self.x, self.y, self.z, ':')
        # # self.gv_visual_data_content.axes.add_patch(self.rect)  # 添加选框范围矩形到画布, 这里需要先初始化一个矩形，后面只需对该矩形矩形参数重设即可让矩形动起来。
        #
        # self.ui.func1.setEnabled(True)
        # self.gv_visual_data_content.draw_idle()

        # def press(self, event):  # 鼠标在原始画布上按下将会被调用的函数，该函数获取鼠标按下的坐标
        #     self.startx = event.x
        #     self.starty = event.x
        #
        # def release(self, event):  # 鼠标在原始画布上释放将会被调用的函数，该函数获取鼠标按下的坐标， 同时处理获取局部图像事务
        #     self.endx = event.x
        #     self.endy = event.x
        #
        #     # 鼠标按下释放后获取选取的矩形范围
        #
        #     self.rect_x = self.gv_visual_data_content.axes.get_xlim()
        #     self.rect_y = self.gv_visual_data_content.axes.get_ylim()
        #
        #     # 如果鼠标按下释放都是同一点，那么此时不出现选择的矩形框（即矩形的起点与宽高都全部设置为0），反之则设置矩形的坐标范围
        #     if self.startx == self.endx and self.starty == self.endy:
        #         self.rect.set_x(0)
        #         self.rect.set_y(0)
        #         self.rect.set_width(0)
        #         self.rect.set_height(0)
        #     else:
        #         self.rect.set_x(self.rect_x[0])
        #         self.rect.set_y(self.rect_y[0])
        #         self.rect.set_width(self.rect_x[1] - self.rect_x[0])
        #         self.rect.set_height(self.rect_y[1] - self.rect_y[0])
        #
        #     # 由于前面选取矩形后，原始图像的坐标轴范围发生了变化，下面代码我们通过将前面存储的原始图像坐标轴范围设置，从而达到恢复原始图像坐标轴的目的，同时保留了选取的矩形框
        #     self.gv_visual_data_content.axes.set_xlim(self.xlim)
        #     self.gv_visual_data_content.axes.set_ylim(self.ylim)
        #     # 我们对原始图像坐标轴约束在选取的矩形坐标范围，即右边局部图像
        #     self.gv_visual_data_content1.axes.cla()
        roi_data = [i for i in zip(self.x, self.y, self.z) if i]
        x, y, z = zip(*roi_data)

        a = Controller.roi_select(x, y, z)
        print(a)
        self.gv_visual_data_content.axes.plot3D(x[477600:550399],y[477600:550399],z[477600:550399], ':')
        self.gv_visual_data_content.draw_idle()
        # if self._x_plot == 'fail' or self._x_plot == ():
        #     QMessageBox.information(self, 'error', '请重新选择')

    #
    #     else:
    #         if miss:
    #
    #             self.gv_visual_data_content1.axes.plot(self._x_plot, self._y_plot)
    #             self.gv_visual_data_content1.draw_idle()
    #         else:
    #             QMessageBox.information(self, 'error', 'roi选择错误')
    #
    #     # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
    #     # 通过列表递推式将选择的矩形范围作为约束条件，对原始数据进行筛选选区数据
    #     # self.data = [i for i in zip(self.x, self.y) if
    #     #              self.rect_x[1] >= i[0] >= self.rect_x[0] and self.rect_y[1] >= i[1] >= self.rect_y[0]]
    #     # print(self.data)

    def pick(self):  # func1

        self.gv_visual_data_content1.axes.scatter(self._x_plot, self._y_plot, picker=2, s=0.001)
        self.gv_visual_data_content1.mpl_connect('pick_event', self._pick)

    def _pick(self, event):
        if self.ui.func1.isEnabled():
            ind = event.ind
            x, y, point_str = Controller.pick_point(self._x_plot, self._y_plot, ind)
            self.marked_x.append(x)
            self.marked_y.append(y)
            self.gv_visual_data_content1.axes.text(x, y, point_str)  # 打印选定数据点
            self.gv_visual_data_content1.axes.plot(x, y, '.r')
            self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用

            self.gv_visual_data_content1.axes.plot(self.marked_x, self.marked_y)
            if len(self.marked_x) > 1:
                self.ptp_distance = Controller.measure_distance(self.marked_x, self.marked_y)
                r = 'd :' + str(self.ptp_distance) + '\n' + '\n'
                self.gv_visual_data_content1.axes.text((self.marked_x[0] + self.marked_x[1]) / 2,
                                                       (self.marked_y[0] + self.marked_y[1]) / 2, r)

        else:
            pass
        if self.ptp_distance is not None:
            self.ui.widget_result.setItem(0, 0, QTableWidgetItem(str(self.marked_x[0]) + ',' + str(self.marked_y[0])))
            self.ui.widget_result.setItem(0, 1, QTableWidgetItem(str(self.marked_x[1]) + ',' + str(self.marked_y[1])))
            self.ui.widget_result.setItem(0, 2, QTableWidgetItem(str(self.ptp_distance)))
        if self.marked_x[1] > self.marked_x[0]:
            bigger_x = self.marked_x[1]
            smaller_x = self.marked_x[0]
        else:
            bigger_x = self.marked_x[0]
            smaller_x = self.marked_x[1]
        if self.marked_y[1] > self.marked_y[0]:
            bigger_y = self.marked_y[1]
        else:
            bigger_y = self.marked_y[0]

        self.marked_data = [i for i in zip(self.x, self.y) if
                            bigger_x >= i[0] >= smaller_x and bigger_y >= i[1] >=
                            -999]
        if self.ptp_distance is not None:
            self.ui.func1.setEnabled(False)
            # a = self.x.index(self.marked_x[0])
            # b = self.x.index(self.marked_x[1])
            #
            # del self.x[a:b]
            # del self.y[a:b]
            # x_smooth = np.linspace(min(self.x), max(self.x), 30000)
            # y_smooth = make_interp_spline(self.x, self.y)(x_smooth)
            # self.gv_visual_data_content.axes.cla()
            # self.gv_visual_data_content.axes.set_ylim(-8, 8)
            # self.gv_visual_data_content.axes.plot(x_smooth, y_smooth)
            # self.gv_visual_data_content.draw_idle()
            # print(self.x) TODO:

    # def _area(self):  # func3
    #     area_data, area_plot = Controller.measure_area(self.marked_x, self.marked_y, self.marked_data)
    #
    #     self.gv_visual_data_content1.axes.text((self.marked_x[0] + self.marked_x[1]) / 2,
    #                                            (self.marked_y[0] + self.marked_y[1] - 0.7) / 2, area_plot)
    #     self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
    #     self.ui.widget_result.setItem(0, 3, QTableWidgetItem(area_data))
    #
    # def _depth(self):
    #     depth_point, drop_foot_x, drop_foot_y, depth_max = Controller.measure_depth(self.marked_x,
    #                                                                                 self.marked_y,
    #                                                                                 self.marked_data,
    #                                                                                 self.ptp_distance)
    #
    #     self.gv_visual_data_content1.axes.plot([depth_point[0], drop_foot_x], [depth_point[1], drop_foot_y])
    #     print(depth_point)
    #     print(drop_foot_x, drop_foot_y)
    #     depth_plot = 'dp :' + str(depth_max)
    #     self.ui.widget_result.setItem(0, 4, QTableWidgetItem(str(depth_max)))
    #     self.gv_visual_data_content1.axes.text((self.marked_x[0] + self.marked_x[1]) / 2,
    #                                            (self.marked_y[0] + self.marked_y[1] - 0.8) / 2, depth_plot)
    #
    #     # self.gv_visual_data_content1.axes.set_aspect(1)
    #
    #     self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
    #
    # def cln_data(self):  # 清空數據
    #
    #     self.marked_x = []
    #     self.marked_y = []
    #     self.ptp_distance = None
    #
    # def delete(self):
    #     self.ui.widget_result.clearContents()
    #     self.gv_visual_data_content1.axes.cla()
    #     self.gv_visual_data_content1.axes.plot(self._x_plot, self._y_plot, )
    #
    #     self.gv_visual_data_content1.draw_idle()
    #     self.cln_data()
    #     if self.ptp_distance is None:
    #         self.ui.func1.setEnabled(True)
    #
    # def save(self):
    #     # TODO:
    #
    #     filenames, _ = QFileDialog.getSaveFileName(self, caption='保存文件', dir='', filter=".xls(*.xls)")
    #     wbk = xlwt.Workbook()
    #     sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
    #     for currentColumn in range(self.ui.widget_result.columnCount()):
    #         for currentRow in range(self.ui.widget_result.rowCount()):
    #             teext = str(self.ui.widget_result.item(currentRow, currentColumn).text())
    #             sheet.write(currentRow, currentColumn, teext)
    #     wbk.save(filenames)
    #
    # def back(self):
    #     if len(self.marked_x) == 2:
    #         del self.marked_x[1]
    #         del self.marked_y[1]
    #
    #         self.ui.widget_result.clearContents()
    #         self.ui.widget_result.setItem(0, 0, QTableWidgetItem(str(self.marked_x[0]) + ',' + str(self.marked_y[0])))
    #         self.gv_visual_data_content1.axes.cla()
    #         self.gv_visual_data_content1.axes.plot(self._x_plot, self._y_plot, )
    #         self.gv_visual_data_content1.axes.plot(self.marked_x[0], self.marked_y[0], '.r')
    #         self.gv_visual_data_content1.axes.text(self.marked_x[0], self.marked_y[0],
    #                                                str(self.marked_x[0]) + '  ' + str(
    #                                                    self.marked_y[0]) + '\n' + '\n')  # 打印选定数据点
    #         self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
    #         self.ptp_distance = None
    #     elif len(self.marked_x) == 1:
    #         del self.marked_x[0]
    #         del self.marked_y[0]
    #         self.ui.widget_result.clearContents()
    #         self.gv_visual_data_content1.axes.cla()
    #
    #         self.gv_visual_data_content1.axes.plot(self._x_plot, self._y_plot, )
    #         self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
    #     if self.ptp_distance is None:
    #         self.ui.func1.setEnabled(True)


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.showMaximized()
    app.exec_()
