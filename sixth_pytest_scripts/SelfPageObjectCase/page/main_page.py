#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'mainpage'
__author__ = 'creamk'
__time__ = '2020/8/22 22:51'
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
from sixth_pytest_scripts.SelfPageObjectCase.page.add_member_page import AddMemberPage
from sixth_pytest_scripts.SelfPageObjectCase.page.import_contactlist_page import ImportConPage


class MainPage(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact_page(self):
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()
        return ContactPage(self._driver)

    def goto_add_member_page(self):
        self.find(By.CSS_SELECTOR, '[node-type="addmember"').click()
        return AddMemberPage(self._driver)

    def goto_import_contactlist_page(self):
        self.find(By.CSS_SELECTOR, '[node-type="import"').click()
        return ImportConPage(self._driver)
