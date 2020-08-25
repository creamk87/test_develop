#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'add_member_page'
__author__ = 'creamk'
__time__ = '2020/8/22 22:52'
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
from selenium.webdriver.common.by import By
from sixth_pytest_scripts.SelfPageObjectCase.page.basepage import BasePage
from sixth_pytest_scripts.SelfPageObjectCase.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_member(self, username, acctid):
        self.find(By.CSS_SELECTOR, '#username').send_keys(username)
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(acctid)
        self.find(By.CSS_SELECTOR, 'a[class$=js_btn_save]').click()
        return ContactPage(self._driver)
