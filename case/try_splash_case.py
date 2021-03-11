# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import unittest
from time import sleep
from business.splash_business import SplashBusiness


# 第一种方式解决，# 第二种使用元类解决 # 第三种采用一个函数即可实现
class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super().__init__(methodName)
        self.parame = parame
        global global_i
        global_i = self.parame


class TestSplashCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.splash_business = SplashBusiness(global_i)

    def setUp(self):
        print("this is setup")

    def test01(self):
        print("test01")
        self.splash_business.swipe_on("left", 1000)
        sleep(2)
        self.splash_business.swipe_on("left", 1000)
        sleep(2)
        self.splash_business.swipe_on("right", 1000)
        sleep(2)
        self.splash_business.swipe_on("right", 1000)
        sleep(2)
        self.splash_business.swipe_on("left", 1000)

    # def test02(self):
    #     print("test02")
    #     self.splash_business.swipe_on("left", 1000)
    #     sleep(2)
    #     self.splash_business.swipe_on("left", 1000)

    def tearDown(self):
        print("this is teardown")

    @classmethod
    def tearDownClass(cls):
        print("this is teardownclass")

#
# def appium_server():
#     server = Server()
#     server.main()
#
#
# # 添加多个suit
# def get_suite(i):
#     suite = unittest.TestSuite()
#     suite.addTest(TestCase("test01", parame=i))
#     suite.addTest(TestCase("test02", parame=i))
#     # unittest.TextTestRunner().run(suite)
#     # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="interface"))
#     # HtmlTestRunner.HTMLTestRunner(output="login_test", report_title="xiaoke").run(suite)
#     # html_file = "E:/pycharmProject/appium/appiumProject/reports/login_test" + str(i) + ".html"
#     # with open(html_file, "w") as f:
#     HtmlTestRunner.HTMLTestRunner(output="login_test").run(suite)
#
#
# if __name__ == '__main__':
#     # 在项目开始之前先启动appium服务
#     appium_server()
#     threads = []
#     for i in range(2):
#         # th = threading.Thread(target=get_suite, args=(i,))
#         th = multiprocessing.Process(target=get_suite, args=(i,))
#         threads.append(th)
#
#     for y in threads:
#         # 由于是多线程执行，为了让每个线程生成的报告都显示，那我就让每个线程延时1秒执行
#         # 这样就可以把每个线程生成的报告显示出来
#         sleep(1)
#         y.start()
