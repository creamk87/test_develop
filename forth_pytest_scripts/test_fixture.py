#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'Test_Develop'
__file_name__ = 'test_fixture'
__author__ = 'creamk'
__time__ = '2020/8/15 20:05'
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


# pytest中添加yield，能够激活fixture teardown
@pytest.fixture()
# 当使用autouse之后，自动使用带当前所有测试用例中，不需要传入fixture函数名，这时，传入的是fun对象
# 当函数内需要使用fixture函数中的返回值时，必须要传入到测试函数的参数中
# scope参数，可以控制fixture的作用范围，session > module > class > function

# @pytest.fixture()
def login():
    # yield之前的代码相当于setup
    print("登录函数")
    username = "ll"
    password = "123456"
    # return [username, password]
    yield [username, password]
    # yield之后的代码相当于teardown
    print("登出系统")


def test_case1(login):
    print(f"测试用例1----需要登录{login}")


def test_case2():
    print("测试用例2----不需要登录")


def test_case3():
    print(f"测试用例3----需要登录{login}")


@pytest.mark.usefixtures("login")
def test_case4():
    print(f"测试用例4----需要登录{login}")
