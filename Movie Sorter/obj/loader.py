


class Loader():

    def __init__(self):
        self.wlist = []
        self.path = str()

    def write_list(self, path, name, year, res):
        self.wlist.append([path, name, year, res])

    def file_build(self, filepath, filename, year, resolution):
        file_path = str(filepath)
        file_name = str(filename)
        try:
            file_year = str(year)
        except:
            file_year = str(0000)
        file_res = str(resolution)
        self.write_list(file_path, file_name, file_year, file_res)

    

