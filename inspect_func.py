import os
from PySide2.QtWidgets import QFileDialog
import time
import typing as t
from sensors import FakeSensor
from threading import Thread
from data import myData
from ip_settings.system_settings import Widget
import numpy as np


class Inspect_Func:




    def _render_func(self, data_list: t.List[t.List[float]]) -> None:

        self.gv_visual_data_content.axes.cla()
        self.gv_visual_data_content.axes.set_ylim(-8, 8)
        self.gv_visual_data_content.axes.set_xlim(-8, 8)
        data = np.array(data_list)

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

    # def Track(self):
    #     plot_refs_track = self.gv_visual_data_content1.axes.plot(self.xdata, self.ydata, 'r')
    #     self.plot_refs_track = plot_refs_track[0]
    #
    #     self.tracking_plot()
    #     # self.show()
    #     self.timer_track = QTimer()
    #     self.timer_track.setInterval(2)
    #     self.timer_track.timeout.connect(self.tracking_plot)
    #     self.timer_track.start()
    #     self.ui.Traking.clicked.connect(self.timer_track.stop)
    #
    # def tracking_plot(self):
    #     tracking_xlim = self.xdata[self.i - 2]
    #     if tracking_xlim - 2 <= -8:
    #         self.gv_visual_data_content1.axes.set_xlim(-8, tracking_xlim + 2)
    #
    #     elif tracking_xlim + 2 >= 8:
    #         self.gv_visual_data_content1.axes.set_xlim((tracking_xlim - 2), 8)
    #     elif -6 < tracking_xlim < 6:
    #         self.gv_visual_data_content1.axes.set_xlim(tracking_xlim - 2, tracking_xlim + 2)
    #     tracking_ylim = self.ydata[self.i - 2]
    #     if tracking_ylim - 2 <= -8:
    #         self.gv_visual_data_content1.axes.set_ylim(-8, -6)
    #     elif -6 < tracking_ylim < 6:
    #         self.gv_visual_data_content1.axes.set_ylim(tracking_ylim - 2, tracking_ylim + 2)
    #
    #     self.plot_refs_track.set_xdata(self.xdata)
    #     self.plot_refs_track.set_ydata(self.ydata)
    #     # self.gv_visual_data_content1.axes.cla()
    #
    #     self.gv_visual_data_content1.draw()
    @staticmethod
    def file(self):  # 文件读取

        self.gv_visual_data_content.axes.cla()
        self.gv_visual_data_content1.axes.cla()
        filename, _ = QFileDialog.getOpenFileName(self, caption="选择文件", dir=os.getcwd(), filter="(*txt)")
        mydata = myData(filename)
        self.x = mydata.x
        self.y = mydata.y

        self.plot_data()

    def system_settings(self):
        self.ss = Widget()
        self.ss.show()

    def plot_data(self):

        self.gv_visual_data_content.axes.set_ylim(-8, 8)
        self.gv_visual_data_content1.axes.set_ylim(-8, 8)
        self.gv_visual_data_content.axes.plot(self.x, self.y)
        self.gv_visual_data_content1.axes.plot(self.x, self.y)
        self.gv_visual_data_content.axes.add_patch(self.rect)  # 添加选框范围矩形到画布, 这里需要先初始化一个矩形，后面只需对该矩形矩形参数重设即可让矩形动起来。
        self.xlim = self.gv_visual_data_content.axes.get_xlim()  # 获取原始x轴范围
        self.ylim = self.gv_visual_data_content.axes.get_ylim()  # 获取原始y轴范围
        self.gv_visual_data_content.toolbar.mode = "zoom rect"  # 将隐藏的画图工具栏的选框放大模式打开
        self.gv_visual_data_content.mpl_connect('button_release_event', self.release)  # 在原始画布上的鼠标按下事件
        self.gv_visual_data_content.mpl_connect('button_press_event', self.press)  # 在原始画布上的鼠标释放事件， 该事件绑定了关键操作
        self.ui.func1.setEnabled(True)
        self.gv_visual_data_content.draw_idle()
        self.gv_visual_data_content1.draw_idle()

    def press(self, event):  # 鼠标在原始画布上按下将会被调用的函数，该函数获取鼠标按下的坐标
        self.startx = event.x
        self.starty = event.x

    def release(self, event):  # 鼠标在原始画布上释放将会被调用的函数，该函数获取鼠标按下的坐标， 同时处理获取局部图像事务
        self.endx = event.x
        self.endy = event.x

        # 鼠标按下释放后获取选取的矩形范围

        self.rect_x = self.gv_visual_data_content.axes.get_xlim()
        self.rect_y = self.gv_visual_data_content.axes.get_ylim()

        # 如果鼠标按下释放都是同一点，那么此时不出现选择的矩形框（即矩形的起点与宽高都全部设置为0），反之则设置矩形的坐标范围
        if self.startx == self.endx and self.starty == self.endy:
            self.rect.set_x(0)
            self.rect.set_y(0)
            self.rect.set_width(0)
            self.rect.set_height(0)
        else:
            self.rect.set_x(self.rect_x[0])
            self.rect.set_y(self.rect_y[0])
            self.rect.set_width(self.rect_x[1] - self.rect_x[0])
            self.rect.set_height(self.rect_y[1] - self.rect_y[0])

        # 由于前面选取矩形后，原始图像的坐标轴范围发生了变化，下面代码我们通过将前面存储的原始图像坐标轴范围设置，从而达到恢复原始图像坐标轴的目的，同时保留了选取的矩形框
        self.gv_visual_data_content.axes.set_xlim(self.xlim)
        self.gv_visual_data_content.axes.set_ylim(self.ylim)
        # 我们对原始图像坐标轴约束在选取的矩形坐标范围，即右边局部图像
        self.gv_visual_data_content1.axes.set_xlim(self.rect_x[0], self.rect_x[1])
        self.gv_visual_data_content1.axes.set_ylim(self.rect_y[0], self.rect_y[1])
        self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
        # 通过列表递推式将选择的矩形范围作为约束条件，对原始数据进行筛选选区数据
        self.data = [i for i in zip(self.x, self.y) if
                     self.rect_x[1] >= i[0] >= self.rect_x[0] and self.rect_y[1] >= i[1] >= self.rect_y[0]]
        print(self.data)
