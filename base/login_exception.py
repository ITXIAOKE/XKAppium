# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com
class LoginException:
    # 这个exception_list列表必须定义为类变量，这样就可以作为公共的列表，添加异常信息了
    exception_list = []

    def exception_append_value(self, value):
        self.exception_list.append(value)

    def get_exception_length(self):
        return len(self.exception_list)
