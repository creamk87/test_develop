#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'Test_Develop'
__file_name__ = 'TestCal_4thday'
__author__ = 'creamk'
__time__ = '2020/8/15 22:35'
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
import os

import yaml

from python_scripts.third_pytest_scripts_01.Calculator.MyCalculator import Calculator
import pytest
import allure


def get_data(method):
    my_data_path = os.path.dirname(__file__) + "/datas.yml"
    print(my_data_path)
    with open(my_data_path, encoding='utf-8') as f:
        my_data = yaml.safe_load(f)
        test_data = my_data[method]
    return test_data


class TestCal:
    @pytest.mark.parametrize(['a', 'b', 'expect'], get_data('integer_add'),
                             ids=['result_01', 'result_02', 'result_03', 'result_04'])
    def test_add_integer(self, a, b, expect, initialize):
        result = initialize.add(a, b)
        assert result == expect

    @pytest.mark.parametrize(['a', 'b', 'expect'], get_data('integer_add'),
                             ids=['result_01', 'result_02', 'result_03', 'result_04'])
    def test_add_float(self, a, b, expect, initialize):
        result = round(initialize.add(a, b), 2)
        assert result == expect

    @pytest.mark.parametrize(['a', 'b', 'expect'], get_data('integer_div'),
                             ids=['result_01', 'result_02', 'result_03', 'result_04'])
    def test_div_integer(self, a, b, expect, initialize):
        result = initialize.div(a, b)
        assert result == expect

