# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com
import multiprocessing
import unittest
from time import sleep
from business.login_business import LoginBusiness
import sys, traceback
from base.login_exception import LoginException


# 第一种方式解决，# 第二种使用元类解决 # 第三种采用一个函数即可实现
from util.server import Server


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super().__init__(methodName)
        self.parame = parame
        global global_i
        global_i = self.parame


class TestLoginCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        # 注意以下的写法，每次都创建出一个driver，也就是一个session，那么就会报错已有session了：
        # 报错如下 a session eithor terminder  or not start
        cls.login_business = LoginBusiness(global_i)
        # cls.splash_business = SplashBusiness(global_i)
        cls.exception_list = LoginException()

    def setUp(self):
        print("this is setup")

    def test01(self):
        # 休息4秒的原因是为了等待手动找到登录页面，进行操作
        sleep(4)
        self.login_business.login_success()

    # def test02(self):
    #     print("test02")
    #     self.login_business.login_user_error()

    def tearDown(self):
        sleep(1)
        print("this is teardown")
        print("++++++++++++++++++>>>>%s" % str(sys.exc_info()[1]))
        print("++++++++++++++++++>>>>%s" % str(self.exception_list.get_exception_length()))
        # 运行一个case结束后，判断异常列表中如果有异常，则截图
        if self.exception_list.get_exception_length():
            self.login_business.login_handle.login_page.driver.get_screenshot_as_file("../image/login_error.png")

    @classmethod
    def tearDownClass(cls):
        print("this is teardownclass")
        # print("++++++++++++++++++>>>>%s" % str(sys.exc_info()[1]))  # 捕获异常

def appium_server():
    server = Server()
    server.main()


# 添加多个suit
def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(TestLoginCase("test01", parame=i))
    suite.addTest((TestLoginCase("test02", parame=i)))
    # unittest.TextTestRunner().run(suite)
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="interface"))
    # HtmlTestRunner.HTMLTestRunner(output="login_test", report_title="xiaoke").run(suite)
    # html_file = "E:/pycharmProject/appium/appiumProject/reports/login_test" + str(i) + ".html"
    # with open(html_file, "w") as f:
    HtmlTestRunner.HTMLTestRunner(output="test").run(suite)


if __name__ == '__main__':
    # 在项目开始之前先启动appium服务
    appium_server()
    threads = []
    for i in range(2):
        # 有几个设备就产生几个报告
        # 多线程会产生数据串连，达不到想要的结果
        # th = threading.Thread(target=get_suite, args=(i,))
        th = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(th)

    for y in threads:
        # 由于是多线程执行，为了让每个线程生成的报告都显示，那我就让每个线程延时1秒执行
        # 这样就可以把每个线程生成的报告显示出来
        sleep(1)
        y.start()
