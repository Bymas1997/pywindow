
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt


class MyFigureCanvas(FigureCanvas):

    def __init__(self, parent=None, width=10, height=5, xlim=(0, 2500), ylim=(-2, 2), dpi=100):
        # 创建一个Figure
        fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)  # tight_layout: 用于去除画图时两边的空白

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111)  # 添加子图
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.set_xlim(xlim)
        self.axes.set_ylim(ylim)