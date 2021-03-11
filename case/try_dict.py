# aa = {"a": 3, "b": 3}
# bb = aa.update({"cc": 44})
# print(aa)
# print(len(aa))
# print(bb)

import sys, traceback


# print(traceback.print_exc())
# print(sys.exc_info())
# print(len(sys.exc_info()))
# print(sys.exc_info()[0])

# t = (1, 2, 3)
# print(t[2])
#
# aa = None
# if str(aa):
#     print("111")
# else:
#     print("22")
#
# import sys
#
# m1 = 10000000
# print(sys.getrefcount(m1))

# mm = {}
# nn = []
# print(mm)
# print(mm.items())
# # for key, value in mm.items():
# if  mm:
#     print("aa")
# else:
#     print("bb")

# li = [1, 2, 3, 4, 5]
# tu = (1, 2, 3, 4, 5)
# str = "12345"
# print(li[::-1])
# print(tu[::-1])
# print(str[::-1])

# list = ['a', 'b', 'c', 'd', 'e']
# print(list[10:])
# print(list[3])
# print(list[10])

# keys = ['Name', 'Sex', 'Age']
# values = ['Jack', 'Male', 23]
# mm = zip(keys, values)
# nn = dict(mm)
# print(nn)
# print(nn.get('Age'))

# keys = ['Name', 'Sex', 'Age']
# values = ['Jack', 'Male', 23]
# bb = list(zip(keys, values))
# print(bb)
#
# aa = dict(bb)
# print(aa)
# print(aa.get('Sex'))
# print(3 / 2)
# print(3 // 2)
# 结果是：
# 1.5
# 1

def aa(name=[]):
    print(name)
    name.append(123)
    return name
print(aa())
print(aa())
# 结果为：
# []
# [123]
# [123]
# [123, 123]