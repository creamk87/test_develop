#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'Test_Develop'
__file_name__ = 'conftest'
__author__ = 'creamk'
__time__ = '2020/8/15 22:38'
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
import pytest
import os
import yaml
from python_scripts.third_pytest_scripts_01.Calculator.MyCalculator import Calculator


@pytest.fixture(scope='module')
def initialize():
    print("------开始计算------")
    cal = Calculator()
    yield cal
    print("------结束计算------")

