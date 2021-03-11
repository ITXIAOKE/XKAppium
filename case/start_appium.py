# -*- coding: utf-8 -*-
# @Author  : xiaoke
# @Email   : 976249817@qq.com

from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.get_by_local import GetByLocal


def get_driver():
    capabilities = {
        "platformName": "Android",
        # 这行代码是为了获取5.0以上手机的toast，默认是appium
        # "automationName": "UiAutomator2",
        "deviceName": "127.0.0.1:62001",
        "app": "E:\\pycharmProject\\appium\\appiumProject\\app\\mukewang.apk",
        # 模拟器调试
        # "appActivity": "cn.com.open.mooc.index.splash.GuideActivity"
        # 真机调试
        # "appWaitActivity": "cn.com.open.mooc.index.splash.GuideActivity",
        # "appWaitActivity": "cn.com.open.mooc.user.register.MCPhoneRegisterAty",
        # "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    sleep(5)
    # 切换activity的方法
    # driver.wait_activity()
    return driver


# 获取屏幕的宽和高
def get_size():
    # 获取屏幕的大小
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 向左边滑动
def swipe_left(time=None):
    # 大坐标点
    x1 = get_size()[0] / 10 * 9
    y = get_size()[1] / 2
    # 小坐标点
    x2 = get_size()[0] / 10
    driver.swipe(x1, y, x2, y, time)


# 向右边滑动
def swipe_right(time=None):
    # 大坐标点
    x1 = get_size()[0] / 10 * 9
    y = get_size()[1] / 2
    # 小坐标点
    x2 = get_size()[0] / 10
    driver.swipe(x2, y, x1, y, time)


# 向上边滑动
def swipe_up(time=None):
    # 大坐标点
    x = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    # 小坐标点
    y2 = get_size()[1] / 9
    driver.swipe(x, y1, x, y2, time)


# 向下边滑动
def swipe_down(time=None):
    # 大坐标点
    x = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    # 小坐标点
    y2 = get_size()[1] / 10
    driver.swipe(x, y2, x, y1, time)


# 根据指定的滑动方向，选择滑动的函数
def swipe_on(direction=None, time=None):
    if direction == "up":
        swipe_up(time)
    elif direction == "down":
        swipe_down(time)
    elif direction == "left":
        swipe_left(time)
    else:
        swipe_right(time)


# 点击已有账号，去登录
def go_login():
    driver.find_element_by_id("cn.com.open.mooc:id/tv_go_login").click()


# 点击登录按钮
def login():
    get_by_local = GetByLocal(driver)
    get_by_local.get_element("username").send_keys("15101658189")
    get_by_local.get_element("password").send_keys("1991")
    get_by_local.get_element("login_button").click()


# 通过类名点击登录
def login_by_class_name():
    # 找到一组textView
    elements = driver.find_elements_by_class_name("android.widget.TextView")
    # 通过uiautomationView查看要点击的textView的角标
    elements[4].click()


# 通过层级节点找到用户名和密码输入的框
def login_by_node():
    # 找到最外层的scrollView
    scrollview = driver.find_element_by_id("cn.com.open.mooc:id/sv_scrollview")
    # 找到该scrollView下面的所有editText
    elements = scrollview.find_elements_by_class_name("android.widget.EditText")
    # 用户名输入框
    elements[0].send_keys("15101658189")
    # 密码输入框
    elements[1].send_keys("199")
    # driver.find_element_by_id("cn.com.open.mooc:id/login").click()


# 通过杀手锏，uiautomator定位
def login_uiautomator():
    driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').clear()
    driver.find_element_by_android_uiautomator('new UiSelector().text("手机号/邮箱")').send_keys("15101658189")
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("cn.com.open.mooc:id/password_edit")').clear()
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("cn.com.open.mooc:id/password_edit")').send_keys("19")


# 通过xpath来定位，但是在移动端不推荐用xpath，因为xpath效率太低
def login_by_xpath():
    # driver.find_element_by_xpath('//*[contains(@text,"忘记密码")]').click()
    # driver.find_element_by_xpath('//android.widget.TextView[@text="忘记密码"]').click()
    # 下面两种方式没有成功
    # driver.find_element_by_xpath(
    #     '//android.widget.TextView[@resource-id="cn.com.open.mooc:id/forget_lable"]/../preceding-sibling::*[@index="1"]') \
    #     .send_keys("123456")
    # driver.find_element_by_xpath(
    #     '//android.widget.TextView[@resource-id="cn.com.open.mooc:id/forget_lable"]/../preceding-sibling::*[@index="2"]') \
    #     .send_keys("1111111")
    driver.find_element_by_xpath('//*[contains(@text,"手机号/邮箱")]').clear()
    driver.find_element_by_xpath('//*[contains(@text,"手机号/邮箱")]').send_keys("123456")
    driver.find_element_by_xpath('//android.widget.EditText[@resource-id="cn.com.open.mooc:id/password_edit"]').clear()
    driver.find_element_by_xpath(
        '//android.widget.EditText[@resource-id="cn.com.open.mooc:id/password_edit"]').send_keys("111111")


def get_web_view():
    # WebView.setWebContentsDebuggingEnabled(true);
    sleep(10)
    webview = driver.contexts
    for viw in webview:
        if 'WEBVIEW_cn.com.open.mooc' in viw:
            driver.switch_to.context(viw)
            break
    driver.find_element_by_link_text('C').click()
    try:
        driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
    except Exception as e:
        # 在抛出异常之前先切换回原来的上下文环境
        driver.switch_to.context(webview[0])
        driver.find_element_by_id('cn.com.open.mooc:id/left_icon').click()
        raise e  # 抛出异常的信息
    print(webview)


# 注意这个toast的获取必须在5.0以上的机器上运行
def get_toast():
    sleep(2)
    driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('18513199586')
    toast_element = ("xpath", "//*[coantains(@text,'请输入密码')]")
    # webdriverwait。。。。until....
    ele = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(toast_element))
    print(ele)


if __name__ == '__main__':
    driver = get_driver()
    swipe_on("left")
    sleep(1)
    swipe_on("left", 1000)
    sleep(1)
    swipe_on("right")
    sleep(1)
    swipe_on("right", 1000)
    # 进入注册页面
    swipe_on("left")
    swipe_on("left")
    sleep(2)
    swipe_on("up", 3000)
    sleep(2)
    go_login()
    sleep(1)
    login()
    # sleep(1)
    # login_by_class_name()
    # sleep(1)
    # login_by_node()
    # login_uiautomator()
    # login_by_xpath()
    # get_web_view()
