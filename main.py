import os
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QGraphicsScene, QTableWidgetItem, QHeaderView, \
    QFileDialog
from PySide2.QtGui import QIcon

from main_ui import Ui_MainWindow
from graph import MyFigureCanvas
import matplotlib
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
import matplotlib.pyplot as plt
from data import myData
import numpy as np

matplotlib.use("Qt5Agg")  # 声明使用QT5


class Stats(QMainWindow):

    def __init__(self):
        super(Stats, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.distance = []

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
        self.rect = plt.Rectangle((0, 0), 0, 0, color="springgreen", alpha=0.2)  # 选取的范围框
        self.tool = QLabel(self)  # 实例化一个标签，用来作为工具栏的容器
        self.tool.hide()  # 隐藏工具栏
        self.mpl_toolbar = NavigationToolbar2QT(self.gv_visual_data_content, self.tool)  # 实例化工具栏
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
        self.ui.func2.clicked.connect(self._depth)
        self.ui.func3.clicked.connect(self._area)
        self.ui.delete_2.clicked.connect(self.delete)
        self.ui.save.clicked.connect(self.save)

    def file(self):  # 文件读取
        self.gv_visual_data_content.axes.cla()
        self.gv_visual_data_content1.axes.cla()
        filename, _ = QFileDialog.getOpenFileName(self, caption="选择文件", dir=os.getcwd(), filter="(*txt)")
        print(filename)
        mydata = myData(filename)
        self.x = mydata.x
        self.y = mydata.y

        self.plot_data()

    def plot_data(self):

        self.gv_visual_data_content.axes.set_ylim(-8, 8)
        self.gv_visual_data_content1.axes.set_ylim(-8, 8)

        self.gv_visual_data_content.axes.plot(self.x, self.y)
        self.gv_visual_data_content.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用

        self.gv_visual_data_content1.axes.plot(self.x, self.y)
        self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用

        self.gv_visual_data_content.axes.add_patch(self.rect)  # 添加选框范围矩形到画布, 这里需要先初始化一个矩形，后面只需对该矩形矩形参数重设即可让矩形动起来。
        self.xlim = self.gv_visual_data_content.axes.get_xlim()  # 获取原始x轴范围
        self.ylim = self.gv_visual_data_content.axes.get_ylim()  # 获取原始y轴范围
        self.gv_visual_data_content.axes.set_title('')
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene.addWidget(self.gv_visual_data_content)
        # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.graphic_scene1.addWidget(self.gv_visual_data_content1)

        self.ui.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView_2.setScene(self.graphic_scene1)  # 把QGraphicsScene放入QGraphicsView(右边局部)

        self.ui.graphicsView.show()  # 调用show方法呈现图形
        self.ui.graphicsView_2.show()  # 调用show方法呈现图形
        self.gv_visual_data_content.toolbar.mode = "zoom rect"  # 将隐藏的画图工具栏的选框放大模式打开
        self.gv_visual_data_content.mpl_connect('button_release_event', self.release)  # 在原始画布上的鼠标按下事件
        self.gv_visual_data_content.mpl_connect('button_press_event', self.press)  # 在原始画布上的鼠标释放事件， 该事件绑定了关键操作
        self.ui.func1.setEnabled(True)

    def press(self, event):  # 鼠标在原始画布上按下将会被调用的函数，该函数获取鼠标按下的坐标
        self.startx = event.x
        self.starty = event.x

    def release(self, event):  # 鼠标在原始画布上释放将会被调用的函数，该函数获取鼠标按下的坐标， 同时处理获取局部图像事务
        self.endx = event.x
        self.endy = event.x

        # 鼠标按下释放后获取选取的矩形范围

        x = self.gv_visual_data_content.axes.get_xlim()
        # print(x)
        y = self.gv_visual_data_content.axes.get_ylim()
        # print(y)

        # 如果鼠标按下释放都是同一点，那么此时不出现选择的矩形框（即矩形的起点与宽高都全部设置为0），反之则设置矩形的坐标范围
        if self.startx == self.endx and self.starty == self.endy:
            self.rect.set_x(0)
            self.rect.set_y(0)
            self.rect.set_width(0)
            self.rect.set_height(0)
        else:
            self.rect.set_x(x[0])
            self.rect.set_y(y[0])
            self.rect.set_width(x[1] - x[0])
            self.rect.set_height(y[1] - y[0])

        # 由于前面选取矩形后，原始图像的坐标轴范围发生了变化，下面代码我们通过将前面存储的原始图像坐标轴范围设置，从而达到恢复原始图像坐标轴的目的，同时保留了选取的矩形框
        self.gv_visual_data_content.axes.set_xlim(self.xlim)
        self.gv_visual_data_content.axes.set_ylim(self.ylim)
        # 我们对原始图像坐标轴约束在选取的矩形坐标范围，即右边局部图像
        self.gv_visual_data_content1.axes.set_xlim(x[0], x[1])
        self.gv_visual_data_content1.axes.set_ylim(y[0], y[1])
        self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
        # 通过列表递推式将选择的矩形范围作为约束条件，对原始数据进行筛选选区数据
        self.data = [i for i in zip(self.x, self.y) if x[1] >= i[0] >= x[0] and y[1] >= i[1] >= y[0]]

    def pick(self):  # func1

        self.gv_visual_data_content1.axes.scatter(self.x, self.y, picker=True, s=0.001)
        self.gv_visual_data_content1.mpl_connect('pick_event', self._pick)

    def _pick(self, event):
        if self.ui.func1.isEnabled():
            xx = np.array(self.x)
            yy = np.array(self.y)
            ind = event.ind
            xxx = np.array(xx[ind])
            cu_datax = xxx[0]
            self.cu_dataxx = np.array(cu_datax)
            yyy = np.array(yy[ind])
            cu_datay = yyy[1]
            self.cu_datayy = np.array(cu_datay)
            xy1 = (cu_datax, cu_datay)
            print(xy1)  # 打印选定数据
            dataxy = str(cu_datax) + '  ' + str(cu_datay) + '\n' + '\n'  # text函数转换数字类型至字符串打印
            self.gv_visual_data_content1.axes.text(self.cu_dataxx, self.cu_datayy, dataxy)  # 打印选定数据点
            self.gv_visual_data_content1.axes.plot(self.cu_dataxx, self.cu_datayy, '.r')
            self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
            self.marked_x.append(self.cu_dataxx)
            self.marked_y.append(self.cu_datayy)
            self.gv_visual_data_content1.axes.plot(self.marked_x, self.marked_y)
            self.distance = pow(
                pow(self.marked_x[0] - self.marked_x[1], 2) + pow(self.marked_y[0] - self.marked_y[1], 2), 0.5)
            print(self.distance)
            r = 'd :' + str(self.distance) + '\n' + '\n'
            self.gv_visual_data_content1.axes.text((self.marked_x[0] + self.marked_x[1]) / 2,
                                                   (self.marked_y[0] + self.marked_y[1]) / 2, r)
        else:
            pass
        if self.distance is not None:
            self.ui.widget_result.item(0, 0).setText(str(self.marked_x[0]) + ',' + str(self.marked_y[0]))
            self.ui.widget_result.setItem(0, 1, QTableWidgetItem(str(self.marked_x[1]) + ',' + str(self.marked_y[1])))
            self.ui.widget_result.setItem(0, 2, QTableWidgetItem(str(self.distance)))

    def _area(self):  # func3
        print(self.marked_x)
        self.area = [i for i in zip(self.x, self.y) if self.marked_x[1] >= i[0] >= self.marked_x[0]]
        for num in self.area:
            self.area_x.append(num[0])
            self.area_y.append(num[1])
        self.area1 = np.trapz(self.marked_y, x=self.marked_x)
        print(self.area1)
        self.area2 = np.trapz(self.area_x, x=self.area_y)
        print(self.area2)
        area = self.area2 - self.area1
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
        self.area = np.array([i for i in zip(self.x, self.y) if self.marked_x[1] >= i[0] >= self.marked_x[0]])
        _p2 = self.area - p1
        cross = np.cross(_p1, _p2)
        cross_norm = np.absolute(cross)
        depth = cross_norm / self.distance
        print(depth)
        self.depth_max = max(depth)
        depth_plot = 'd :' + str(self.depth_max)
        self.ui.widget_result.setItem(0, 4, QTableWidgetItem(str(self.depth_max)))
        self.gv_visual_data_content1.axes.text((self.marked_x[0] + self.marked_x[1]) / 2,
                                               (self.marked_y[0] + self.marked_y[1] - 0.8) / 2, depth_plot)
        self.gv_visual_data_content1.draw_idle()  # 此行代码至关重要，若没有改行代码，右边图像将无法随矩形选区更新，改行代码起实时更新作用
        self.cln_data()

    def cln_data(self):  # 清空數據
        self.cu_dataxx = None  # def pink
        self.cu_datayy = None
        self.marked_x = []
        self.marked_y = []
        self.area_x = []
        self.area_y = []
        self.cu_dataxx = None
        self.cu_datayy = None
        self.marked_x = []
        self.marked_y = []
        self.xlim = None  # 用来存储左边原始图像的x坐标轴范围
        self.ylim = None  # 用来存储左边原始图像的y坐标轴范围
        self.distance = []

    def delete(self):
        self.ui.widget_result.clearContents()
        self.gv_visual_data_content1.axes.cla()
        self.gv_visual_data_content1.axes.plot(self.x, self.y)
        self.gv_visual_data_content1.axes.set_ylim(-8, 8)
        self.gv_visual_data_content1.draw_idle()

    def save(self):

        # filenames, _ = QFileDialog.getSaveFileName(self, caption='保存文件', dir='', filter='Text files (*.txt)')
        # print(filenames)
        # try:
        #     with open(filenames, 'w', encoding='utf-8') as f:
        #         f.write('123')
        # except:
        #     pass
        # out = {}
        # for a in range(self.ui.widget_result.columnCount()):
        #     col = str(a)
        #     out[col] = []
        #     for b in range(self.ui.widget_result.rowCount()):
        #         data = self.ui.widget_result.item(b, a).text()
        #         line_a = data.append()
        # print(a)
        # print(b)
        # print(line_a)


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.showMaximized()
    app.exec_()
