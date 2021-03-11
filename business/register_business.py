# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

from appium import webdriver
from time import sleep
from base.base_driver import BaseDriver


class RegisterBusiness:

    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.get_driver(i)

    # 点击已有账号，去登录
    def go_login(self):
        self.driver.find_element_by_id("cn.com.open.mooc:id/tv_go_login").click()
