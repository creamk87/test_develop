#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'Test_case_appium'
__author__ = 'creamk'
__time__ = '2020/8/26 12:17'
__product_name = PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃        ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestWechat:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_delete_contact(self):
        name = '暖男'
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'通讯录')]").click()
        self.driver.find_element(MobileBy.XPATH, f"//*[contains(@text,'{name}')]").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '编辑成员')]").click()
        # 获取当前窗口的宽、高
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        print(window_rect)
        height = window_rect['height']
        sleep(3)
        # 滑动屏幕，从下往上划
        action.press(x=0, y=height * 0.8).wait(200).move_to(x=0, y=height * 0.2).release().perform()
        sleep(3)
        # 删除成员，并确定
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '删除成员')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '确定')]").click()
        # 找到搜索按钮，搜索联系人
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id, 'com.tencent.wework:id/hk9')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id, 'com.tencent.wework:id/g75')]").send_keys(name)
        result = self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id, 'com.tencent.wework:id/c5m')]").text
        assert "无搜索结果" == result

