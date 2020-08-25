#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'contact_page'
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
from sixth_pytest_scripts.SelfPageObjectCase.page.add_member_page import AddMemberPage
from sixth_pytest_scripts.SelfPageObjectCase.page.add_department_page import AddDepPage
from sixth_pytest_scripts.SelfPageObjectCase.page.import_contactlist_page import ImportConPage


class ContactPage(BasePage):

    def goto_add_member_page(self):
        self.find(By.CSS_SELECTOR, 'div[class=ww_operationBar]>a[class$=js_add_member]').click()
        return AddMemberPage(self._driver)

    def goto_add_department_page(self):
        self.find(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        return AddDepPage(self._driver)

    def goto_import_contactlist_page(self):
        self.find(By.CSS_SELECTOR, 'div[class=ww_operationBar]>div[class$=js_import_other_wrap]').click()
        self.find(By.CSS_SELECTOR, 'div[class=ww_operationBar]>div[class$=ww_btnWithMenu_Open]>div[class$=ww_dropdownMenu]>ul>li>a[class$=js_import_member]').click()
        return ImportConPage(self._driver)

    def get_department_list(self):
        return self.finds(By.CSS_SELECTOR, 'div[aria-activedescendant=1688852892996541] a').text
