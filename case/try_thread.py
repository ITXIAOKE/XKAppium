# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

import threading

threads = []


def sum(a):
    print(a + 1)


for i in range(3):
    thread = threading.Thread(target=sum, args=(i,))
    threads.append(thread)
    print(thread)

if __name__ == '__main__':
    for y in threads:
        y.start()
