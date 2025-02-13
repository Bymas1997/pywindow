import numpy as np


class File_Loader(object):
    def __init__(self, filename):
        self.name = filename
        lnum = 0
        x = []  # 创建空表存放x数据
        y = []
        z = []  # 创建空表存放y数据
        with open(self.name, 'r') as f:  # 以只读形式打开某.txt文件
            for line in f:
                lnum += 1
                if lnum >= 0:
                    line = line.strip('\n')  # 去掉换行符
                    line = line.split('\t')  # 分割掉两列数据之间的制表符
                    x.append(line[0])
                    y.append(line[1])
                    z.append(line[2])

        # NOTE：此时所得到的x列表中的数据类型是str类型，因此需要进行转换，转换为float类型
        _x = np.array(x)
        _x = _x.astype(float).tolist()

        _y = np.array(y)
        _y = _y.astype(float).tolist()

        _z = np.array(z)
        _z = _z.astype(float).tolist()
        self.x = _x
        self.y = _y
        self.z = _z


if __name__ == '__main__':
    filename = '../profile_1.txt'
    # mydata = myData(filename)
    # print(mydata.x)
