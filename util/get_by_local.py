# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

from util.read_init import ReadIni
import sys, traceback
from base.login_exception import LoginException


class GetByLocal:

    def __init__(self, driver):
        self.read_ini = ReadIni()
        self.driver = driver
        self.exception_login = LoginException()

    def get_element(self, key):
        data = self.read_ini.get_ini_data(key)
        # print(data)
        if data is not None:
            split_data = data.split(">")
            by_method = split_data[0]
            by_content = split_data[1]
            try:
                if by_method == "id":
                    return self.driver.find_element_by_id(by_content)
                elif by_method == "className":
                    return self.driver.find_element_by_class_name(by_content)
                else:
                    return self.driver.find_element_by_xpath(by_content)
            except Exception as e:
                print("++++++++++++++++++>>>>%s" % str(sys.exc_info()))
                print("++++++++++++++++++>>>>%s" % str(sys.exc_info()[0]))
                print("++++++++++++++++++>>>>%s" % str(sys.exc_info()[1]))
                print("++++++++++++++++++>>>>%s" % str(sys.exc_info()[2]))
                self.driver.get_screenshot_as_file("../image/by_element.png")
                self.exception_login.exception_append_value(e)
                print("bbbb++>>>>%s" % str(self.exception_login.get_exception_length()))
                raise e
        else:
            return None
