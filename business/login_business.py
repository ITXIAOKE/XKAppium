# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com
from handle.login_handle import LoginHandle


# 操作登录页面的，业务层
class LoginBusiness:
    def __init__(self, i):
        self.login_handle = LoginHandle(i)

    def login_success(self):
        self.login_handle.send_username("15101658189")
        self.login_handle.send_password("1991117abcxz")
        self.login_handle.click_login()

    def login_user_error(self):
        self.login_handle.send_username("15101658188")
        self.login_handle.send_password("1991117abcxz")
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost("账号未注册")
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        self.login_handle.send_username("15101658189")
        self.login_handle.send_password("1243566")
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost("登录密码错误")
        if user_flag:
            return True
        else:
            return False
