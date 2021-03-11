# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

# test = ['aa', 'bb', 'cc', 'dd']
# for i in range(len(test)):
#     print(i, test[i])

#
# def string_reverse(text='abcdef'):
#     new_text = []
#     for i in range(1, len(text)+1):
#         # new_text += text[-i]
#         new_text.append(text[-i])
#         print(new_text)
#     return ''.join(new_text)
#
#
# print(string_reverse())
# print([x for x in range(0, 10) if x % 2 == 0])

# coding=utf-8 
# def originalFunc():
#     print('this is original function!')
#
# def modifiedFunc():
#     modifiedFunc = 1
#     print('this is modified function!')
#
# def main():
#     originalFunc()
#
# if __name__ == '__main__':
#     originalFunc = modifiedFunc  # 这句是加的猴子补丁
#     main()


from json import JSONEncoder

# def _default(self, obj):
#     return getattr(obj.__class__, "to_json", _default.default)(obj)
#
#     # 在没有to_json属性的情况下才使用默认的JSONEncoder.default的方法
#     _default.default = JSONEncoder().default
#
#     # 设置JSONEncoder.default方法为自定义的，有to_json属性的_default方法
#     default.JSONEncoder.default = _default

# a = 1
# print(a)  # 1
#
#
# def fun(a):
#     a = 2
#     print("--%s" % a)  # 2
#
#
# fun(a)
# print(a)  # 1

# 第二个例子：
# a = []
# print(a)  # []
#
#
# def fun(a):
#     a.append(1)
#     print(a)  # [1]
#
#
# fun(a)
# print(a)  # [1]
# def o_fuc(self):
#     print("obj_func")
#
#
# @classmethod
# def class_func(cls):
#     print("class_func")
#
#
# @staticmethod
# def static_func():
#     print("static_func")
#
#
# Foo = type("Foo", (object,), {"a": 100, "obj_func": o_fuc, "class_func": class_func, "static_func": static_func})
# obj = Foo()
# print(obj.a)
# print(Foo.a)
# obj.obj_func()
# Foo.class_func()
# Foo.static_func()
# +++++++++++++++++++++++++++++++++++++
# class A(object):
#     print("nn")
#     def foo(self, x):
#         print("bb")
#         print("executing foo(%s,%s)" % (self, x))
#         print("cc")
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s,%s)" % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % x)
#
#
# class B(A):
#     print("ee")
#     pass
#     print("ff")
#
#
# b = B()
# print("aa")
# print()
# print(b.foo(2))
# print()
# print("dd")
# print(b.class_foo(2))
# print(b.static_foo(3))
# # 结果如下：
# # executing foo(<__main__.B object at 0x000001BB5A70E390>,2) # 注意这个实例对象是B，调用A类中的实例方法
# # None
# # executing class_foo(<class '__main__.B'>,2)  # 注意这个类对象是B，调用A类中的类方法
# # None
# # executing static_foo(3)
# # None
# print(b)

# li = [12, 45, 78, 784]
# print(map('the number is {} '.format, li))
# for xx in map('the number is {} '.format, li):
#     print(xx)
# 结果是：
# <map object at 0x000002626AB542B0>
# the number is 12
# the number is 45
# the number is 78
# the number is 784
#
# class Fib(object):
#     def __init__(self):
#         pass
#
#     def __call__(self, num):
#         a, b = 0, 1
#         self.l = []
#         for x in range(num):
#             self.l.append(a)
#             a, b = b, a + b
#         return self.l
#
#     def __str__(self):
#         return str(self.l)
#
#     __repr__ = __str__
#
#
# f = Fib()
# print(f(10))

# print(3/2)
# print(3//2)
# print(3/2.0)
# print(3//2.0)
# print(3.0/2)
# print(3.0//2)

dict_test = [{'a': 4}, {'a': 5}, {'a': 3}, {'a': 4}, {'a': 5}]


# 第一种方法：使用continue和新列表返回查找到的元素
def btest(dict_test):
    for aa in dict_test:
        for key, value in aa.items():
            if 4 == value:
                yield aa


ff = btest(dict_test)
print(ff)
for nn in ff:
    print(nn)
