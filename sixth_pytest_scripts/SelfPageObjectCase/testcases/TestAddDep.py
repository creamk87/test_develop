#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'TestAddDep'
__author__ = 'creamk'
__time__ = '2020/8/23 01:09'
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
from sixth_pytest_scripts.SelfPageObjectCase.page.main_page import MainPage


class TestAddDepCase:

    def test_add_department(self):
        main_page = MainPage()
        main_page.goto_contact_page().goto_add_department_page().add_department('拉勾3期内推组')
        result = main_page.goto_contact_page().get_department_list()
        print(result)
        assert '拉勾3期内推组' in result
