#!/Library/Frameworks/Python.framework/Versions/3.7/bin python3
"""
__project_ = 'python_scripts'
__file_name__ = 'Test_Frame'
__author__ = 'creamk'
__time__ = '2020/8/22 10:43'
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
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestFrame:
    def setup(self):
        # 从终端给传递参数,多浏览器处理
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

        self.url1 = 'https://www.baidu.com'
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
        # pass

    def test_window(self):
        self.driver.get(self.url1)
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 切换handle
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        print(windows[-1].title())
        # 查找用户名、密码输入窗口
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__userName").send_keys("zw6862439")
        self.driver.find_element(By.ID, "TANGRAM__PSP_4__phone").send_keys(13800000000)
        # 再次切换handle
        self.driver.switch_to.window(windows[0])
        sleep(3)
        # 点击用户名登录
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__userName").send_keys("creamk87")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__password").send_keys("6862439ck")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()
        sleep(4)

    def test_js_scroll(self):
        self.driver.get(self.url1)
        self.driver.find_element(By.ID, "kw").send_keys("selenium测试")
        # 点击"百度以下"按钮
        # self.driver.find_element(By.ID, "su").click()
        # 执行js脚本，找到"百度一下"按钮，然后调用对象的click方法点击按钮
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        sleep(1)
        # 返回页面的title和页面加载性能数据
        for code in ['return document.title', 'return JSON.stringify(performance.timing)']:
            print(self.driver.execute_script(code))
        # selenium测试_百度搜索
        # {"connectStart":1598073116690,"navigationStart":1598073116600,"loadEventEnd":1598073117585,
        # "domLoading":1598073116845,"secureConnectionStart":1598073116727,"fetchStart":1598073116648,
        # "domContentLoadedEventStart":1598073117250,"responseStart":1598073116833,
        # "responseEnd":1598073116870,"domInteractive":1598073117250,"domainLookupEnd":1598073116690,
        # "redirectStart":0,"requestStart":1598073116797,"unloadEventEnd":0,"unloadEventStart":0,
        # "domComplete":1598073117579,"domainLookupStart":1598073116690,"loadEventStart":1598073117579,
        # "domContentLoadedEventEnd":1598073117268,"redirectEnd":0,"connectEnd":1598073116796}

        # 执行滑动到最底端操作
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)

    def test_12306_timezone(self):
        self.driver.get("https://www.12306.cn/index/")
        date = '2020-12-31'
        self.driver.execute_script("time_element=document.getElementById('train_date');"
                                   "time_element.removeAttribute('readonly');")
        self.driver.execute_script(f"document.getElementById('train_date').value='{date}'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(3)

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # 查找拖拽和放置的2个元素
        drag = self.driver.find_element(By.ID, "draggable")
        drop = self.driver.find_element(By.ID, "droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        self.driver.switch_to.alert.accept()
        # 切换回默认的iframe
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submitBTN").click()
        sleep(3)
