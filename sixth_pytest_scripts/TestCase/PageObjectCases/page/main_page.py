#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'main_page'
__author__ = 'creamk'
__time__ = '2020/8/22 20:30'
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from sixth_pytest_scripts.TestCase.PageObjectCases.page.BasePage import BasePage
from sixth_pytest_scripts.TestCase.PageObjectCases.page.add_member_page import AddMember
from sixth_pytest_scripts.TestCase.PageObjectCases.page.contact_page import ContactPage


class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact(self):
        return ContactPage(self.driver)

    def goto_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, "[]").click()
        return AddMember(self.driver)
