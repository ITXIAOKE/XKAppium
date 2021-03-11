# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import os


class DosCmd:
    # 执行dos命令
    def execute_cmd(self, command):
        os.system(command)

    # 执行dos命令，获取结果
    def execute_result_cmd(self, command):
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            # 最后一个数据是\n,如果遍历到\n，那就遍历就结束了
            if i == "\n":
                continue
            result_list.append(i.strip("\n"))
        return result_list


if __name__ == '__main__':
    dos = DosCmd()
    # print(dos.execute_result_cmd("adb devices"))
    # print(dos.execute_cmd("adb devices"))
