# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import yaml
from time import sleep


# 操作yaml文件的类
class WriteDeviceYaml:
    def __init__(self, file_path=None):
        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = '../config/devicesconfig.yaml'

    def read_yaml(self):
        with open(self.file_path, 'rb') as f:
            data = yaml.load(f)
            # print(data)
        return data

    # 在初始化driver的时候，由于是多机运行，就可以从yaml文件中读取到不同机器的机器名和端口号
    def get_value(self, tag, key):
        # tag是机器名，key是字典中的键
        return self.read_yaml()[tag][key]

    # 拼接符合yaml格式的数据
    def join_value(self, i, port, bp, deviceName):
        data = {
            "device_info_" + str(i): {
                "port": port,
                "bp": bp,
                "deviceName": deviceName
            }
        }
        # print(data)
        return data

    # 把数据写入yaml中
    def write_value(self, i, port, bp, deviceName):
        write_data = self.join_value(i, port, bp, deviceName)
        # 追加的方式把数据添加到yaml文件中
        with open(self.file_path, 'a') as f:
            yaml.dump(write_data, f)

    # 每次添加数据前，先把yaml文件中数据先清空
    def clear_value(self):
        with open(self.file_path, "w") as f:
            f.truncate()

    # 拿到写入yaml文件的设备个数
    def get_file_lines(self):
        data = self.read_yaml()
        return len(data)


if __name__ == '__main__':
    write = WriteDeviceYaml()
    # print(write.get_value("device_info_01", "bp"))
    # write.write_value(1, 11, 22, 3333)
