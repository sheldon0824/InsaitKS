import unittest
import time
import os.path
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage
from pageobjects.player_page import PlayerPage
from pageobjects.team_page import TeamPage


class PlayerUpdate(unittest.TestCase):
    """新增一支球队并且批量导入一批球员，而后删除"""
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_BulkImportPlayers(self):

        loginPage = LoginPage(self.driver)
        playPage = PlayerPage(self.driver)
        teamPage = TeamPage(self.driver)

        """登录国内环境"""
        loginPage.type_china_account('automated01', 'admin123')
        loginPage.send_submit_btn()
        loginPage.take_window_img("LoginAccountCN")
        loginPage.sleep(3)
        if loginPage.login_account_name() == 'Automated01':
            print("Login to China server successfully!")
        else:
            print("Failed on login to China!")

        """打开球队菜单，并新增一支球队"""
        teamPage.create_team(time.strftime("TeamName%Y%m%d%H%M%S", time.localtime()))

        """进入这支球队，批量导入球员"""
        excel_path = os.path.dirname(os.path.abspath('.')) + '/tools/导入模板.xlsx'  # 此文档有 20 位球员
        teamPage.bulk_in_team(excel_path)

        """删除这批球员"""  # 也可以通过触发搜索球员名字来实现删除测试数据
        playPage.del_page_players()
        playPage.del_page_players()  # 一页删 10 个，删了 2 次

        """删除这支球队"""
        teamPage.del_team()

        # """用户登出"""
        # login_page = LoginPage(self.driver)
        # login_page.logout()
        # login_page.take_window_img("LogoutCN")


if __name__ == '__main__':
    unittest.main()
