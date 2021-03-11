# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

from appium import webdriver
from time import sleep
from base.base_driver import BaseDriver


class SplashBusiness:

    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.get_driver(i)

    # 获取屏幕的宽和高
    def get_size(self):
        # 获取屏幕的大小
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self, time=None):
        # 大坐标点
        x1 = self.get_size()[0] / 9 * 7
        y = self.get_size()[1] / 2
        # 小坐标点
        x2 = self.get_size()[0] / 9
        self.driver.swipe(x1, y, x2, y, time)

    # 向右边滑动
    def swipe_right(self, time=None):
        # 大坐标点
        x1 = self.get_size()[0] / 9 * 7
        y = self.get_size()[1] / 2
        # 小坐标点
        x2 = self.get_size()[0] / 9
        self.driver.swipe(x2, y, x1, y, time)

    # 向上边滑动
    def swipe_up(self, time=None):
        # 大坐标点
        x = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 8
        # 小坐标点
        y2 = self.get_size()[1] / 10
        self.driver.swipe(x, y1, x, y2, time)

    # 向下边滑动
    def swipe_down(self, time=None):
        # 大坐标点
        x = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        # 小坐标点
        y2 = self.get_size()[1] / 10
        self.driver.swipe(x, y2, x, y1, time)

    # 根据指定的滑动方向，选择滑动的函数
    def swipe_on(self, direction=None, time=None):
        if direction == "up":
            self.swipe_up(time)
        elif direction == "down":
            self.swipe_down(time)
        elif direction == "left":
            self.swipe_left(time)
        elif direction == "right":
            self.swipe_right(time)
        else:
            self.swipe_right(time)


if __name__ == '__main__':
    splash_business = SplashBusiness(0)
    splash_business.swipe_on("left")
    sleep(1)
    splash_business.swipe_on("left", 1000)
    sleep(1)
    splash_business.swipe_on("right")
    sleep(1)
    splash_business.swipe_on("right", 1000)
    # 进入注册页面
    splash_business.swipe_on("left")
    splash_business.swipe_on("left")
    sleep(2)
    splash_business.swipe_on("up", 3000)
    sleep(2)
