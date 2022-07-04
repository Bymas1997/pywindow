from func.data import File_Loader


class Controller:
    def load_file(self, filename):
        mydata = File_Loader(filename)
        x = mydata.x
        y = mydata.y
        return x, y
