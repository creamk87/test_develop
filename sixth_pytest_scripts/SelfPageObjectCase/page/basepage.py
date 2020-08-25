#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'basepage'
__author__ = 'creamk'
__time__ = '2020/8/22 22:59'
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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver


class BasePage:
    _url = ""

    def __init__(self, driver=None):
        if driver is None:
            options = Options()
            options.debugger_address('localhost:9222')
            self._driver = webdriver.Chrome(options=options)
        else:
            self._driver: WebDriver = driver
        if self._url != "":
            self._driver.get(self._url)

    def find(self, by, value):
        return self._driver.find_element(by=by, value=value)

    def finds(self, by, value):
        return self._driver.find_elements(by=by, value=value)
