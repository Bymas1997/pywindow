from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from main_ui import Ui_MainWindow
from graph import MyFigureCanvas
import matplotlib
from matplotlib.widgets import RectangleSelector
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from graph import myData
matplotlib.use("Qt5Agg")  # 声明使用QT5


class FigureCanvasDemo1(FigureCanvas, myData):
    def __init__(self):
        fig = Figure()
        FigureCanvas.__init__(self, fig)
        self.ax = fig.add_subplot(
            xlim=(-8, 8),
            ylim=(-9, 9))
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        # 开始作图

        self.ax.plot(myData.x, myData.y)
        self.ax.set_title('')
        self.x = RectangleSelector(self.ax, self.onselect_xy,
                                   drawtype='box',
                                   useblit=False,  # or True?
                                   rectprops={'alpha': 0.5, 'facecolor': 'red'},
                                   interactive=True)
        self.draw()

    def onselect_xy(self, *args, **kwargs):
        self.ax.clear()
        self.ax.plot([random.random() for _ in range(50)])
        self.draw()


class Stats(QMainWindow, myData):

    def __init__(self):
        super(Stats, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.func1.clicked.connect(self.select_callback)
        self.gv_visual_data_content = MyFigureCanvas(width=self.ui.graphicsView.width() / 101,
                                                     height=self.ui.graphicsView.height() / 101,
                                                     xlim=(-8, 8),
                                                     ylim=(-9, 9))  # 实例化一个FigureCanvas
        self.plot_data()

        self.plot = FigureCanvasDemo1()
        layout = self.ui.verticalLayout_3
        layout.addWidget(self.plot)

    def plot_data(self):
        self.gv_visual_data_content.axes.plot(myData.x, myData.y)
        self.gv_visual_data_content.axes.set_title('')
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(self.gv_visual_data_content)
        # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 调用show方法呈现图形


if __name__ == '__main__':
    myData = myData()
    app = QApplication([])
    stats = Stats()
    stats.show()
    app.exec_()
