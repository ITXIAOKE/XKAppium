# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

from util.dos_cmd import DosCmd


class Port:
    def __init__(self):
        self.dos_cmd = DosCmd()

    # 判断端口是否被占用
    def port_is_use(self, port_num):
        command = 'netstat -ano | findstr ' + str(port_num)
        result = self.dos_cmd.execute_result_cmd(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    # 生成可用的端口列表，是为有几个手机设备做准备
    def create_use_port(self, start_port, devices_list):
        # 放可用端口的集合，有几个设备就有几个端口
        port_list = []
        if len(devices_list) > 0:
            while len(port_list) != len(devices_list):
                # 判断传进来的端口是否被占用，如果没有被占用，那就添加到可用端口的列表集合中
                if self.port_is_use(start_port) is not True:
                    port_list.append(start_port)
                # 因为有很多个设备，那就要生成很多的端口，当添加完一个端口到可用端口列表中后，下一个端口就要加1
                start_port = start_port + 1
            return port_list
        else:
            return None


if __name__ == '__main__':
    port = Port()
    # print(port.port_is_use(62001))
    print(port.create_use_port(4700, [1, 2, 3]))
