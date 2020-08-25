#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'test_add_member'
__author__ = 'creamk'
__time__ = '2020/8/22 20:36'
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
from sixth_pytest_scripts.TestCase.PageObjectCases.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        self.main = MainPage()
        #  跳转到添加成员页面 --> 添加成员
        self.main.goto_add_member().add_member()

    def test_contact_add_member(self):
        self.main = MainPage()
        #  跳转到通讯录页面 --> 跳转到添加成员页面 --> 添加成员
        self.main.goto_contact().goto_add_member().add_member()
