import numpy as np


class myData(object):
    def __init__(self,filename):
        self.name = filename
        lnum = 0
        x = []  # 创建空表存放x数据
        y = []  # 创建空表存放y数据
        with open(self.name, 'r') as f:  # 以只读形式打开某.txt文件
            for line in f:
                lnum += 1
                if lnum >= 0:  # 从第四行开始添加数据
                    line = line.strip('\n')  # 去掉换行符
                    line = line.split('\t')  # 分割掉两列数据之间的制表符
                    x.append(line[0])
                    y.append(line[1])

        # NOTE：此时所得到的x列表中的数据类型是str类型，因此需要进行转换，转换为float类型
        x = np.array(x)
        x = x.astype(float).tolist()

        y = np.array(y)
        y = y.astype(float).tolist()
        self.x = x
        self.y = y


if __name__ == '__main__':
    filename = '../profile_1.txt'
    mydata = myData(filename)
    print(mydata.x)
