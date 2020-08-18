#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'Test_Develop'
__file_name__ = 'test_conftest'
__author__ = 'creamk'
__time__ = '2020/8/15 20:38'
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


# 使用conftest这个文件进行数据共享，
# 测试用例会优先读取当前模块下的fixture方法
# 其次读取当前目录下定义的conftest.py文件里面的fixture方法
# 最后，才会在项目下逐层向上查找conftest.py文件里的fixture方法

def test_case1(login):
    print(f"测试用例1----需要登录{login}")


def test_case2():
    print("测试用例2----不需要登录")


def test_case3(login):
    print(f"测试用例3----需要登录{login}")


def test_case4(login):
    print(f"测试用例4----需要登录{login}")
