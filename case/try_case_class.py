# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import unittest
import threading
import HtmlTestRunner
from time import sleep
from business.login_business import LoginBusiness


# 第一种方式解决
class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super().__init__(methodName)
        self.parame = parame
        global parame_global
        parame_global = self.parame


class TestCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass--->%s" % parame_global)

    def setUp(self):
        print("setup--->%s" % parame_global)

    def test01(self):
        print("test01--->%s" % parame_global)

    def tearDown(self):
        print("this is teardown")

    @classmethod
    def tearDownClass(cls):
        print("this is teardownclass")


def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(TestCase("test01", parame=i))
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    threads = []
    for i in range(3):
        th = threading.Thread(target=get_suite, args=(i,))
        threads.append(th)

    for y in threads:
        sleep(1)
        y.start()
