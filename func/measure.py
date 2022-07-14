import numpy as np


class Measure:
    @staticmethod
    def point_ind(x, y, ind_index):
        pick_x = np.array(np.array(x)[ind_index])[0]
        pick_y = np.array(np.array(y)[ind_index])[0]
        data_xy = str(pick_x) + '  ' + str(pick_y) + '\n' + '\n'

        return pick_x, pick_y, data_xy

    @staticmethod
    def distance(marked_x, marked_y):
        distance = pow(
            pow(marked_x[0] - marked_x[1], 2) + pow(marked_y[0] - marked_y[1], 2), 0.5)
        return distance

    @staticmethod
    def area(marked_x, marked_y, marked_data):
        area_x = []
        area_y = []
        for num in marked_data:
            area_x.append(num[0])
            area_y.append(num[1])
        area1 = np.trapz(marked_y, x=marked_x)
        area2 = np.trapz(area_x, x=area_y)
        area = area2 - area1
        area_data = str(abs(area))
        area_plot = 's :' + str(abs(area))
        return area_data, area_plot

    @staticmethod
    def depth(marked_x, marked_y, marked_data, ptp_distance):
        p1 = np.array([marked_x[0], marked_y[0]])
        p2 = np.array([marked_x[1], marked_y[1]])
        _p1 = p2 - p1
        _p2 = marked_data - p1
        cross = np.cross(_p1, _p2)
        cross_norm = np.absolute(cross)
        depth = cross_norm / ptp_distance
        depth_max = max(depth)
        max_depth_index = np.argmax(depth)
        depth_point = marked_data[max_depth_index]
        drop_foot_x, drop_foot_y = np.linalg.solve(
            [[marked_y[0] - marked_y[1], marked_x[1] - marked_x[0]],
             [-(marked_x[1] - marked_x[0]) / (marked_y[0] - marked_y[1]), 1]],
            [marked_x[1] * marked_y[0] - marked_x[0] * marked_y[1],
             (-(depth_point[0] * (marked_x[1] - marked_x[0])) / (marked_y[0] - marked_y[1])) +
             depth_point[1]])
        return depth_point, drop_foot_x, drop_foot_y, depth_max

    @staticmethod
    def roi(x, y):
        x_resh = np.array_split(x, 3)
        y_resh = np.array_split(y, 3)
        _n = -np.diff(y) / pow(pow(np.diff(x), 2) + pow(np.diff(y), 2), 0.5), np.diff(x) / pow(
            pow(np.diff(x), 2) + pow(np.diff(y), 2), 0.5)
        n = [i for i in zip(_n[0], _n[1])]
        x_t = np.gradient(x, edge_order=2)
        y_t = np.gradient(y, edge_order=2)
        xx_t = np.gradient(x_t)
        yy_t = np.gradient(y_t)
        curvature_val = np.abs(xx_t * y_t - x_t * yy_t) / (x_t * x_t + y_t * y_t) ** 1.5
        cur = curvature_val[0:len(curvature_val) - 1]
        _k = np.diff(x) * cur / pow(pow(np.diff(x), 2) + pow(np.diff(y), 2), 0.5), np.diff(y) * cur / pow(
            pow(np.diff(x), 2) + pow(np.diff(y), 2), 0.5)
        k = [i for i in zip(_k[0], _k[1])]
        k_ave = (np.cumsum(k, axis=0) / len(k))[len(k) - 1]  # K 曲率
        k_avee = k_ave.reshape(2, 1)
        dot = abs(np.dot(n, k_avee).flatten())
        con = np.convolve(dot, np.hanning(40) / 20, 'same')
        print(con)
        target = np.intersect1d(np.argwhere(12< con).flatten(), np.argwhere(18 > con).flatten())
        target_diff = np.diff(target)
        count = 1
        _count = 0
        _miss = True
        for i in target_diff:
            if 4 > i > 0:
                count += 1
            else:
                count += 1
                _count += 1
                # if _count == 1:
                #
                #     jj = (y[target[count-1]] - y[target[0]]) / (x[target[count-1]] - x[target[0]])
                #     if jj > 0:
                #         _miss = False
                #     else:
                #         _miss = True
                #
                # else:
                #     pass
            if _count == 3:
                break
        if _count == 3:
            x_plot = x[target[0] - 4:target[count-1] + 30]
            y_plot = y[target[0] - 4:target[count-1] + 30]
        else:
            x_plot = 'fail'
            y_plot = 'fail'

        return x_plot, y_plot, _miss

    @staticmethod
    def abc(x, y, z):
        j = []
        n = 1
        for i in np.arange(0, 4.794, 0.006):
            if i >= 0:
                qq, _, _ = Measure.roi(x[800 * (n - 1):800 * n - 1], y[800 * (n - 1):800 * n - 1])
                if qq == 'fail' or qq == ():
                    n += 1

                else:
                    j.append(i)
                    n += 1
        return j
