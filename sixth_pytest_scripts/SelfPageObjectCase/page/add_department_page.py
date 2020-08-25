#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'add_department_page'
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


class AddDepPage(BasePage):
    def add_department(self, department_name):
        self.find(By.CSS_SELECTOR, 'input[class$=ww_inputText][name=name]').send_keys(department_name)
        self.find(By.CSS_SELECTOR, 'div[class$=member_tag_dialog] li[id=1688852909985302]>a[class=jstree-anchor][id=1688852909985302_anchor]').click()
        self.find(By.CSS_SELECTOR, 'div[class$=member_tag_dialog] a[d_ck=submit]').click()
        return ContactPage(self._driver)
