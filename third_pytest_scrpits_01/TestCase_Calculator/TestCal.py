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
import pytest
import yaml
from python_scripts.third_pytest_scrpits_01.Calculator.MyCalculator import Calculator


def get_data(key):
    with open('../datas.yml') as f:
        data = yaml.safe_load(f)
        # for data in data[key]:
        #     return tuple(data)
        for data in data[key]:
            yield tuple(data)


class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

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
        result = self.cal.add(a, b)
        assert expect == result

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