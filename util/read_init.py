# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import configparser


class ReadIni:
    def __init__(self, file_path=None):
        self.read_ini = configparser.ConfigParser()
        if file_path is not None:
            self.read_ini.read(file_path)
        else:
            self.read_ini.read("../config/localelement.ini")

    # section代表是哪个页面，默认是登录页面
    # key 代表是哪个输入框
    def get_ini_data(self, key, section=None):
        if section is None:
            section = "login_element"
        try:
            read_data = self.read_ini.get(section, key)
        except Exception as e:
            read_data = None
            print(e)

        return read_data


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_ini_data("password", "login_element"))
