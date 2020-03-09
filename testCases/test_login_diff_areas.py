import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage


class LoginCN(unittest.TestCase):
    """登录国内环境"""
    @classmethod  # 用于同一个类下多个test()时，只执行一次setUp()和tearDown()
    def setUpClass(cls):
        """
        写【测试固件】时，需要的套件之一，setUp()主要为测试固件开始时的前期准备
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        写【测试固件】时，需要的套件之一，tearDown()是指测试结束时候的操作，一般是指关闭浏览器啦
        :return:
        """
        cls.driver.quit()

    def test_login_mainland(self):
        """登录国内环境"""
        """
        注意测试固件的用例方法一定要用test开头
        :return:
        """
        loginpage = LoginPage(self.driver)
        """
        为什么这里要 self.driver?
        到一个新的页面，第一件事情就是初始化这个页面的‘一个页面对象实例’。
        这个self.driver可以这么理解：它是从browser_engine实例出来的，在初始化一个页面对象的时候，也把这个来自browser_engine的
        driver赋值给了这个页面对象，这样才能执行调用页面对象或者基类里面的相关driver方法。
        最重要的是，要保持driver一致。
        """
        loginpage.type_china_account('proqa3', 'admin123')
        loginpage.send_submit_btn()
        if loginpage.login_account_name() == 'proqa3':
            print("Login to China server successfully!")
        else:
            print("Failed on login to China!")

    def test_logout(self):
        """用户登出"""
        loginpage = LoginPage(self.driver)
        loginpage.logout()


class LoginEU(unittest.TestCase):
    """登录法兰克福环境"""
    @classmethod  # 用于同一个类下多个test()时，只执行一次setUp()和tearDown()
    def setUpClass(cls):
        """
        写【测试固件】时，需要的套件之一，setUp()主要为测试固件开始时的前期准备
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        写【测试固件】时，需要的套件之一，tearDown()是指测试结束时候的操作，一般是指关闭浏览器啦
        :return:
        """
        cls.driver.quit()

    def test_login_EU(self):
        """登录法兰克福数据中心"""
        loginpage = LoginPage(self.driver)
        loginpage.type_frankfurt_account('euproqa5', 'admin123')
        loginpage.send_submit_btn()

        if loginpage.login_account_name() == 'BeastLaLo':
            print("Login to Frankfurt data center successfully!")
        else:
            print("Failed on login to Frankfurt data center!")

    def test_logout(self):
        """用户登出"""
        loginpage = LoginPage(self.driver)
        loginpage.logout()


class LoginSGP(unittest.TestCase):
    """登录新加坡环境"""
    @classmethod  # 用于同一个类下多个test()时，只执行一次setUp()和tearDown()
    def setUpClass(cls):
        """
        写【测试固件】时，需要的套件之一，setUp()主要为测试固件开始时的前期准备
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        写【测试固件】时，需要的套件之一，tearDown()是指测试结束时候的操作，一般是指关闭浏览器啦
        :return:
        """
        cls.driver.quit()

    def test_login_SGP(self):
        """登录新加坡数据中心"""
        loginpage = LoginPage(self.driver)
        loginpage.type_singapore_account('sgpqa1', 'admin123')
        loginpage.send_submit_btn()

        if loginpage.login_account_name() == 'sgpqa1':
            print("Login to Singapore data center successfully!")
        else:
            print("Failed on login to Singapore data center!")

    def test_logout(self):
        """用户登出"""
        loginpage = LoginPage(self.driver)
        loginpage.logout()


if __name__ == '__main__':
    unittest.main()

