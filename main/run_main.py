# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import unittest
from util.server import Server
import multiprocessing
from util.write_device_yaml import WriteDeviceYaml
import HtmlTestRunner
from time import sleep
from case import try_login_case
from case import try_splash_case


def appium_server():
    server = Server()
    server.main()


def get_suite(i):
    suite = unittest.TestSuite()
    # suite.addTest(try_splash_case.TestSplashCase("test01", parame=i))
    suite.addTest(try_login_case.TestLoginCase("test01", parame=i))
    HtmlTestRunner.HTMLTestRunner(output="test").run(suite)


def get_count():
    write_user_file = WriteDeviceYaml()
    count = write_user_file.get_file_lines()
    return count


if __name__ == '__main__':
    appium_server()
    threads = []
    for i in range(get_count()):
        th = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(th)

    for y in threads:
        sleep(1)
        y.start()
