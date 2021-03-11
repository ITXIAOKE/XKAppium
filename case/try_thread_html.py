# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import unittest
import threading
import HtmlTestRunner
from time import sleep
from appium import webdriver


class TestReport(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("this is serupclass")

    def setUp(self):
        print("this is setup")

    def test01(self):
        self.assertEqual("1", "1")
        print("test01")

    def test02(self):
        self.assertIn("abc", "xabck")
        print("test02")

    def tearDown(self):
        print("this is teardown")

    @classmethod
    def tearDownClass(cls):
        print("this is teardownclass")


def get_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestReport("test01"))
    suite.addTest((TestReport("test02")))
    # unittest.TextTestRunner().run(suite)
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="interface"))
    # HtmlTestRunner.HTMLTestRunner(output="login_test", report_title="xiaoke").run(suite)
    # html_file = "E:/pycharmProject/appium/appiumProject/reports/login_test" + str(i) + ".html"
    # with open(html_file, "w") as f:
    HtmlTestRunner.HTMLTestRunner(output="login_test").run(suite)


# from unittest import TestLoader, TestSuite
# from HtmlTestRunner import HTMLTestRunner
# import ExampleTest
# import Example2Test
#
# example_tests = TestLoader().loadTestsFromTestCase(ExampleTests)
# example2_tests = TestLoader().loadTestsFromTestCase(Example2Test)
#
# suite = TestSuite([example_tests, example2_tests])
#
# runner = HTMLTestRunner(output='example_suite')
#
# runner.run(suite)

if __name__ == '__main__':
    threads = []
    for i in range(3):
        th = threading.Thread(target=get_suite)
        threads.append(th)

    for y in threads:
        # 由于是多线程执行，为了让每个线程生成的报告都显示，那我就让每个线程延时1秒执行
        # 这样就可以把每个线程生成的报告显示出来
        sleep(1)
        y.start()
