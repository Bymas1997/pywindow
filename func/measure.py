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
