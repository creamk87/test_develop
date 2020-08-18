#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'Test_Develop'
__file_name__ = 'TestCal'
__author__ = 'creamk'
__time__ = '2020/8/12 20:26'
__product_name = PyCharm
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃        ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻   ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑  ┣┓
                ┃　永无BUG！ ┏┛
                ┗┓┓ ┏ ━┳┓ ┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import allure
import pytest
import yaml
import sys

# sys.path.append("..")
# print(sys.path)
from python_scripts.third_pytest_scripts_01.Calculator.MyCalculator import Calculator


def get_data(key):
    with open("../datas.yml") as f:
        data = yaml.safe_load(f)
        for data in data[key]:
            yield tuple(data)


@allure.feature("计算器")
class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @allure.story("整数加法")
    @pytest.mark.parametrize(
        ['a', 'b', 'expect'],
        [data for data in get_data('integer_add')],
        ids=[
            '整数加法_结果1',
            '整数加法_结果2',
            '整数加法_结果3',
            '整数加法_结果4'
        ])
    def test_integer_add(self, a, b, expect):
        with allure.step("得到计算结果"):
            print("得到计算结果")
            result = self.cal.add(a, b)
        with allure.step("断言结果"):
            print("断言判断")
            assert expect == result

    @allure.story("整数除法")
    @pytest.mark.parametrize(
        ['a', 'b', 'expect'],
        [data for data in get_data('integer_div')],
        ids=[
            '整数除法_结果1',
            '整数除法_结果2',
            '整数除法_结果3',
            '整数除法_结果4'
        ])
    def test_integer_div(self, a, b, expect):
        result = self.cal.div(a, b)
        assert expect == result

    @allure.story("小数加法")
    @pytest.mark.parametrize(
        ['a', 'b', 'expect'],
        [data for data in get_data('float_add')],
        ids=[
            'float_add_result1',
            'float_add_result2',
            'float_add_result3'
        ])
    def test_float_add(self, a, b, expect):
        result = self.cal.add(a, b)
        assert expect == result

    @allure.story("小数除法")
    @allure.link("https://www.baidu.com", name="百度")
    @pytest.mark.parametrize(
        ['a', 'b', 'expect'],
        [data for data in get_data('float_div')],
        ids=[
            'float_div_result1',
            'float_div_result2',
            'float_div_result3'
        ])
    def test_float_div(self, a, b, expect):
        result = self.cal.div(a, b)
        assert expect == result
