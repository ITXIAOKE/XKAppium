# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import unittest
import threading
from time import sleep


# 第二种使用自定义元类的方式解决,这个方法和函数类似，有待考察
class TestCaseMeta:
    def __new__(cls, class_name, class_base, parame):
        global parame_global
        new_parame = {"parame_global": parame}
        return type(class_name, class_base, new_parame)


class MyTestCase(unittest.TestCase, metaclass=TestCaseMeta):

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
    suite.addTest(MyTestCase("test01", parame=i))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    threads = []
    for i in range(2):
        th = threading.Thread(target=get_suite, args=(i,))
        threads.append(th)

    for y in threads:
        sleep(1)
        y.start()
