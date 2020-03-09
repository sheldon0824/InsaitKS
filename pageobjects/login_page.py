from framework.base_page import BasePage


class LoginPage(BasePage):
    """
    可以这样设想，一个page object可以先将一个页面的所有element都列出来，
    对每个element都进行命名，即变量名，并写出它的定位方式
    """
    username = "id=>username"  # 输入用户名
    password = "id=>password"  # 输入密码
    drop_down = "xpath=>//*/input[@class='dropdown-value']"   # 先点击选择了下拉框
    China = "xpath=>//*[@class='dropdown-menu']/li[2]"    # 选择国内环境
    Frankfurt = "xpath=>//*[@class='dropdown-menu']/li[contains(text(),'荷兰')]"  # 法兰克福数据中心 - 荷兰Nederland
    Singapore = "xpath=>//*/li[contains(text(),'新加坡')]"   # 新加坡数据中心 - 新加坡 Singapore
    login_btn = "xpath=>//*[@type='submit']"  # 登录按钮

    homepage_username = "xpath=>//*/span[@class='username']"  # 登录后的用户名称
    logout_btn = "xpath=>//*/img[@alt='退出']"  # 用户登出按钮

    def type_china_account(self, text1, text2):
        self.type(self.username, text1)  # base_page.type(self, selector, text)
        self.type(self.password, text2)
        self.click(self.drop_down)
        self.click(self.China)
        self.take_window_img("LoginCN")

    def type_frankfurt_account(self, text1, text2):
        self.type(self.username, text1)  # base_page.type(self, selector, text)
        self.type(self.password, text2)
        self.click(self.drop_down)
        self.click(self.Frankfurt)
        self.take_window_img("LoginEU")

    def type_singapore_account(self, text1, text2):
        self.type(self.username, text1)  # base_page.type(self, selector, text)
        self.type(self.password, text2)
        self.click(self.drop_down)
        self.click(self.Singapore)
        self.take_window_img("LoginSGP")

    def send_submit_btn(self):
        self.click(self.login_btn)
        self.sleep(5)

    def login_account_name(self):
        return self.get_text(self.homepage_username)

    def logout(self):
        self.click(self.logout_btn)
        self.take_window_img("Logout")

