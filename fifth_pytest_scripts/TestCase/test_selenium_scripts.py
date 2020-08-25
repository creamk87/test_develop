#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'Test_Develop'
__file_name__ = 'test_selenium_scripts'
__author__ = 'creamk'
__time__ = '2020/8/18 19:51'
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
import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestSelenium:

    def setup_class(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        self.url = "https://work.weixin.qq.com/wework_admin/frame#index"
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        db = shelve.open("mydb/login_cookies")
        db['cookies'] = cookies
        db.close()

    def test_wechat(self):
        self.driver.get(self.url)
        self.save_cookies()

    def test_cookie_login(self):
        self.driver.get(self.url)
        self.save_cookies()
        assert "退出" == self.driver.find_element(By.ID, "logout").text

    def test_cookie1(self):

        # Shelve 小型的数据库， 对象持久化保存方法，
        db = shelve.open("mydb/login_cookies.db")
        cookies = db['cookies']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

    def test_add_content(self):
        self.driver.find_element(By.XPATH, '//a[@class="index_service_cnt_itemWrap"][2]').click()
        self.driver.find_element(By.ID, 'js_upload_file_input').send_keys('/Users/CreamK/WorkDirectory/ME/Document/mydata.xlsx')
