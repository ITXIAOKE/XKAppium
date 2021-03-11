# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

from appium import webdriver
from time import sleep
from util.write_device_yaml import WriteDeviceYaml


class BaseDriver:
    def __init__(self):
        self.write_yaml = WriteDeviceYaml()

    def android_driver(self, i):
        device_name = self.write_yaml.get_value("device_info_" + str(i), "deviceName")
        device_port = self.write_yaml.get_value("device_info_" + str(i), "port")
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": device_name,
            "app": "E:\\pycharmProject\\appium\\appiumProject\\app\\mukewang.apk",
            # "appWaitActivity": "cn.com.open.mooc.user.register.MCPhoneRegisterAty",
            # "appWaitActivity": "cn.com.open.mooc.user.login.MCLoginActivity",
            # 最新的appium不需要以下两行代码
            # "appPackage":"",
            # "appActivity":"",
            "noReset": "false"
        }
        driver = webdriver.Remote("http://127.0.0.1:" + device_port + "/wd/hub", capabilities)
        sleep(5)
        # driver.network_connection
        # driver.set_network_connection()
        return driver

    def ios_driver(self):
        pass

    def get_driver(self, i):
        return self.android_driver(i)
