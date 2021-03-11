# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

from util.dos_cmd import DosCmd
from util.port import Port
import threading
from util.write_device_yaml import WriteDeviceYaml
from time import sleep


# 操作命令窗口
class Server:
    def __init__(self):
        self.dos_cmd = DosCmd()
        self.port = Port()
        self.write_yaml = WriteDeviceYaml()
        self.get_devices_num = self.get_devices_list()

    # 获取所有设备的列表
    def get_devices_list(self):
        device_list = []
        devices = self.dos_cmd.execute_result_cmd("adb devices")
        if len(devices) >= 2:
            for device_name in devices:
                if "List" in device_name:
                    continue
                flag = device_name.split("\t")[1]
                if flag == "device":
                    device_list.append(device_name.split("\t")[0])
            return device_list
        else:
            return None

    # 创建可用的端口
    def create_use_port(self, start_port):
        return self.port.create_use_port(start_port, self.get_devices_list())

    # 生成命令
    def create_command_list(self, i):
        # appium -p 4700 -bp 4900 -U 127.0.0.1:62001
        command_list = []
        appium_list = self.create_use_port(4700)
        bootstrap_list = self.create_use_port(4900)
        devices = self.get_devices_list()
        command = " appium -p " + str(appium_list[i]) + " -bp " + str(bootstrap_list[i]) + " -U " + str(
            devices[
                i]) + " --no-reset --session-override --log E:/pycharmProject/appium/appiumProject/log/appium_log" + str(
            i) + ".log"
        command_list.append(command)

        # 把设备的端口，bootstrap端口和设备名称写入yaml文件中，方便在初始化driver时候使用
        self.write_yaml.write_value(i, str(appium_list[i]), str(bootstrap_list[i]), str(devices[i]))
        return command_list

    # 启动服务
    def start_server(self, i):
        start_list = self.create_command_list(i)
        print(start_list)
        # 因为是在多线程中，每次启动，只有第一个命令
        self.dos_cmd.execute_cmd(start_list[0])

    # 关闭服务
    def kill_server(self):
        node_list = self.dos_cmd.execute_result_cmd('tasklist | find "node.exe"')
        # print(node_list)
        if len(node_list) > 0:
            self.dos_cmd.execute_cmd('taskkill -F -PID node.exe')

    #   启动服务的主入口，几个设备就启动几个服务
    def main(self):
        # 启动程序的时候，先把已开启的node.exe程序杀死
        self.kill_server()
        # 再把数据写入yaml文件前先把yaml文件中数据清空
        self.write_yaml.clear_value()
        for i in range(len(self.get_devices_num)):
            appium_thread = threading.Thread(target=self.start_server, args=(i,))
            appium_thread.start()
        # 因为是多个机器，这个地方一定要等待一下，让所有的设备都能运行起来
        sleep(5)


if __name__ == '__main__':
    server = Server()
    # print(server.get_devices_list())
    # print(server.create_command_list())
    server.main()
