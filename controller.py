from func.data import File_Loader
from func.measure import Measure


class Controller:

    @staticmethod
    def load_file(filename):
        mydata = File_Loader(filename)
        x = mydata.x
        y = mydata.y
        z = mydata.z
        return x, y, z

    @staticmethod
    def pick_point(x, y, ind):
        _pick_x, _pick_y, _point_str = Measure.point_ind(x, y, ind)
        return _pick_x, _pick_y, _point_str

    @staticmethod
    def measure_distance(marked_x, marked_y):
        distance = Measure.distance(marked_x, marked_y)
        return distance

    @staticmethod
    def measure_area(marked_x, marked_y, marked_data):
        area_data, area_plot = Measure.area(marked_x, marked_y, marked_data)
        return area_data, area_plot

    @staticmethod
    def measure_depth(marked_x, marked_y, marked_data, ptp_distance):
        depth_point, drop_foot_x, drop_foot_y, depth_max = Measure.depth(marked_x, marked_y, marked_data, ptp_distance)
        return depth_point, drop_foot_x, drop_foot_y, depth_max

    @staticmethod
    def roi_select(x, y, z):
        j = Measure.abc(x, y, z)
        return j
