# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

from appium import webdriver

import time
# 4zr70639780335000b   万能验证码  190325
# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '127.0.0.1:62025'
# app信息
desired_caps['appPackage'] = 'com.hx.vrshop'
desired_caps['appActivity'] = '.ui.activity.MainActivity'
# 初始化webdriver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("appium 正在运行...")
time.sleep(10)
print("appium 即将运行结束...")
driver.quit()
print("appium 运行结束...")