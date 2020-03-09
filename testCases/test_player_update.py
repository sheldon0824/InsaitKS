import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage
from pageobjects.player_page import PlayerPage


class PlayerUpdate(unittest.TestCase):
    """在国内登录，新增一名球员，再编辑该球员，而后删除"""
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_PlayerUpdateFlow(self):

        loginPage = LoginPage(self.driver)
        updatePlayer = PlayerPage(self.driver)

        """登录国内环境"""
        loginPage.type_china_account('automated01', 'admin123')
        loginPage.send_submit_btn()
        if loginPage.login_account_name() == 'Automated01':
            print("Login to China server successfully!")
        else:
            print("Failed on login to China!")

        """打开添加球员的二级页面并且新增一个球员"""
        js_birthday = "document.getElementById('birthday').removeAttribute('readonly')"

        updatePlayer.open_add_player()
        updatePlayer.input_player_info(time.strftime("Name_%Y%m%d-%H%M%S", time.localtime()),
                                       time.strftime("ID%Y%m%d%H%M%S", time.localtime()),  # -%H%M%S
                                       "1999-12-25",
                                       170,
                                       50,)
        """编辑保存这名新球员"""
        updatePlayer.update_player_info(time.strftime("Name_%Y%m%d-%H%M%S", time.localtime()))

        """删除球员"""
        updatePlayer.del_first_player()

        # """用户登出"""
        # login_page = LoginPage(self.driver)
        # login_page.logout()
        # login_page.take_window_img("LogoutCN")


if __name__ == '__main__':
    unittest.main()
