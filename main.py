from PySide2.QtWidgets import QApplication, QMessageBox, QPushButton, QMainWindow, QGraphicsScene, QFileDialog
from PySide2.QtUiTools import QUiLoader
from main_ui import Ui_MainWindow
import numpy as np
from graph import MyFigureCanvas
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt

matplotlib.use("Qt5Agg")  # 声明使用QT5


class Stats(QMainWindow):

    def __init__(self):
        super(Stats, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.gv_visual_data_content = MyFigureCanvas(width=self.ui.graphicsView.width() / 101,
                                                     height=self.ui.graphicsView.height() / 101,
                                                     xlim=(-8, 8),
                                                     ylim=(-9, 9))  # 实例化一个FigureCanvas
        lnum = 0
        x = []  # 创建空表存放x数据
        y = []  # 创建空表存放y数据
        with open("profile_1.txt", 'r') as f:  # 以只读形式打开某.txt文件
            for line in f:
                lnum += 1
                if (lnum >= 0):  # 从第四行开始添加数据
                    line = line.strip('\n')  # 去掉换行符
                    line = line.split('\t')  # 分割掉两列数据之间的制表符
                    x.append(line[0])
                    y.append(line[1])

        # NOTE：此时所得到的x列表中的数据类型是str类型，因此需要进行转换，转换为float类型
        x = np.array(x)
        x = x.astype(float).tolist()

        y = np.array(y)
        y = y.astype(float).tolist()
        self.plot_cos()

    def loadData(flieName):

        lnum = 0
        x = []  # 创建空表存放x数据
        y = []  # 创建空表存放y数据
        with open(flieName, 'r') as f:  # 以只读形式打开某.txt文件
            for line in f:
                lnum += 1
                if (lnum >= 1):  # 从第四行开始添加数据
                    line = line.strip('\n')  # 去掉换行符
                    line = line.split('\t')  # 分割掉两列数据之间的制表符
                    x.append(line[0])
                    y.append(line[1])

        # NOTE：此时所得到的x列表中的数据类型是str类型，因此需要进行转换，转换为float类型
        x = np.array(x)
        x = x.astype(np.float).tolist()

        y = np.array(y)
        y = y.astype(np.float).tolist()

        return x, y

    def plot_cos(self):
        lnum = 0
        x = []  # 创建空表存放x数据
        y = []  # 创建空表存放y数据
        with open("profile_1.txt", 'r') as f:  # 以只读形式打开某.txt文件
            for line in f:
                lnum += 1
                if (lnum >= 0):  # 从第四行开始添加数据
                    line = line.strip('\n')  # 去掉换行符
                    line = line.split('\t')  # 分割掉两列数据之间的制表符
                    x.append(line[0])
                    y.append(line[1])

        # NOTE：此时所得到的x列表中的数据类型是str类型，因此需要进行转换，转换为float类型
        x = np.array(x)
        x = x.astype(float).tolist()

        y = np.array(y)
        y = y.astype(float).tolist()

        # return x, y
        #
        # x = np.arange(0, 2 * np.pi, 0.001)
        # y = x * x
        self.gv_visual_data_content.axes.plot(x, y)

        self.gv_visual_data_content.axes.set_title('')
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(
            self.gv_visual_data_content)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 调用show方法呈现图形


if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.show()
    app.exec_()
