# coding=utf-8
import configparser


class ReadIni(object):
    def __init__(self, file_name=None):
        if file_name == None:
            file_name = "D:/OTC_selenium/config/LocalElement.ini"
        self.cf = self.load_ini(file_name)

    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value得值
    def get_value(self, node, key):
        data = self.cf.get(node, key)
        return data


if __name__ == '__main__':
   read = ReadIni()
   print(read.get_value("RegisterElement", 'user_email'))
